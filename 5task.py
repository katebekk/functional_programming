; Про каждое блюдо известен набор продуктов, требуемый для его изготовления, и количество каждого продукта.
; Задан список продуктов, имеющихся в наличие: какой продукт, сколько.
; Написать функции, формирующие возможное меню. Учитывать, что суммарное количество одного и того же продукта 
; в меню не может превышать имеющееся количество продукта.

(setq inStock '(("Макароны" 2)("Колбаса" 5) ("Сыр" 2) ("Тесто" 2)("Вренье" 5)("Картофель" 9)("Хлеб" 1)))
 
(setq recept '(("Пицца" (("Колбаса" 2) ("Сыр" 1) ("Тесто" 1))) ("Сосиска в тесте" (("Колбаса" 1) ("Тесто" 1))) ("Карбонара" (("Колбаса" 2) ("Сыр" 1) ("Макароны" 1)))))
 

 (defun have_products ((availinStock productOfRecipe)
(cond
    ((NULL (availinStock) T)
    ((>= (CADAR (availinStock) (findProductCost (CAAR (availinStock) productOfRecipe)) (have_products(CDR (availinStock) productOfRecipe))
    (T NIL)
)
)
 
(defun make_menu (availinStock recipes)
(cond
    ((NULL recipes) NIL)
    ((eq T (have_products (availinStock (CADAR recipes))) (cons (CAAR recipes) (make_menu (dif availinStock (CADAR recipes)) (CDR recipes))))
    (T (make_menu availinStock (CDR recipes)))
)
)

(defun findProductCost (product source)
(cond
    ((NULL source) 0)
    ((string-equal product (CAAR source)) (CADAR source))
    (T (findProductCost product (CDR source)))
)
)
(defun dif (availProduct productOfRecipe)
(cond
    ((NULL availProduct) NIL)
    (T (cons (list (CAAR availProduct) (- (CADAR availProduct) (findProductCost (CAAR availProduct) productOfRecipe))) (dif (CDR availProduct) productOfRecipe)))
)
)
(defun allMenu (products recipes)
(cond
    ((NULL recipes) NIL)
    (T (cons (make_menu products (CAR recipes)) (allMenu products (CDR recipes))))
)
)
(defun comb (recipes)
    (cond
        ((NULL (CDR recipes)) NIL)
        (T (cons (list (CAR recipes) (CADR recipes)) (comb (cons (CAR recipes) (CDDR recipes)))))
    )
)
(defun all-comb (recipes)
(cond
    ((NULL recipes) NIL)
    (T (cons (comb recipes) (all-comb (CDR recipes))))
)
)
(print(allMenu inStock recept))
