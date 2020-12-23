

(setq students '(("Михалков" (("История" 4 "ex") ("География" 3 "reex"))) ("Ржепко" (("История" 4 "reex") ("География" 5 "ex"))) ("Маслов" (("История" 2 "reex") ("История" 3 "reex"))) ("Беккерман" (("История" 5 "ex") ("География" 4 "ex")))))

(defun countOfReex (studentMark subj)
(cond
    ((NULL studentMark) 0)
    ((and (string-equal subj (CAAR studentMark)) (string-equal "reex" (CADDAR studentMark))) (+ 1 (countOfReex (CDR studentMark) subj)))
    (T (countOfReex (CDR studentMark) subj))
)
)
(defun formatStudents (studentsInfo subj)
(cond
    ((NULL studentsInfo) NIL)
    (T (cons (list (CAAR studentsInfo) (countOfReex (CADAR studentsInfo) subj)) (formatStudents (CDR studentsInfo) subj)))
)    
)
(defun findMax (studentsInfo)
(cond
    ((NULL (CDR studentsInfo)) (CAR studentsInfo))
    ((> (CADAR studentsInfo) (CADADR studentsInfo)) (findMax (cons (CAR studentsInfo) (CDDR studentsInfo))))
    (T (findMax (CDR studentsInfo)))
)
)
(defun delMaxFromList (max studentsInfo)
(cond
    ((NULL studentsInfo) NIL)
    ((eq max (CAR studentsInfo)) (delMaxFromList max (CDR studentsInfo)))
    (T (cons (CAR studentsInfo) (delMaxFromList max (CDR studentsInfo))))
)
)
(defun sortStudents (studentsInfo)
(cond
    ((NULL studentsInfo) NIL)
    (T (cons (findMax studentsInfo) (sortStudents (delMaxFromList (findMax studentsInfo) studentsInfo))))
)
)
(print(sortStudents(formatStudents students "История")))