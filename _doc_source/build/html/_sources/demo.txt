Demos
=====

These are demo examples of what can be built with the score module.
These are to be considered unstable releases until they are properly
tested and bug checked.

The demos are located in ``/score/demo``.

.. note:: Demos have only been tested using Apple's
    Python 2.5.1.  Further testing will need to be done in other
    versions of Python.


align.py
--------




Pipe Chain Trick
================

It is possible to chain pipes in series to process scores with
multiple scripts in one swoop.  The following command does two things.
First, it sums the values of pfields 4 in instrument 2 events with
0.99999 with sum.py.  The output is then piped into align.py, making
the columns tidy and neat::
    
    $ cat carry.sco | ./sum.py -si -i2 -p4 -v0.99999 | ./align.py

.. highlight:: none

Before::
        
    i 2 0 0.25 0.3 7.00
    i 2 + 0.25 0.3 7.00
    i 2 + 0.25 0.3 7.00
    /**/
    i 2 + 0.25 0.5 7.00
    i 2 + 0.25 0.3 7.00
    i 2 + 0.25 0.5 7.00
    i 1 0 0.25 0.5 7.00
    i 1 1 0.25 0.5 7.00
    i 1 1 0.25 0.5 7.00
    i 1 1 0.25 0.5 7.00
    
This outputs::
    
    i 2 0 0.25 1.29999 7.00
    i 2 + 0.25 1.29999 7.00
    i 2 + 0.25 1.29999 7.00
    /**/
    i 2 + 0.25 1.49999 7.00
    i 2 + 0.25 1.29999 7.00
    i 2 + 0.25 1.49999 7.00
    i 1 0 0.25 0.5     7.00
    i 1 1 0.25 0.5     7.00
    i 1 1 0.25 0.5     7.00
    i 1 1 0.25 0.5     7.00

