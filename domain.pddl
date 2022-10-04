(define (domain multi_agent_lines)
    (:requirements :fluents :adl :typing)
    (:types agent tank well - object)
    (:predicates (has-water ?a - agent) (has-filled ?a - agent))
    (:functions (xloc ?o - object) (yloc ?o - object) - integer
                (walls) - bit-matrix)

    (:action collect
     :parameters (?a - agent ?w - well)
     :precondition (and (not (has-water ?a))
                        (or (and (= (xloc ?a) (xloc ?w)) (= (- (yloc ?a) 1) (yloc ?w)))
                            (and (= (xloc ?a) (xloc ?w)) (= (+ (yloc ?a) 1) (yloc ?w)))
                            (and (= (- (xloc ?a) 1) (xloc ?w)) (= (yloc ?a) (yloc ?w)))
                            (and (= (+ (xloc ?a) 1) (xloc ?w)) (= (yloc ?a) (yloc ?w)))))
     :effect (has-water ?a) 
    )

    (:action fill
     :parameters (?a - agent ?t - tank)
     :precondition (and (has-water ?a)
                        (or (and (= (xloc ?a) (xloc ?t)) (= (- (yloc ?a) 1) (yloc ?t)))
                            (and (= (xloc ?a) (xloc ?t)) (= (+ (yloc ?a) 1) (yloc ?t)))
                            (and (= (- (xloc ?a) 1) (xloc ?t)) (= (yloc ?a) (yloc ?t)))
                            (and (= (+ (xloc ?a) 1) (xloc ?t)) (= (yloc ?a) (yloc ?t)))))
     :effect (and (not (has-water ?a)) (has-filled ?a))
    )

    (:action up
     :parameters (?a - agent)
     :precondition
        (and (> (yloc ?a) 1)
            (= (get-index walls (- (yloc ?a) 1) (xloc ?a)) false)
            (not (exists (?t - tank)
                (and (= (xloc ?a) (xloc ?t)) (= (- (yloc ?a) 1) (yloc ?t)))))
            (not (exists (?w - well)
                (and (= (xloc ?a) (xloc ?w)) (= (- (yloc ?a) 1) (yloc ?w))))))
     :effect (decrease (yloc ?a) 1)
    )
    (:action down
     :parameters (?a - agent)
     :precondition
        (and (< (yloc ?a) (height walls))
            (= (get-index walls (+ (yloc ?a) 1) (xloc ?a)) false)
            (not (exists (?t - tank)
                (and (= (xloc ?a) (xloc ?t)) (= (+ (yloc ?a) 1) (yloc ?t)))))
            (not (exists (?w - well)
                (and (= (xloc ?a) (xloc ?w)) (= (+ (yloc ?a) 1) (yloc ?w))))))
     :effect (increase (yloc ?a) 1)
    )
    (:action left
     :parameters (?a - agent)
     :precondition
        (and (> (xloc ?a) 1)
            (= (get-index walls (yloc ?a) (- (xloc ?a) 1)) false)
            (not (exists (?t - tank)
                (and (= (- (xloc ?a) 1) (xloc ?t)) (= (yloc ?a) (yloc ?t)))))
            (not (exists (?w - well)
                (and (= (- (xloc ?a) 1) (xloc ?w)) (= (yloc ?a) (yloc ?w))))))
     :effect (decrease (xloc ?a) 1)
    )
    (:action right
     :parameters (?a - agent)
     :precondition
        (and (< (xloc ?a) (width walls))
            (= (get-index walls (yloc ?a) (+ (xloc ?a) 1)) false)
            (not (exists (?t - tank)
                (and (= (+ (xloc ?a) 1) (xloc ?t)) (= (yloc ?a) (yloc ?t)))))
            (not (exists (?w - well)
                (and (= (+ (xloc ?a) 1) (xloc ?w)) (= (yloc ?a) (yloc ?w))))))
     :effect (increase (xloc ?a) 1)
    )
)