(println "===== CLOJURE IMMUTABLE DATA STRUCTURES =====")

;; 1. LIST
(println "\n1. LIST OPERATIONS")

(def original-list '(10 20 30 40))

(println "Original List:" original-list)
(println "First Element:" (first original-list))
(println "Rest of List:" (rest original-list))

(def new-list (conj original-list 5))

(println "After conj:" new-list)
(println "Original List (Unchanged):" original-list)

;; 2. VECTOR
(println "\n2. VECTOR OPERATIONS")

(def original-vector [10 20 30 40])

(println "Original Vector:" original-vector)
(println "Element at Index 2:" (get original-vector 2))
(println "Vector Count:" (count original-vector))

(def new-vector (conj original-vector 50))

(println "After conj:" new-vector)
(println "Original Vector (Unchanged):" original-vector)

;; 3. MAP
(println "\n3. MAP OPERATIONS")

(def original-map {:name "Mayank" :age 21 :course "Cybersecurity"})

(println "Original Map:" original-map)
(println "Get Name:" (get original-map :name))

(def updated-map (assoc original-map :age 22))
(println "After assoc:" updated-map)

(def new-map (dissoc updated-map :course))
(println "After dissoc:" new-map)

(println "Original Map (Unchanged):" original-map)

;; 4. SET
(println "\n4. SET OPERATIONS")

(def original-set #{10 20 30 40})

(println "Original Set:" original-set)
(println "Contains 20:" (contains? original-set 20))

(def updated-set (conj original-set 50))
(println "After conj:" updated-set)

(def new-set (disj updated-set 30))
(println "After disj:" new-set)

(println "Original Set (Unchanged):" original-set)

;; END
(println "\n===== PROGRAM EXECUTED SUCCESSFULLY =====")
