(define (domain multi_agent_lines)
    (:requirements :fluents :adl :typing)
    (:types agent tank well finish - object)
    (:predicates (has-water1 ?a - agent) (has-water2 ?a - agent) (has-water3 ?a - agent) (has-filled ?a - agent) (has-completed ?a - agent))
    (:functions (xloc ?o - object) (yloc ?o - object) - integer
                (walls) - bit-matrix)

    (:action collect1
     :parameters (?a - agent ?w - well)
     :precondition (and (not (has-water1 ?a))
                        (or (and (= (xloc ?a) (xloc ?w)) (= (- (yloc ?a) 1) (yloc ?w)))
                            (and (= (xloc ?a) (xloc ?w)) (= (+ (yloc ?a) 1) (yloc ?w)))
                            (and (= (- (xloc ?a) 1) (xloc ?w)) (= (yloc ?a) (yloc ?w)))
                            (and (= (+ (xloc ?a) 1) (xloc ?w)) (= (yloc ?a) (yloc ?w)))))
     :effect (has-water1 ?a) 
    )
    (:action collect2
     :parameters (?a - agent ?w - well)
     :precondition (and (has-water1 ?a)
                        (or (and (= (xloc ?a) (xloc ?w)) (= (- (yloc ?a) 1) (yloc ?w)))
                            (and (= (xloc ?a) (xloc ?w)) (= (+ (yloc ?a) 1) (yloc ?w)))
                            (and (= (- (xloc ?a) 1) (xloc ?w)) (= (yloc ?a) (yloc ?w)))
                            (and (= (+ (xloc ?a) 1) (xloc ?w)) (= (yloc ?a) (yloc ?w)))))
     :effect (and (has-water2 ?a) (not (has-water1 ?a)))
    )
    (:action collect3
     :parameters (?a - agent ?w - well)
     :precondition (and (has-water2 ?a)
                        (or (and (= (xloc ?a) (xloc ?w)) (= (- (yloc ?a) 1) (yloc ?w)))
                            (and (= (xloc ?a) (xloc ?w)) (= (+ (yloc ?a) 1) (yloc ?w)))
                            (and (= (- (xloc ?a) 1) (xloc ?w)) (= (yloc ?a) (yloc ?w)))
                            (and (= (+ (xloc ?a) 1) (xloc ?w)) (= (yloc ?a) (yloc ?w)))))
     :effect (and (has-water3 ?a) (not (has-water2 ?a)))
    )

    (:action fill
     :parameters (?a - agent ?t - tank)
     :precondition (and (has-water3 ?a)
                        (or (and (= (xloc ?a) (xloc ?t)) (= (- (yloc ?a) 1) (yloc ?t)))
                            (and (= (xloc ?a) (xloc ?t)) (= (+ (yloc ?a) 1) (yloc ?t)))
                            (and (= (- (xloc ?a) 1) (xloc ?t)) (= (yloc ?a) (yloc ?t)))
                            (and (= (+ (xloc ?a) 1) (xloc ?t)) (= (yloc ?a) (yloc ?t)))))
     :effect (and (not (has-water3 ?a)) (has-filled ?a))
    )

    (:action up
     :parameters (?a - agent)
     :precondition
        (and 
            (> (yloc ?a) 1)
            (not (or
                (has-water1 ?a)
                (has-water2 ?a))
            )
            (= (get-index walls (- (yloc ?a) 1) (xloc ?a)) false)
            (not (exists (?t - tank)
                (and (= (xloc ?a) (xloc ?t)) (= (- (yloc ?a) 1) (yloc ?t)))))
            (not (exists (?w - well)
                (and (= (xloc ?a) (xloc ?w)) (= (- (yloc ?a) 1) (yloc ?w)))))
            (not (exists (?b - agent)
                (and (= (xloc ?a) (xloc ?b)) (= (- (yloc ?a) 1) (yloc ?b)))))
        )
     :effect (decrease (yloc ?a) 1)
    )
    (:action down
     :parameters (?a - agent)
     :precondition
        (and 
            (< (yloc ?a) (height walls))
            (not (or
                (has-water1 ?a)
                (has-water2 ?a))
            )
            (= (get-index walls (+ (yloc ?a) 1) (xloc ?a)) false)
            (not (exists (?t - tank)
                (and (= (xloc ?a) (xloc ?t)) (= (+ (yloc ?a) 1) (yloc ?t)))))
            (not (exists (?w - well)
                (and (= (xloc ?a) (xloc ?w)) (= (+ (yloc ?a) 1) (yloc ?w)))))
            (not (exists (?b - agent)
                (and (= (xloc ?a) (xloc ?b)) (= (+ (yloc ?a) 1) (yloc ?b)))))
        )
     :effect (increase (yloc ?a) 1)
    )
    (:action left
     :parameters (?a - agent)
     :precondition
        (and 
            (> (xloc ?a) 1)
            (not (or
                (has-water1 ?a)
                (has-water2 ?a))
            )
            (= (get-index walls (yloc ?a) (- (xloc ?a) 1)) false)
            (not (exists (?t - tank)
                (and (= (- (xloc ?a) 1) (xloc ?t)) (= (yloc ?a) (yloc ?t)))))
            (not (exists (?w - well)
                (and (= (- (xloc ?a) 1) (xloc ?w)) (= (yloc ?a) (yloc ?w)))))
            (not (exists (?b - agent)
                (and (= (- (xloc ?a) 1) (xloc ?b)) (= (yloc ?a) (yloc ?b)))))
        )
     :effect (decrease (xloc ?a) 1)
    )
    (:action right
     :parameters (?a - agent)
     :precondition
        (and 
            (< (xloc ?a) (width walls))
            (not (or
                (has-water1 ?a)
                (has-water2 ?a))
            )
            (= (get-index walls (yloc ?a) (+ (xloc ?a) 1)) false)
            (not (exists (?t - tank)
                (and (= (+ (xloc ?a) 1) (xloc ?t)) (= (yloc ?a) (yloc ?t)))))
            (not (exists (?w - well)
                (and (= (+ (xloc ?a) 1) (xloc ?w)) (= (yloc ?a) (yloc ?w)))))
            (not (exists (?b - agent)
                (and (= (+ (xloc ?a) 1) (xloc ?b)) (= (yloc ?a) (yloc ?b)))))
        )
     :effect (increase (xloc ?a) 1)
    )
    (:action wait
     :parameters (?a - agent)
     :precondition 
        (not 
            (or
                (has-water1 ?a)
                (has-water2 ?a)
            )
        )
     :effect (and)
    )
    (:action complete
     :parameters (?a - agent ?f - finish)
     :precondition (and (has-filled ?a) 
                        (and (= (xloc ?a) (xloc ?f)) (= (yloc ?a) (yloc ?f))))
     :effect (has-completed ?a)
    )
)