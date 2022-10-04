export WellTankHeuristic

struct WellTankHeuristic <: Heuristic
    min_well_tank_dists::Dict{Any,Int}
    #min_well_tank_dists::Dict{Const, Int} 
end

function WellTankHeuristic()
    min_well_tank_dists = Dict{Const,Int}()
    return WellTankHeuristic(min_well_tank_dists)
end

function get_obj_loc(state::State, obj::Const)
    xloc = state[Compound(:xloc, Term[obj])]
    yloc = PDDL.get_fluent(state, Compound(:yloc, Term[obj]))
    return (xloc, yloc)
end

function precompute!(h::WellTankHeuristic,
                     domain::Domain, state::State, spec::Specification)
    wells = PDDL.get_objects(state, :well)
    tanks = PDDL.get_objects(state, :tank)
    h.min_well_tank_dists = Dict{Const,Int}()
    well_locs = [get_obj_loc(state, w) for w in wells]
    tank_locs = [get_obj_loc(state, t) for t in tanks]
    for (w, well_loc) in zip(wells, well_locs)
        min_dist = typemax(Int)
        for tank_loc in tank_locs
            well_tank_dist = sum(abs.(well_loc .- tank_loc))
            min_dist = min(well_tank_dist, min_dist)
        end
        h.min_well_tank_dists[w] = min_dist
    end
    return h 
end

function is_precomputed(h::WellTankHeuristic,
                        domain::Domain, state::State, spec::Specification)
    return isdefined(h, :min_well_tank_dists)
end

function compute(h::WellTankHeuristic, 
                 domain::Domain, state::State, spec::Specification)
    # Precompute if necessary
    if !is_precomputed(h, domain, state, spec)
        precompute!(h, domain, state, spec)
    end

    # Find max heuristic distance to goal across agents
    max_dist = 0

    agents = PDDL.get_objects(state, :agent)
    wells = PDDL.get_objects(state, :well)
    tanks = PDDL.get_objects(state, :tank)

    for a in agents 
        task_completed = Compound(Symbol("has-filled"), Term[a])
        water_collected = Compound(Symbol("has-water"), Term[a])
            
        #condition, agent has completed the tanks
        #then return 0
        if state[task_completed] #if satisfy(domain, state , Compound(Symbol(“has-filled”), Term[a])
            return 0
        end
        #condition, agent hasn't gotten the water yet
        #then return the minimum distance precomputed in all the min_well_tank_dists
        if !state[water_collected]
            return minimum(values(h.min_well_tank_dists))
        end

        agent_loc = get_obj_loc(state, a)
        agent_dist = Inf
        for w in wells
            well_loc = get_obj_loc(state, w)
            agent_well_dist = sum(abs.(well_loc .- agent_loc))
            for t in tanks
                tank_loc = get_obj_loc(state, t)
                well_tank_dist = sum(abs.(well_loc .- tank_loc))
                agent_dist = min(agent_dist, agent_well_dist + well_tank_dist)
            end
            max_dist = max(agent_dist,max_dist)
        end
    end 
    return max_dist
end