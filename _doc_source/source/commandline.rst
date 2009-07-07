Command-line Operations
=======================

Pasteboard Trick (for OS X)
---------------------------

OS X comes with two commands that can easily aid in the process of
using these demo scripts in your work flow: ``pbpaste`` and ``pbcopy``.
These paste and copy the contents of the pasteboard in the OS X
Terminal.

To use in a workflow, highlight a section of score you want to process,
copy the selection, type the following into the Terminal::

    $ pbpaste | ./align.py | pbcopy

Go back to your text editor, and with the section of score code still
highlighted, paste.  The highlighted test will be replaced with your
newly processed score.
   
Pipe Chain Trick
----------------

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
    
After::
    
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

