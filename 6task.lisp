;; Использовать функции высших порядков при решение следующих задач:
;; к каждому элементу списка прибавить заданное число;

;; каждый элемет списка умножить на заданное число;

;; по исходному списку сформировать список пар, где вторым элементом списка является заданное число;


(DEFUN SUM (x y) (+ x y))
(DEFUN MULL(x y) (* x y))
(DEFUN SUML (x y) (LIST x y))

(DEFUN ALLF (L x f) (COND ((NULL L) Nil)((NULL x) L) 
                        (T (CONS (funcall f (CAR L) x)(ALLF (CDR L) x f)))))

(print (ALLF '(4 1 2) 2 'SUM))
(print (ALLF '(4 1 2) 2 'MULL))
(print (ALLF '(4 1 2) 2 'SUML))
