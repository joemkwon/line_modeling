export StateConstrainedGoal

"Goal specification with constraints that must hold for every state."
struct StateConstrainedGoal{G <: Goal} <: Goal
    goal::G
    constraints::Vector{Term}
end

function StateConstrainedGoal(problem::Problem)
    # Convert problem to underlying goal
    goal = Specification(problem)::Goal
    # Get constraints
    constraints = PDDL.get_constraints(problem)::Term
    return StateConstrainedGoal(goal, constraints)
end
StateConstrainedGoal(goal::Goal, constraints::Term) =
    StateConstrainedGoal(goal, PDDL.flatten_conjs(constraints))

Base.hash(spec::StateConstrainedGoal, h::UInt) =
    hash(spec.constraints, hash(spec.goal, h))
Base.:(==)(s1::StateConstrainedGoal, s2::StateConstrainedGoal) =
    Set(s1.constraints) == Set(s2.constraints) && s1.goal == s2.goal

is_goal(spec::StateConstrainedGoal, domain::Domain, state::State) =
    is_goal(spec.goal, domain, state)
is_violated(spec::StateConstrainedGoal, domain::Domain, state::State) =
    !satisfy(domain, state, spec.constraints) ||
    is_violated(spec.goal, domain, state)
get_cost(spec::StateConstrainedGoal, d::Domain, s1::State, a::Term, s2::State) =
    get_cost(spec.goal, d, s1, a, s2)
get_reward(spec::StateConstrainedGoal, d::Domain, s1::State, a::Term, s2::State) =
    get_reward(spec.goal, d, s1, a, s2)
get_goal_terms(spec::StateConstrainedGoal) = get_goal_terms(spec.goal)
