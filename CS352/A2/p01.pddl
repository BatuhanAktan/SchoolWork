(define (problem p1-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-3-1 loc-1-2 loc-2-2 loc-3-2 loc-4-2 loc-2-3 loc-3-3 loc-2-4 loc-3-4 loc-4-4 - location
    key1 key2 key3 key4 - key
    c3132 c1222 c2232 c3242 c2223 c3233 c2333 c2324 c3334 c2434 c3444 - corridor
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-1-2)
    (arms-free key1)
    (arms-free key2)
    (arms-free key3)
    (arms-free key4)
    
    (not (at-hand))

    ; Locationg <> Corridor Connections
    (cor-connect loc-3-1 loc-3-2 c3132)
    (cor-connect loc-1-2 loc-2-2 c1222)
    (cor-connect loc-2-2 loc-3-2 c2232)
    (cor-connect loc-3-2 loc-4-2 c3242)
    (cor-connect loc-2-2 loc-2-3 c2223)
    (cor-connect loc-3-2 loc-3-3 c3233)
    (cor-connect loc-2-3 loc-3-3 c2333)
    (cor-connect loc-2-3 loc-2-4 c2324)
    (cor-connect loc-3-3 loc-3-4 c3334)
    (cor-connect loc-2-4 loc-3-4 c2434)
    (cor-connect loc-3-4 loc-4-4 c3444)

    (next-to-cor loc-3-1 c3132)
    (next-to-cor loc-1-2 c1222)
    (next-to-cor loc-2-2 c2232)
    (next-to-cor loc-3-2 c3242)
    (next-to-cor loc-2-2 c2223)
    (next-to-cor loc-3-2 c3233)
    (next-to-cor loc-2-3 c2333)
    (next-to-cor loc-2-3 c2324)
    (next-to-cor loc-3-3 c3334)
    (next-to-cor loc-2-4 c2434)
    (next-to-cor loc-3-4 c3444)
    
    
    (cor-connect loc-3-2 loc-3-1 c3132)
    (cor-connect loc-2-2 loc-1-2 c1222)
    (cor-connect loc-3-2 loc-2-2 c2232)
    (cor-connect loc-4-2 loc-3-2 c3242)
    (cor-connect loc-2-3 loc-2-2 c2223)
    (cor-connect loc-3-3 loc-3-2 c3233)
    (cor-connect loc-3-3 loc-2-3 c2333)
    (cor-connect loc-2-4 loc-2-3 c2324)
    (cor-connect loc-3-4 loc-3-3 c3334)
    (cor-connect loc-3-4 loc-2-4 c2434)
    (cor-connect loc-4-4 loc-3-4 c3444)
    
    (next-to-cor loc-3-2 c3132)
    (next-to-cor loc-2-2 c1222)
    (next-to-cor loc-3-2 c2232)
    (next-to-cor loc-4-2 c3242)
    (next-to-cor loc-2-3 c2223)
    (next-to-cor loc-3-3 c3233)
    (next-to-cor loc-3-3 c2333)
    (next-to-cor loc-2-4 c2324)
    (next-to-cor loc-3-4 c3334)
    (next-to-cor loc-3-4 c2434)
    (next-to-cor loc-4-4 c3444)
    
    ; Key locations
    (key-at key1 loc-2-2)
    (key-at key2 loc-2-4)
    (key-at key3 loc-4-2)
    (key-at key4 loc-4-4)
    
    ; Locked corridors
    (not (cor-unlocked c2324))
    (cor-locked c2324 red)
    
    (not (cor-unlocked c2434))
    (cor-locked c2434 red)
    
    (not (cor-unlocked c3444))
    (cor-locked c3444 yellow)
    
    (not (cor-unlocked c3242))
    (cor-locked c3242 purple)
    
    (not (cor-unlocked c3132))
    (cor-locked c3132 rainbow)
    
    (cor-unlocked c1222) 
    (cor-unlocked c2232)
    (cor-unlocked c2223)
    (cor-unlocked c3233)
    (cor-unlocked c2333) 
    (cor-unlocked c3334)
    
    ; Risky corridors
    (cor-risky c2324)
    (cor-risky c2434)
    
    ; Key colours
    (key-colour key1 red)
    (key-colour key2 yellow)
    (key-colour key3 rainbow)
    (key-colour key4 purple)

    ; Key usage properties (one use, two use, etc)
    (= (uses key1) 1000)
    (= (uses key2) 2)
    (= (uses key3) 1)
    (= (uses key4) 1)

  )
  (:goal
      (hero-at loc-3-1)
  )

)
