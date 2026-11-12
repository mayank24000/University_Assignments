
;; Experiment 18: Sequence Transformations
;; Demonstrating map, filter, reduce, take, drop and threading macros

(println "===== CLOJURE SEQUENCE TRANSFORMATIONS =====")

;; First Collection
(def numbers [1 2 3 4 5 6 7 8 9 10])

(println "\n========== COLLECTION 1 ==========")
(println "Original Collection:" numbers)

;; 1. MAP - Square each element
(println "\n1. MAP - Square each element")
(println "Result:" (map #(* % %) numbers))

;; 2. FILTER - Select even numbers
(println "\n2. FILTER - Select even numbers")
(println "Result:" (filter even? numbers))

;; 3. REDUCE - Calculate sum
(println "\n3. REDUCE - Calculate sum")
(println "Sum:" (reduce + numbers))

;; 4. TAKE and DROP - Slice sequence
(println "\n4. TAKE and DROP")
(println "First 5 elements:" (take 5 numbers))
(println "After dropping 5 elements:" (drop 5 numbers))

;; 5. THREADING MACRO ->>
(println "\n5. THREADING MACRO ->>")
(println "Square even numbers:"
         (->> numbers
              (filter even?)
              (map #(* % %))))

;; Second Collection
(def numbers2 [12 15 18 21 24 27 30])

(println "\n========== COLLECTION 2 ==========")
(println "Original Collection:" numbers2)

;; MAP
(println "\n1. MAP - Square each element")
(println "Result:" (map #(* % %) numbers2))

;; FILTER
(println "\n2. FILTER - Select odd numbers")
(println "Result:" (filter odd? numbers2))

;; REDUCE
(println "\n3. REDUCE - Calculate maximum")
(println "Maximum:" (reduce max numbers2))

;; TAKE and DROP
(println "\n4. TAKE and DROP")
(println "First 3 elements:" (take 3 numbers2))
(println "After dropping 3 elements:" (drop 3 numbers2))

;; THREADING MACRO ->>
(println "\n5. THREADING MACRO ->>")
(println "Double odd numbers:"
         (->> numbers2
              (filter odd?)
              (map #(* % 2))
              (take 3)))

(println "\n===== PROGRAM EXECUTED SUCCESSFULLY =====")
