Bugs
=====

* In some of the test scores, there are some score string examples using
  single quotes.  Single quotes are not supported by the score.
  
Planned Changes
===============

Major revisions are planned for this module.

Functions may support returning single events as strings and
multiple events as lists.  This might negate the need for column
functions like ``score.swap_column()``.
    
    >>> score.swap('i 1 0 4 1.0 440', 4, 5)
    'i 1 0 4 1.0 440'
    >>> score.swap('i 1 0 4 1.0 440\ni 1 4 8 0.5 770', 4, 5)
    ['i 1 0 4 440 1.0', 'i 1 4 8 770 0.5']

Error checking, exceptions, and warnings - *Oh my!!*

Eliminate redundant functions, add new ones as required.

