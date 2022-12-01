(require "asdf")

(defun max-depth (n)
  (if (typep n 'list)
      (+ (max (max-depth (first n)) (max-depth (second n))) 1)
      0))

(defun depth-list (n)
  (if (typep n 'list)
      (if (or (typep (first n) 'list) (typep (second n) 'list))
          (mapcar #'(lambda (x) (+ x 1))
            (concatenate 'list (depth-list (first n)) (depth-list (second n))))
          '(0))
      '(-1)))

(defun left (depth n)
  (if (< depth 1)
      n
      (if (typep n 'list)
	        (left (- depth 1) (first n))
	        nil)))

(defun right (depth n)
  (if (< depth 1)
      n
      (if (typep n 'list)
	        (right (- depth 1) (second n))
	        nil)))

(defun add-to-left (n m)
  (if (typep n 'list)
      (list
        (add-to-left (first n) m)
        (second n))
      (+ n m)))

(defun add-to-right (n m)
  (if (typep n 'list)
      (list
        (first n)
        (add-to-right (second n) m))
      (+ n m)))

(defun explode (depth n)
  (if (typep n 'list)
      (if (= depth 0)
          0
          (list
            (add-to-right (explode (- depth 1) (first n))
                          (if (and (= (first (depth-list (second n)))
																			(- (apply #'max (depth-list n)) 1))
																	 (> (apply #'max (depth-list (second n)))
																			(apply #'max (depth-list (first n)))))
                              (or (left depth (second n)) 0)
                              0))
            (add-to-left (if (<= (max-depth (first n)) (- depth 1))
                             (explode (- depth 1) (second n))
                             (second n))
                         (if (and (= (first (last (depth-list (first n))))
				 										 		 		 (- (apply #'max (depth-list n)) 1))
																	(<= (count (apply #'max (depth-list (first n)))
																						 (depth-list (first n)))
																		  1))
                             (or (right depth (first n)) 0)
                             0))))
      n))

(defun split (n)
  (if (typep n 'list)
      (list (split (first n)) (if (tree-equal (split (first n)) (first n))
																	(split (second n))
																	(second n)))
      (if (> n 9)
          (list (floor n 2) (ceiling n 2))
          n)))

(defun reduce-num (n)
  (if (tree-equal (explode 4 n) n)
      (if (tree-equal (split n) n)
          n
          (reduce-num (split n)))
      (reduce-num (explode 4 n))))

(defun listify (s)
  (read-from-string
    (substitute #\space #\, (substitute #\) #\] (substitute #\( #\[ s)))))

(defun star-add (n m)
  (reduce-num (list n m)))

(defun magnitude (n)
  (if (typep n 'list)
      (+ (* (magnitude (first n)) 3) (* (magnitude (second n)) 2))
      n))

(defun product (a b)
	(if (car a)
			(append
				(if (car b)
						(append (list (list (car a) (car b)))
										(product (list (car a)) (cdr b))))
				(product (cdr a) b))))

(defun main ()
;	(magnitude (reduce #'star-add (mapcar #'listify
;																				(uiop:read-file-lines "day18input.txt")))))
	(apply
		#'max
		(mapcar
			#'magnitude
			(mapcar #'(lambda (n) (star-add (first n) (second n)))
							(product (mapcar #'listify (uiop:read-file-lines "day18input.txt"))
											 (mapcar #'listify (uiop:read-file-lines "day18input.txt")))))))
