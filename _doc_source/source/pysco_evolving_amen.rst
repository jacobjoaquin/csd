################################
Evolving Amen - A Pycso Tutorial
################################

..
    Set up Sampler Instrument
    Classical Score example with 1 bar repeat 4 times
    score() version
    split bars with cue()
    def measure()
    instrs as definitions
        factoring out instr number, start time, duration
        default values
        One orchestra instrument becomes many score instruments
    Refactor instrs
        Importing choice from Python Library
        Choice
        Lists
    Score phrase to def phrase()
    Algorithmic flair def
        Lists

    Arranging

    Where to put p_callback and pmap
        dB for p_callback
        slight variations to pan position / pitch for pmap


.. literalinclude:: ../../demo/pysco/evolving_amen_1.csd
    :start-after: <CsInstruments
    :end-before: </CsInstruments

Classical Csound Score
======================

.. literalinclude:: ../../demo/pysco/evolving_amen_1.csd
    :start-after: <CsScore
    :end-before: </CsScore>

Porting to Python Score
=======================

* bin
* score()
* triple single quotes

.. literalinclude:: ../../demo/pysco/evolving_amen_ported.csd
    :language: python
    :start-after: </CsInstruments>
    :end-before: </CsoundSynthesizers>

Cue
===

* What is the cue?
* In beats
* pfield 2
* single quotes for score
* The # comment

.. literalinclude:: ../../demo/pysco/evolving_amen_cue.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Measure
=======

* Factored out comment, the indicator is now code
* def
* example of the extensible nature of Python

.. literalinclude:: ../../demo/pysco/evolving_amen_measure.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

event_i
=======

* Classical data to python event
* event_i
* nested cue

.. literalinclude:: ../../demo/pysco/evolving_amen_event_i.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Nested Cues
===========

* Cues are nestable
* Start times are separated from event

.. literalinclude:: ../../demo/pysco/evolving_amen_nested.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Score Instrument Interfaces
===========================

* 1 instrument, multiple def interfaces
* factor out instr number, start time 

.. literalinclude:: ../../demo/pysco/evolving_amen_instr_interface.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Pause For A Moment
==================

* Data to structure
* fundamentally more expressive (which is a good thing with music)
* Even if you don't know python, this is fundamentally more readable
* Definitely read on, but practice the preceeding examples

Moving Forward
--------------

For the rest of the tutorial, concepts will be introduced through making changes to the music.

Goal is to show fluidity in composition

Drum Pattern
============

* Defs as containers for reusable musical pharase
* Consolidating code that is used multiple times
* Pattern isn't inserted into the score until it is called

.. literalinclude:: ../../demo/pysco/evolving_amen_pattern.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Range
=====

* The score is now 6 lines shorter than the original, even with defining 4 custom functions
* range()
* Python List
* Looping
* Adding 4 more measures would require a single change, from 5 to 9
* If 5 to 9, more events generated than there are lines of code in CsScore
* Python interpretor

[0, 1, 2, 3]

.. literalinclude:: ../../demo/pysco/evolving_amen_range.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Default Def Values
==================

* def with default value








