; В игре участвуют два игрока. Множество карт игрока представлено списком.
; Элемент списка имеет следующую структуру: название масти, название карты. 
; Также задан второй список, в котором каждой карте колоды сопоставляется «стоимость» - некоторое число. 
; Написать функцию, которая по всем картам заданной масти определяет, у кого из игроков стоимость карт этой масти максимальная.
; Написать функцию, которая определяет, какие карты остались в колоде.

(setq cards '((1 "Six") (2 "Six") (3 "Six") (4 "Six") (1 "Seven") (2 "Seven") (3 "Seven") (4 "Seven") (1 "Eight") (2 "Eight") (3 "Eight") (4 "Eight") (1 "Nine") (2 "Nine") (3 "Nine") (4 "Nine") (1 "Ten") (2 "Ten") (3 "Ten") (4 "Ten") (1 "B") (2 "B") (3 "B") (4 "B") (1 "Q") (2 "Q") (3 "Q") (4 "Q") (1 "K") (2 "K") (3 "K") (4 "K") (1 "A") (2 "A") (3 "A") (4 "A")))
(setq point '(("Six" 6) ("Seven" 7) ("Eight" 8) ("Nine" 9) ("Ten" 10) ("B" 11) ("Q" 12) ("K" 13) ("A" 14)))
(setq pl1 '((1 "Ten") (2 "Six") (3 "K") (1 "B") (4 "B") (4 "Nine")))
(setq pl2 '((2 "Eight") (4 "A") (1 "Seven") (4 "Six")))

(defun get_num (player num)
(cond
    ((NULL player) NIL)
    ((eq num (CAAR player)) (cons (CAR player) (get_num (CDR player) num)))
    (T (get_num (CDR player) num))
)
)
(defun get_point (pCart point)
(cond
    ((string-equal pCart (CAAR point)) (CADAR point))
    (T (get_point pCart (CDR point)))
)
)

(defun score (player)
(cond 
    ((NULL player) 0)
    (T (+ (get_point (CADAR player) point) (score (CDR player))))
)
)
(defun winner (p1 p2 num)
(cond
    ((> (score (get_num p1 num)) (score (get_num p2 num))) (list "Won player 1" (score (get_num p1 num))))
    ((> (score (get_num p2 num)) (score (get_num p1 num))) (list "Won player 2" (score (get_num p2 num))))
    (T (list "None win" (score (get_num p1 num))))
)
)
 
(print(winner pl1 pl2 4))

(defun on_hand(cart on)
(cond
    ((NULL on) NIL)
    ((equal cart (CAR on)) T)
    (T (on_hand cart (CDR on)))
)
)

(defun stayed (cart on)
(cond
    ((NULL cart) NIL)
    ((eq NIL (on_hand (CAR cart) on)) (cons (CAR cart) (stayed (CDR cart) on)))
    (T (stayed (CDR cart) on))
)
)

(print(winner pl1 pl2 1))
(print(winner pl1 pl2 2))

(print(winner pl1 pl2 3))
(print(stayed cards (append pl1 pl2)))

