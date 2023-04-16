(define (problem p4-dungeon)
  (:domain Dungeon)

  ; Come up with your own problem instance (see assignment for details)
  ; NOTE: You _may_ use new objects for this problem only.

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-1-2 loc-2-2 loc-2-3 loc-3-2 loc-3-3 loc-4-2 loc-4-1 loc-3-1 - location
    c1222 c2223 c2232 c3233 c3242 c4241 c4131 - corridor
    key1 key2 key3 - key
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-1-2)
    (arms-free key1)
    (arms-free key2)
    (arms-free key3)
    
    (not (at-hand))
    ; Locationg <> Corridor Connections
    (cor-connect loc-1-2 loc-2-2 c1222)
    (cor-connect loc-2-2 loc-2-3 c2223)
    (cor-connect loc-2-2 loc-3-2 c2232)
    (cor-connect loc-3-2 loc-3-3 c3233)
    (cor-connect loc-3-2 loc-4-2 c3242)
    (cor-connect loc-4-2 loc-4-1 c4241)
    (cor-connect loc-4-1 loc-3-1 c4131)
    
    (next-to-cor loc-1-2 c1222)
    (next-to-cor loc-2-2 c2223)
    (next-to-cor loc-2-2 c2232)
    (next-to-cor loc-3-2 c3233)
    (next-to-cor loc-3-2 c3242)
    (next-to-cor loc-4-2 c4241)
    (next-to-cor loc-4-1 c4131)
    
    (cor-connect loc-2-2 loc-1-2 c1222)
    (cor-connect loc-2-3 loc-2-2 c2223)
    (cor-connect loc-3-2 loc-2-2 c2232)
    (cor-connect loc-3-3 loc-3-2 c3233)
    (cor-connect loc-4-2 loc-3-2 c3242)
    (cor-connect loc-4-1 loc-4-2 c4241)
    (cor-connect loc-3-1 loc-4-1 c4131)
    
    (next-to-cor loc-2-2 c1222)
    (next-to-cor loc-2-3 c2223)
    (next-to-cor loc-3-2 c2232)
    (next-to-cor loc-3-3 c3233)
    (next-to-cor loc-4-2 c3242)
    (next-to-cor loc-4-1 c4241)
    (next-to-cor loc-3-1 c4131)
    
    ; Key locations
    (key-at key1 loc-1-2)
    (key-at key2 loc-2-3)
    (key-at key3 loc-3-3)
    ; Locked corridors
    (not (cor-unlocked c2232))
    (cor-locked c2232 red)
    
    (not (cor-unlocked c3242))
    (cor-locked c3242 green)
    
    (not (cor-unlocked c4131))
    (cor-locked c4131 rainbow)
    
    (cor-unlocked c1222) 
    (cor-unlocked c2223)
    (cor-unlocked c4241)
    (cor-unlocked c3233)

    ; Risky corridors
    (cor-risky c2232)
    
    ; Key colours
    (key-colour key1 red)
    (key-colour key2 green)
    (key-colour key3 rainbow)
    ; Key usage properties (one use, two use, etc)
    (= (uses key1) 1000)
    (= (uses key2) 1)
    (= (uses key3) 1)
  )
  (:goal
    (hero-at loc-3-1)
  )

)
