(define (problem yes-line-x)
    (:domain multi_agent_lines)
    (:objects tank1 tank2 tank3 tank4 tank5 tank6 - tank well1 well2 well3 well4 well5 well6 well7 well8 well9 well10 well11 well12 - well agent1 agent2 agent3 agent4 agent5 agent6 agent7 agent8 - agent)
    (:init  
        (= (walls)
            (transpose (bit-mat
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 1 1 1 1 1 1 1)
                (bit-vec 0 0 0 0 0 0 0 1 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 1 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 1 0 0 1 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 1 0 0 1 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 1 0 0 1 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 1 0 0 1 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 1 0 0 1 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 1 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 1 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 1 0 0 0 0 0 0))))

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

        (= (xloc well1) 3)
        (= (yloc well1) 4)
        (= (xloc well2) 4)
        (= (yloc well2) 4)
        (= (xloc well3) 5)
        (= (yloc well3) 4)
        (= (xloc well4) 6)
        (= (yloc well4) 4)
        (= (xloc well5) 7)
        (= (yloc well5) 4)

        (= (xloc well6) 7)
        (= (yloc well6) 7)
        (= (xloc well7) 7)
        (= (yloc well7) 8)
        (= (xloc well8) 6)
        (= (yloc well8) 8)
        (= (xloc well9) 6)
        (= (yloc well9) 9)
        (= (xloc well10) 5)
        (= (yloc well10) 10)
        (= (xloc well11) 4)
        (= (yloc well11) 11)
        (= (xloc well12) 4)
        (= (yloc well12) 12)

        (= (xloc agent1) 13)
        (= (yloc agent1) 7)
        (not (has-water agent1))
        (not (has-filled agent1))
        
        (= (xloc agent2) 13)
        (= (yloc agent2) 8)
        (not (has-water agent2))
        (not (has-filled agent2))

        (= (xloc agent3) 13)
        (= (yloc agent3) 9)
        (not (has-water agent3))
        (not (has-filled agent3))

        (= (xloc agent4) 13)
        (= (yloc agent4) 10)
        (not (has-water agent4))
        (not (has-filled agent4))

        (= (xloc agent5) 13)
        (= (yloc agent5) 11)
        (not (has-water agent5))
        (not (has-filled agent5))

        (= (xloc agent6) 13)
        (= (yloc agent6) 12)
        (not (has-water agent6))
        (not (has-filled agent6))

        (= (xloc agent7) 13)
        (= (yloc agent7) 13)
        (not (has-water agent7))
        (not (has-filled agent7))

        (= (xloc agent8) 13)
        (= (yloc agent8) 14)
        (not (has-water agent8))
        (not (has-filled agent8)))
        
    (:goal (and (has-filled agent1) (has-filled agent2) (has-filled agent3) (has-filled agent4) (has-filled agent5) (has-filled agent6) (has-filled agent7) (has-filled agent8)))
)