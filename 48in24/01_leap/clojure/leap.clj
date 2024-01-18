(ns leap)

(defn leap-year? [year]
  (cond (== (mod year 4) 0)
        (cond (== (mod year 100) 0)
              (== (mod year 400) 0)
              :else true)
        :else false))
