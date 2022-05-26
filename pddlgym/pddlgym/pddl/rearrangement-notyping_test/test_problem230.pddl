(define (problem rearrangement-notyping) 
    (:domain rearrangement-notyping)

    (:objects
    
	bear-0
	monkey-1
	bear-2
	robot
	loc-0-0
	loc-0-1
	loc-0-2
	loc-0-3
	loc-0-4
	loc-1-0
	loc-1-1
	loc-1-2
	loc-1-3
	loc-1-4
	loc-2-0
	loc-2-1
	loc-2-2
	loc-2-3
	loc-2-4
    )

    (:init
    
	(isbear bear-0)
	(ismonkey monkey-1)
	(isbear bear-2)
	(isrobot robot)
	(at bear-0 loc-0-0)
	(at monkey-1 loc-1-1)
	(at bear-2 loc-1-3)
	(at robot loc-0-3)
	(handsfree robot)

    ; action literals
    
	(pick bear-0)
	(place bear-0)
	(pick monkey-1)
	(place monkey-1)
	(pick bear-2)
	(place bear-2)
	(moveto loc-0-0)
	(moveto loc-0-1)
	(moveto loc-0-2)
	(moveto loc-0-3)
	(moveto loc-0-4)
	(moveto loc-1-0)
	(moveto loc-1-1)
	(moveto loc-1-2)
	(moveto loc-1-3)
	(moveto loc-1-4)
	(moveto loc-2-0)
	(moveto loc-2-1)
	(moveto loc-2-2)
	(moveto loc-2-3)
	(moveto loc-2-4)
    )

    (:goal (and  (holding bear-0)  (at bear-0 loc-1-3) ))
)
    