Csound Score Parsing Python Module
==================================

.. toctree::
   :maxdepth: 2

   score_module
   demo
   
Introduction
------------

This is an early release of the score module for processing Csound
score code.

This python module along with the command-line demos accepts Csound
score code at the standard input and processes them.

This package is currently a rough draft, and development will
definitely continue for the near future.  There are some definite
quirks, which will eventually be ironed out.

score.py contains the core functions that can be used to create
custom python scripts.  Everything is in a state of flux, so do
expect things to chage.

In the demo folder, you'll find five demo scripts: align.py,
arpeggiator.py, carry.py and swap_columns.py.  There are descriptions
beloew.  These scripts aren't thoroughly test, but you still may
find them useful.  align.py is probably the most reliable at the
moment.

In the test folder, there are many py scripts used to test the
functions defined in score.py.



.. warning::  These scripts are still experimental.  Back up any
        Csound work you plan on running through these scripts.



Info
----
Csound Score Parsing Python Module

By Jacob Joaquin

jacobjoaquin@gmail.com

http://www.thumbuki.com/

http://jacobjoaquin.tumblr.com/

http://twitter.com/JacobJoaquin

copyright (c) Jacob Joaquin 2009


License
-------
GNU Lesser General Public License

Version 3, 29 June 2007

http://http://www.gnu.org/licenses/lgpl.html

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

