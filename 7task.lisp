; 1
(DEFUN LISTOFLISTS (L) (COND ((NULL L) Nil)
                        ((ATOM (CAR L)) (LISTOFLISTS (CDR L)))
                        (T (CONS (CAR L) (LISTOFLISTS (CDR L)) ))))
; 2 
(DEFUN SUMIN (L x)
      (COND 
      ((NULL L) 0)
      ((eq x (CAR L)) (+ 1 (SUMIN (CDR L) x)))
      (T (+ 0 (SUMIN (CDR L) x)))))
            
(defun del(L x)
        (COND 
        ((NULL L) nil)
        ((NOT (eq x (CAR L)))(cons (CAR L) (del (CDR L) x) )  )
        (T (del (CDR L) x))))
(defun in (L)
        (cond
        ((NULL L) nil)
        (T (cons (list (CAR L) (SUMIN L (CAR L)))(in (del (CDR L) (CAR L)))))))


                        
; 3
(defun diff(L)
    (cond
    ((NULL L) nil)
    ((NULL (CDR L)) nil)
    ((> (CAR L)(CADR L)) (cons (- (CAR L)(CADR L))(diff (CDR L))) )
    ((< (CAR L)(CADR L)) (cons (- (CADR L)(CAR L))(diff (CDR L))) )
    (T (cons (- (CAR L)(CADR L))(diff (CDR L))) )))

; 4
(defun sum(L)
    (cond
    ((NULL L) nil)
    ((NULL (CDR L)) nil)
    (T (cons (+ (CAR L)(CADR L))(sum (CDR L))) )))



(print (in '(1 2 1 14 2 14 14 14)))
(print '(1 3 3 4 5 1 2 7 2))
(print (diff '(1 3 3 4 5 1 2 7 2)))
(print (sum '(1 3 3 4 5 1 2 7 2)))

