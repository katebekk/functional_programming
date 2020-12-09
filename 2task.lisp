;; Написать функцию, которая по списку вида:
;; фамилия

;; улица

;; номер дома

(setq tenants 
'((Кошкин Сенная 9)(Павлов Бумагина 60)(Орлов Сенная 12)(Тамарова Камарова 4)(Бубнов Камарова 20)(Шерохов Бумагина 2)(Путин Сенная 9)(Путин Сенная 1) (Кошкин Сенная 8) ))


(defun SameStreet (L street)
    (cond
        ((NULL L) NIL)
        ((eq street (CADAR L)) (cons (CAR L) (SameStreet (CDR L) street)))
        (T (SameStreet (CDR L) street) )))
(defun findSameName (name L)
    (cond 
     ((NULL L) NIL)
     ((eq name (CAAR L)) (cons (CAR L) (findSameName name (CDR L) )))
        (T (findSameName name (CDR L)) )))

                         
(defun haveName (L name)
    (cond
    ((NULL L) NIL)
    ((eq name (CAAR L)) T)
    (T (haveName (CDR L) name))))

(defun SameName (L)
    (cond 
     ((NULL L) NIL)
     ((eq T (haveName (CDR L) (CAAR L)))(cons (findSamename (CAAR L) L)(SameName (CDR L)) ))
     (T (SameName (CDR L)))))


; (print (findSameName 'Путин (SameStreet tenants 'Сенная)))
(print (SameName (SameStreet tenants 'Сенная)))
; (print (LENLIST tenants))

