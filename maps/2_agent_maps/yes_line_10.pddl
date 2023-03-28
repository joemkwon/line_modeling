(define (problem yes-line-10)
    (:domain multi_agent_lines)
    (:objects tank1 tank2 tank3 tank4 tank5 tank6 - tank well1 well2 well3 well4 well5 well6 well7 well8 well9 well10 - well agent1 agent2 - agent)
    (:init  
        (= (walls)
            (transpose (bit-mat
                (bit-vec 0 0 0 1 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 1 1 1 1 0 0 1 1 1 1 1)
                (bit-vec 0 0 0 0 0 0 1 1 0 1 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 1 0 0 1 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 1 0 0 1 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 1 0 0 1 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 1 0 0 1 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 1 0 0 1 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
                (bit-vec 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
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

        (= (xloc well1) 5)
        (= (yloc well1) 1)
        (= (xloc well2) 6)
        (= (yloc well2) 1)
        (= (xloc well3) 7)
        (= (yloc well3) 1)
        (= (xloc well4) 8)
        (= (yloc well4) 1)
        (= (xloc well5) 9)
        (= (yloc well5) 1)
        (= (xloc well6) 10)
        (= (yloc well6) 1)
        (= (xloc well7) 11)
        (= (yloc well7) 1)
        (= (xloc well8) 12)
        (= (yloc well8) 1)
        (= (xloc well9) 13)
        (= (yloc well9) 1)
        (= (xloc well10) 14)
        (= (yloc well10) 1)

        (= (xloc agent1) 9)
        (= (yloc agent1) 5)
        (not (has-water agent1))
        (not (has-filled agent1))
        
        (= (xloc agent2) 9)
        (= (yloc agent2) 6)
        (not (has-water agent2))
        (not (has-filled agent2)))
        
    (:goal (and (has-filled agent1) (has-filled agent2)))
)