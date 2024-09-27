(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

(define (zip pairs)
    (cond ((equal? pairs nil) (cons nil (cons nil nil)))
        (else 
            (cons (cons (caar pairs) (car(zip (cdr pairs))))
                  (cons (cons (car (cdar pairs)) (cadr(zip (cdr pairs)))) nil)      
            )
        ) 
    )

)
;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
    (define (para s t)
        (if (equal? s nil) nil (cons (cons t (cons (car s) nil)) (para (cdr s) (+ t 1)))
    
  ))(para s 0))
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (cond ((equal? list1 nil) list2)
        ((equal? list2 nil) list1)
        ((comp (car list1) (car list2)) (cons (car list1) (merge comp (cdr list1) list2)))
        ((comp (car list2) (car list1)) (cons (car list2) (merge comp list1 (cdr list2))))
        
  )
)
  ; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
    (cond 
        ((eq? nil s) nil)
        
        ((= 1 (length s)) (cons s nil))
        
        ((> (car s) (cadr s)) 
            (cons (cons (car s) nil) (nondecreaselist (cdr s)))
            )
        ((< (car s) (cadr s)) 
            (cons(cons (car s) (nondecreaselist (cdr s))) nil)
            )
    )
)
    ; END PROBLEM 17

;; Problem EC
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((quoted? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
            (append (list form params) (map let-to-lambda body))
           ; END PROBLEM EC
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           'replace-this-line
           (define form (car (zip values)))
           (define params (map let-to-lambda (cadr (zip values))))
           (define body (map let-to-lambda body))
            (cons (append (list 'lambda form) body) params)
           ; END PROBLEM EC
           ))
        (else
         ; BEGIN PROBLEM EC
         'replace-this-line
         (map let-to-lambda expr)
         ; END PROBLEM EC
         )))

