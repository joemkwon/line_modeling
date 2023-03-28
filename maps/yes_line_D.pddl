(define (problem yes-line-x)
    (:domain multi_agent_lines)
    (:objects tank1 tank2 tank3 tank4 tank5 tank6 - tank well1 well2 well3 well4 - well agent1 agent2 agent3 agent4 agent5 agent6 agent7 agent8 - agent)
    (:init  
        (= (walls)
            (transpose (bit-mat
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 1 0 1 1 1 0 0 0)
                (bit-vec 0 0 0 0 0 0 1 0 0 0 1 0 0 0)
                (bit-vec 0 0 0 0 0 0 1 0 0 0 1 0 0 0)
                (bit-vec 0 0 0 0 0 0 1 0 0 0 1 0 0 0)
                (bit-vec 0 0 0 0 0 0 1 0 0 0 1 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 1 1 1 1 1 1 1 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
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

        (= (xloc well1) 9)
        (= (yloc well1) 6)
        (= (xloc well2) 9)
        (= (yloc well2) 7)
        (= (xloc well3) 9)
        (= (yloc well3) 8)
        (= (xloc well4) 9)
        (= (yloc well4) 9)

        (= (xloc agent1) 14)
        (= (yloc agent1) 10)
        
        (= (xloc agent2) 14)
        (= (yloc agent2) 11)

        (= (xloc agent3) 14)
        (= (yloc agent3) 12)

        (= (xloc agent4) 13)
        (= (yloc agent4) 12)

        (= (xloc agent5) 12)
        (= (yloc agent5) 12)

        (= (xloc agent6) 11)
        (= (yloc agent6) 12)

        (= (xloc agent7) 10)
        (= (yloc agent7) 12)

        (= (xloc agent8) 9)
        (= (yloc agent8) 12)
    )
        
    (:goal 
        (and 
            (has-filled agent1) 
            (has-filled agent2) 
            (has-filled agent3) 
            (has-filled agent4) 
            (has-filled agent5) 
            (has-filled agent6) 
            (has-filled agent7) 
            (has-filled agent8)

            (= (xloc agent1) 14)
            (= (yloc agent1) 14)
            (= (xloc agent2) 13)
            (= (yloc agent2) 14)
            (= (xloc agent3) 12)
            (= (yloc agent3) 14)
            (= (xloc agent4) 11)
            (= (yloc agent4) 14)
            (= (xloc agent5) 10)
            (= (yloc agent5) 14)
            (= (xloc agent6) 9)
            (= (yloc agent6) 14)
            (= (xloc agent7) 13)
            (= (yloc agent7) 13)
            (= (xloc agent8) 13)
            (= (yloc agent8) 12)
        )
    )
)