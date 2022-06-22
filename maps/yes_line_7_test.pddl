(define (problem yes-line-7)
    (:domain multi_agent_lines)
    (:objects tank1 tank2 tank3 tank4 tank5 tank6 - tank well1 - well agent1 agent2 agent3 agent4 agent5 agent6 agent7 agent8 - agent)
    (:init  
        (= (walls)
            (transpose (bit-mat
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 1 0 0 0 0 0 0 0 0 0 0 1)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 1)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 1 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 1 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0))))

        (= (xloc tank1) 1)
        (= (yloc tank1) 5)
        (= (xloc tank2) 1)
        (= (yloc tank2) 6)
        (= (xloc tank3) 1)
        (= (yloc tank3) 7)
        (= (xloc tank4) 1)
        (= (yloc tank4) 8)
        (= (xloc tank5) 1)
        (= (yloc tank5) 9)
        (= (xloc tank6) 1)
        (= (yloc tank6) 10)

        (= (xloc well1) 14)
        (= (yloc well1) 4)

        (= (xloc agent1) 12)
        (= (yloc agent1) 4)
        (not (has-water agent1))
        (not (has-filled agent1))

        (= (xloc agent2) 11)
        (= (yloc agent2) 4)
        (not (has-water agent2))
        (not (has-filled agent2))

        (= (xloc agent3) 10)
        (= (yloc agent3) 4)
        (not (has-water agent3))
        (not (has-filled agent3))

        (= (xloc agent4) 9)
        (= (yloc agent4) 4)
        (not (has-water agent4))
        (not (has-filled agent4))

        (= (xloc agent5) 8)
        (= (yloc agent5) 4)
        (not (has-water agent5))
        (not (has-filled agent5))

        (= (xloc agent6) 7)
        (= (yloc agent6) 4)
        (not (has-water agent6))
        (not (has-filled agent6))

        (= (xloc agent7) 6)
        (= (yloc agent7) 4)
        (not (has-water agent7))
        (not (has-filled agent7))

        (= (xloc agent8) 5)
        (= (yloc agent8) 4)
        (not (has-water agent8))
        (not (has-filled agent8)))
        
    (:goal (and (has-filled agent1) (has-filled agent2) (has-filled agent3) (has-filled agent4) (has-filled agent5) (has-filled agent6) (has-filled agent7) (has-filled agent8)))
)