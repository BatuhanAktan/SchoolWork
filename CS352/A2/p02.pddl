(define (problem p2-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-2-1 loc-1-2 loc-2-2 loc-3-2 loc-4-2 loc-2-3 - location
    key1 key2 key3 key4 - key
    c2122 c1222 c2232 c3242 c2223 - corridor
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-2-2)
    (arms-free key1)
    (arms-free key2)
    (arms-free key3)
    (arms-free key4)
    
    (not (at-hand))
    
    ; Locationg <> Corridor Connections
    (cor-connect loc-2-1 loc-2-2 c2122)
    (cor-connect loc-1-2 loc-2-2 c1222)
    (cor-connect loc-2-2 loc-3-2 c2232)
    (cor-connect loc-3-2 loc-4-2 c3242)
    (cor-connect loc-2-2 loc-2-3 c2223)
    
    (next-to-cor loc-2-1 c2122)
    (next-to-cor loc-1-2 c1222)
    (next-to-cor loc-2-2 c2232)
    (next-to-cor loc-3-2 c3242)
    (next-to-cor loc-2-2 c2223)
    
    (cor-connect loc-2-2 loc-2-1 c2122)
    (cor-connect loc-2-2 loc-1-2 c1222)
    (cor-connect loc-3-2 loc-2-2 c2232)
    (cor-connect loc-4-2 loc-3-2 c3242)
    (cor-connect loc-2-3 loc-2-2 c2223)
    
    (next-to-cor loc-2-2 c2122)
    (next-to-cor loc-2-2 c1222)
    (next-to-cor loc-3-2 c2232)
    (next-to-cor loc-4-2 c3242)
    (next-to-cor loc-2-3 c2223)
    
    ; Key locations
    (key-at key1 loc-2-1)
    (key-at key2 loc-1-2)
    (key-at key3 loc-2-2)
    (key-at key4 loc-2-3)
    
    ; Locked corridors
    (not (cor-unlocked c2122))
    (cor-locked c2122 purple)
    
    (not (cor-unlocked c2232))
    (cor-locked c2232 yellow)
    
    (not (cor-unlocked c1222))
    (cor-locked c1222 yellow)
    
    (not (cor-unlocked c2223))
    (cor-locked c2223 green)
    
    (not (cor-unlocked c3242))
    (cor-locked c3242 rainbow)
    
    ; Risky corridors

    ; Key colours
    (key-colour key1 green)
    (key-colour key2 rainbow)
    (key-colour key3 purple)
    (key-colour key4 yellow)
    ; Key usage properties (one use, two use, etc)
    (= (uses key1) 1)
    (= (uses key2) 1)
    (= (uses key3) 1)
    (= (uses key4) 2)
  )
  (:goal
    (hero-at loc-4-2)
  )

)
