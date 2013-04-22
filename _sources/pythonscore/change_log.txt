%%%%%%%%%%%%%%%%%%%%%%
PythonScore Change Log
%%%%%%%%%%%%%%%%%%%%%%

Update 2013/4/22
================

Change Log created 2013/4/22

Added ``PythonScore.f()`` for creating Csound f-tables.  

Added ``PythonScore.t()`` for creating Csound tempo events.

Use PythonScoreBin instead of PythonScore in CSD files::

    from csd.pysco import PythonScoreBin

    score = PythonScoreBin()

Removed ``PythonScore.end()`` method. This is now automagically handled in ``PythonScoreBin``.

Prior to 2013/4/22
==================

Prior to this change log, PythonScore used to be called Pysco, and was an individual script that would be run by the bin CsScore option. It has since beem converted into a proper Python module, and many of the original functions are now methods of the PythonScore class and subclasses and have been renamed.
