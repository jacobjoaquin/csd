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
    
    $ cat arpeggiator.sco | ./arpeggiator.py -si -i1 -p4 -v'0.1 0.444 0.9922' | ./sco_align.py


.. highlight:: none
    
Arpeggiated and aligned::
    
    i 1 0 0.25 0.1    7.00
    i 1 + .    0.444  .
    i 1 + .    0.9922 .
    i 1 + .    0.1    .
    i 1 + .    0.444  .
    i 1 + .    0.9922 .
    i 1 + .    0.1    .
    i 1 + .    0.444  .


