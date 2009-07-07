i1 0 4 6.04 15000 2 100 81 50 56 20 1 ; No alignment
i1 + . . . . 101 . . . . . 
i1 + . 5.04 . . 100 . . . . . 
i1 + . . . . 101 . . . . . 
i1 + . 6.04 . 2 100 . . . . . 
i1 + . . . . 101 . . . . . 
i1 + . 5.04 . . 100 . . . . . 
i1 + . . . . 101 . . . . . 


i1 0 1 0.1 8.00 0.5 0.333333  ; Begin new section
i1 + . .   .    .   .  ; Comment
i1 + . .   .    .   .  ; Another comment
i1 + . .   .    0.75   .  ; And one more
i1 10 0.44 0.99 5.05 0 1  ; Swap mix-rates of last 2 pfields
i1 + 0.44 0.99 5.02 < <
i1 + 0.44 [~ * 0.5 + 0.5] 5.01 < <  ; Expressions work
i 1 + 0.44 [~ * 0.8 + 0.2] 5.00 < <
i 1  + 0.44 . 5.00 < <
i 1 + 0.6333 0.88 6.04 1 0


i 7 16.4 3.5 8000 5.019 0.2 0.7 0.5 2 3 0.1 ; Mangled snippet from Trapped
i 7 19.3 6.4 8000 5.041 . 0.9 1 3 2 0.1
i 9 26.7 1.9 "file.wav" 4.114 . 0.1 5.9 300
i 9 29.1 2.1 0.1 5.013 . 0.2 4.2 390
i 99 32 6.2 0.28 ; Comments are aligned
i 9 32 9.1 0.34 5.051 2300 0.5 3.8 420


i "foo" 0 $macro 0 3 ; Strings and macros work
i $bar 0 1 2 3  ; See.



