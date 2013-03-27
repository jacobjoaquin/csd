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

    pbpaste | ./sco_align.py | pbcopy

Go back to your text editor, and with the section of score code still
highlighted, paste.  The highlighted test will be replaced with your
newly processed score.
   
Pipe Chain Trick
----------------

You can chain multiple csd scripts in a row to do several csd processes
in a single swoop.  The following example does three things.  First, it
transposes pfield 5 by two octaves with ``pfunc.py``.  Then the output
of ``pfunc.py`` is piped into ``arpeggiator.py``, processing that
amplitude values in p4.  The resulting score is made neat and tidy with
``sco_align.py``::
    
    cat arpeggiator.sco | \
    > ./pfunc.py i 1 5 'x + 2' | \
    > ./arpeggiator.py i 1 4 '0.1 0.444 0.9922' | \
    > ./sco_align.py

Before::

    i 1 0 0.25 0.3 7.00
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    i 1 + .    .   .
    
After::
    
    i 1 0 0.25 0.1    9.0
    i 1 + .    0.444  .
    i 1 + .    0.9922 .
    i 1 + .    0.1    .
    i 1 + .    0.444  .
    i 1 + .    0.9922 .
    i 1 + .    0.1    .
    i 1 + .    0.444  .


