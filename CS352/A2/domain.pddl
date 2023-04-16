(define (domain Dungeon)

    (:requirements
        :typing
        :negative-preconditions
        :conditional-effects
    )

    ; Do not modify the types
    (:types
        location colour key corridor
    )

    ; Do not modify the constants
    (:constants
        red yellow green purple rainbow - colour
    )

    ; You may introduce whatever predicates you would like to use
    (:predicates

        ; One predicate given for free!
        (hero-at ?loc - location)
        (arms-free ?k)
        
        (cor-connect ?from ?to - location ?cor - corridor)
        (cor-unlocked ?cor - corridor)
        (cor-collapsed ?cor - corridor)
        (cor-risky ?cor - corridor)
        (cor-locked ?cor - corridor ?col - colour)
        (loc-messy ?loc - location)
        (next-to-cor ?from - location ?cor - corridor)
        
        (key-at ?k - key ?loc - location)
        (key-usable ?k - key)
        (key-colour ?k - key ?col - colour)
        
        (at-hand)

    )
    
    (:functions
        (uses ?k - key) - number
    )

    ; IMPORTANT: You should not change/add/remove the action names or parameters

    ;Hero can move if the
    ;    - hero is at current location ?from,
    ;    - hero will move to location ?to,
    ;    - corridor ?cor exists between the ?from and ?to locations
    ;    - there isn't a locked door in corridor ?cor
    ;Effects move the hero, and collapse the corridor if it's "risky" (also causing a mess in the ?to location)
    (:action move

        :parameters (?from ?to - location ?cor - corridor)

        :precondition (and  (hero-at ?from) (cor-connect ?from ?to ?cor) 
                        (cor-unlocked ?cor) (not (cor-collapsed ?cor))


        )

        :effect (and (hero-at ?to) (not (hero-at ?from))
        
            (when (cor-risky ?cor) 
            
               (and (cor-collapsed ?cor) (loc-messy ?to)
               )
            
            )
        )
    )

    ;Hero can pick up a key if the
    ;    - hero is at current location ?loc,
    ;    - there is a key ?k at location ?loc,
    ;    - the hero's arm is free,
    ;    - the location is not messy
    ;Effect will have the hero holding the key and their arm no longer being free
    (:action pick-up

        :parameters (?loc - location ?k - key)

        :precondition (and (hero-at ?loc) (key-at ?k ?loc) 
                        (arms-free ?k ) (not (at-hand)) (not (loc-messy ?loc))
                    )

        :effect (and (not (arms-free ?k)) (at-hand) 
        )
    )

    ;Hero can drop a key if the
    ;    - hero is holding a key ?k,
    ;    - the hero is at location ?loc
    ;Effect will be that the hero is no longer holding the key
    (:action drop

        :parameters (?loc - location ?k - key)

        :precondition (and (not (arms-free ?k)) (at-hand) (hero-at ?loc)

        )

        :effect (and (arms-free ?k) (key-at ?k ?loc) (not (at-hand))
        
        )
    )


    ;Hero can use a key for a corridor if
    ;    - the hero is holding a key ?k,
    ;    - the key still has some uses left,
    ;    - the corridor ?cor is locked with colour ?col,
    ;    - the key ?k is if the right colour ?col,
    ;    - the hero is at location ?loc
    ;    - the corridor is connected to the location ?loc
    ;Effect will be that the corridor is unlocked and the key usage will be updated if necessary
    (:action unlock

        :parameters (?loc - location ?cor - corridor ?col - colour ?k - key)

        :precondition (and (not (arms-free ?k)) (at-hand) (> (uses ?k) 0) (cor-locked ?cor ?col)
            (key-colour ?k ?col) (hero-at ?loc) (next-to-cor ?loc ?cor)

        )

        :effect (and (cor-unlocked ?cor) (not (cor-locked ?cor ?col)) 
        (decrease (uses ?k) 1)
        )
    )

    ;Hero can clean a location if
    ;    - the hero is at location ?loc,
    ;    - the location is messy
    ;Effect will be that the location is no longer messy
    (:action clean

        :parameters (?loc - location)

        :precondition (and (hero-at ?loc) (loc-messy ?loc)

        )

        :effect (and (not (loc-messy ?loc)) (hero-at ?loc)

        )
    )

)
