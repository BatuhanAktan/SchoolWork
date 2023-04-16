(define (problem p3-dungeon)
  (:domain Dungeon)

  ; Naming convention:
  ; - loc-{i}-{j} refers to the location at the i'th column and j'th row (starting in top left corner)
  ; - c{i}{j}{h}{k} refers to the corridor connecting loc-{i}-{j} and loc-{h}-{k}
  (:objects
    loc-3-4 loc-4-5 loc-1-2 loc-2-2 loc-3-2 loc-3-3 loc-2-5 loc-1-3 loc-2-1 loc-1-4 loc-3-5 loc-2-4 loc-4-4 loc-2-3 loc-4-3 - location
    c2122 c1222 c2232 c1213 c1223 c2223 c3223 c3233 c1323 c2333 c1314 c2314 c2324 c2334 c3334 c1424 c2434 c2425 c2535 c3545 c4544 c4443 - corridor
    key1 key2 key3 key4 key5 key6 - key
  )

  (:init

    ; Hero location and carrying status
    (hero-at loc-2-1)
    (arms-free key1)
    (arms-free key2)
    (arms-free key3)
    (arms-free key4)
    
    (not (at-hand))
    
    ; Locationg <> Corridor Connections
    (cor-connect loc-2-1 loc-2-2 c2122)
    (cor-connect loc-1-2 loc-2-2 c1222)
    (cor-connect loc-2-2 loc-3-2 c2232)
    (cor-connect loc-1-2 loc-1-3 c1213)
    (cor-connect loc-1-2 loc-2-3 c1223)
    (cor-connect loc-2-2 loc-2-3 c2223)
    (cor-connect loc-3-2 loc-2-3 c3223)
    (cor-connect loc-3-2 loc-3-3 c3233)
    (cor-connect loc-1-3 loc-2-3 c1323)
    (cor-connect loc-2-3 loc-3-3 c2333)
    (cor-connect loc-1-3 loc-1-4 c1314)
    (cor-connect loc-2-3 loc-1-4 c2314)
    (cor-connect loc-2-3 loc-2-4 c2324)
    (cor-connect loc-2-3 loc-3-4 c2334)
    (cor-connect loc-3-3 loc-3-4 c3334)
    (cor-connect loc-1-4 loc-2-4 c1424)
    (cor-connect loc-2-4 loc-3-4 c2434)
    (cor-connect loc-2-4 loc-2-5 c2425)
    (cor-connect loc-2-5 loc-3-5 c2535)
    (cor-connect loc-3-5 loc-4-5 c3545)
    (cor-connect loc-4-5 loc-4-4 c4544)
    (cor-connect loc-4-4 loc-4-3 c4443)
    
    (next-to-cor loc-2-1 c2122)
    (next-to-cor loc-1-2 c1222)
    (next-to-cor loc-2-2 c2232)
    (next-to-cor loc-1-2 c1213)
    (next-to-cor loc-1-2 c1223)
    (next-to-cor loc-2-2 c2223)
    (next-to-cor loc-3-2 c3223)
    (next-to-cor loc-3-2 c3233)
    (next-to-cor loc-1-3 c1323)
    (next-to-cor loc-2-3 c2333)
    (next-to-cor loc-1-3 c1314)
    (next-to-cor loc-2-3 c2314)
    (next-to-cor loc-2-3 c2324)
    (next-to-cor loc-2-3 c2334)
    (next-to-cor loc-3-3 c3334)
    (next-to-cor loc-1-4 c1424)
    (next-to-cor loc-2-4 c2434)
    (next-to-cor loc-2-4 c2425)
    (next-to-cor loc-2-5 c2535)
    (next-to-cor loc-3-5 c3545)
    (next-to-cor loc-4-5 c4544)
    (next-to-cor loc-4-4 c4443)
    
    
    (cor-connect loc-2-2 loc-2-1 c2122)
    (cor-connect loc-2-2 loc-1-2 c1222)
    (cor-connect loc-3-2 loc-2-2 c2232)
    (cor-connect loc-1-3 loc-1-2 c1213)
    (cor-connect loc-2-3 loc-1-2 c1223)
    (cor-connect loc-2-3 loc-2-2 c2223)
    (cor-connect loc-2-3 loc-3-2 c3223)
    (cor-connect loc-3-3 loc-3-2 c3233)
    (cor-connect loc-2-3 loc-1-3 c1323)
    (cor-connect loc-3-3 loc-2-3 c2333)
    (cor-connect loc-1-4 loc-1-3 c1314)
    (cor-connect loc-1-4 loc-2-3 c2314)
    (cor-connect loc-2-4 loc-2-3 c2324)
    (cor-connect loc-3-4 loc-2-3 c2334)
    (cor-connect loc-3-4 loc-3-3 c3334)
    (cor-connect loc-2-4 loc-1-4 c1424)
    (cor-connect loc-3-4 loc-2-4 c2434)
    (cor-connect loc-2-5 loc-2-4 c2425)
    (cor-connect loc-3-5 loc-2-5 c2535)
    (cor-connect loc-4-5 loc-3-5 c3545)
    (cor-connect loc-4-4 loc-4-5 c4544)
    (cor-connect loc-4-3 loc-4-4 c4443)

    (next-to-cor loc-2-2 c2122)
    (next-to-cor loc-2-2 c1222)
    (next-to-cor loc-3-2 c2232)
    (next-to-cor loc-1-3 c1213)
    (next-to-cor loc-2-3 c1223)
    (next-to-cor loc-2-3 c2223)
    (next-to-cor loc-2-3 c3223)
    (next-to-cor loc-3-3 c3233)
    (next-to-cor loc-2-3 c1323)
    (next-to-cor loc-3-3 c2333)
    (next-to-cor loc-1-4 c1314)
    (next-to-cor loc-1-4 c2314)
    (next-to-cor loc-2-4 c2324)
    (next-to-cor loc-3-4 c2334)
    (next-to-cor loc-3-4 c3334)
    (next-to-cor loc-2-4 c1424)
    (next-to-cor loc-3-4 c2434)
    (next-to-cor loc-2-5 c2425)
    (next-to-cor loc-3-5 c2535)
    (next-to-cor loc-4-5 c3545)
    (next-to-cor loc-4-4 c4544)
    (next-to-cor loc-4-3 c4443)
    
    ; Key locations
    (key-at key1 loc-2-1)
    (key-at key2 loc-2-3)
    (key-at key3 loc-2-3)
    (key-at key4 loc-2-3)
    (key-at key5 loc-2-3)
    (key-at key6 loc-4-4)
    
    ; Locked corridors
    (not (cor-unlocked c1223))
    (cor-locked c1223 red)
    
    (not (cor-unlocked c2223))
    (cor-locked c2223 red)
    
    (not (cor-unlocked c3223))
    (cor-locked c3223 red)
    
    (not (cor-unlocked c1323))
    (cor-locked c1323 red)
    
    (not (cor-unlocked c2333))
    (cor-locked c2333 red)
    
    (not (cor-unlocked c2314))
    (cor-locked c2314 red)
    
    (not (cor-unlocked c2324))
    (cor-locked c2324 red)
    
    (not (cor-unlocked c2334))
    (cor-locked c2334 red)
    
    (not (cor-unlocked c2425))
    (cor-locked c2425 purple)
    
    (not (cor-unlocked c2535))
    (cor-locked c2535 green)
    
    (not (cor-unlocked c3545))
    (cor-locked c3545 purple)
    
    (not (cor-unlocked c4544))
    (cor-locked c4544 green)
    
    (not (cor-unlocked c4443))
    (cor-locked c4443 rainbow)
    
    (cor-unlocked c1222)
    (cor-unlocked c2122)
    (cor-unlocked c2232) 
    (cor-unlocked c1213)
    (cor-unlocked c3233)
    (cor-unlocked c1314) 
    (cor-unlocked c2324) 
    (cor-unlocked c3334) 
    (cor-unlocked c1424) 
    (cor-unlocked c2434) 
    
    ; Risky corridors
    (cor-risky c2122)
    (cor-risky c2223)
    (cor-risky c3223)
    (cor-risky c1323)
    (cor-risky c2333)
    (cor-risky c2314)
    (cor-risky c2324)
    (cor-risky c2334)
    
    ; Key colours
    (key-colour key1 red)
    (key-colour key2 green)
    (key-colour key3 green)
    (key-colour key4 purple)
    (key-colour key5 purple)
    (key-colour key6 rainbow)
    
    ; Key usage properties (one use, two use, etc)
    (= (uses key1) 1000)
    (= (uses key2) 1)
    (= (uses key3) 1)
    (= (uses key4) 1)
    (= (uses key5) 1)
    (= (uses key6) 1)
  )
  (:goal
    (hero-at loc-4-3)
  )

)
