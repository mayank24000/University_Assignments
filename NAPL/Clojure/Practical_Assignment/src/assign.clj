(ns assign
  (:require [next.jdbc :as jdbc]
            [ring.adapter.jetty :as jetty]))

;; Student records
(def students
  [{:name "Aarav" :marks 85 :city "Mumbai"}
   {:name "Hemraj" :marks 99 :city "Delhi"}
   {:name "Ishaan" :marks 67 :city "Bengaluru"}
   {:name "Ananya" :marks 30 :city "Chennai"}
   {:name "Kabir" :marks 91 :city "Hyderabad"}
   {:name "Meera" :marks 55 :city "Pune"}
   {:name "Arjun" :marks 73 :city "Jaipur"}
   {:name "Priya" :marks 20 :city "Kolkata"}])

(def db-spec
  {:dbtype "h2" :dbname "./students"})

;; Get students with marks above 50
(defn process-students [data]
  (filter (fn [s] (> (:marks s) 50)) data))

;; Add the table and save the students
(defn save-results [rows]
  (try
    (jdbc/execute! db-spec ["CREATE TABLE IF NOT EXISTS students (name VARCHAR(50), marks INT, city VARCHAR(50))"])
    (reduce (fn [total s]
              (jdbc/execute! db-spec
                ["INSERT INTO students (name, marks, city) VALUES (?, ?, ?)"
                 (:name s) (:marks s) (:city s)])
              (+ total (:marks s)))
            0 rows)
    (catch Exception e
      (println "Database error:" (.getMessage e)))))

(defn read-results []
  (try
    (jdbc/execute! db-spec ["SELECT name, marks, city FROM students"])
    (catch Exception e
      (println "Database error:" (.getMessage e)))))

;; Average marks
(defn average [rows]
  (let [total (reduce (fn [sum s] (+ sum (:marks s))) 0 rows)
        number (count rows)]
    (if (= number 0) 0 (Math/round (double (/ total number))))))

(defn handle-request [request]
  (let [path (:uri request)]
    (cond
      (= path "/") {:status 200 :headers {"Content-Type" "text/plain"}
                    :body "Student results. Open /results to see them."}
      (= path "/results")
      (let [rows (process-students students)
            total (save-results rows)
            saved (read-results)]
        {:status 200 :headers {"Content-Type" "text/plain"}
         :body (str "Students above 50: " (count rows)
                    "\nTotal marks: " total
                    "\nAverage marks: " (average rows)
                    "\nSaved rows: " saved)})
      :else {:status 404 :body "Not found"})))

(defn -main []
  (println "Starting server at http://localhost:3000")
  (jetty/run-jetty handle-request {:port 3000 :join? true}))

