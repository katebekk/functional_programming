; Про каждое блюдо известен набор продуктов, требуемый для его изготовления, и количество каждого продукта.
; Задан список продуктов, имеющихся в наличие: какой продукт, сколько.
; Написать функции, формирующие возможное меню. Учитывать, что суммарное количество одного и того же продукта 
; в меню не может превышать имеющееся количество продукта.

(setq prods '(("Грибы" 8) ("Сыр" 1) ("Тесто" 10) ("Макароны" 1)))

(setq dishes '(("Пицца" (("Грибы" 2) ("Сыр" 1) ("Тесто" 1))) 
("Пирог с капустой" (("Капуста" 1) ("Тесто" 1))) 
("Паста с грибами" (("Грибы" 2) ("Сыр" 1) ("Макароны" 1)))))


(defun haveProducts (inStock prod)
(cond
    ((NULL inStock) T)
    ((>= (CADAR inStock) (productCost (CAAR inStock) prod)) (haveProducts (CDR inStock) prod))
    (T NIL)
)
)
(defun productCost (prod source)
(cond
    ((NULL source) 0)
    ((string-equal prod (CAAR source)) (CADAR source))
    (T (productCost prod (CDR source)))
)
)
(defun dif (inStock prod)
(cond
    ((NULL inStock) NIL)
    (T (cons (list (CAAR inStock) (- (CADAR inStock) (productCost (CAAR inStock) prod))) (dif (CDR inStock) prod)))
)
)
(defun makeMenu (inStock recipes)
(cond
    ((NULL recipes) NIL)
    ((eq T (haveProducts inStock (CADAR recipes))) (cons (CAAR recipes) (makeMenu (dif inStock (CADAR recipes)) (CDR recipes))))
    (T (makeMenu inStock (CDR recipes)))
)
)

(print(makeMenu prods dishes)) 
