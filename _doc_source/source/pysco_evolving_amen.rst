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


TODO: Update orchesta. Envelope was added in variation example.
TODO: hat() before evolving_amen_default_args.csd need updating
TODO: drum_pattern_2 isn't in everything

Note. 4 spaces, not tabs. Indentation sensitve

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

List
====

* Python List
* Looping
* Crossed an interesting threshold. The Python Score is 2 lines shorter than the original classical score

.. literalinclude:: ../../demo/pysco/evolving_amen_list.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Range
=====

* range()
* Python interpretor
* Adding 4 more measures would require a single change, from 5 to 9
* If 5 to 9, more events generated than there are lines of code in CsScore

.. literalinclude:: ../../demo/pysco/evolving_amen_range.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Sample Variation with Choice
============================

New Audio File

* Import from library
* choice

.. literalinclude:: ../../demo/pysco/evolving_amen_choice.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Hats
====

* Reinforce one instrument, multiple score interfaces
* Include phrases within new phrases
* Samples out of range

     number of samples out of range:       25       25

.. literalinclude:: ../../demo/pysco/evolving_amen_hats.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Post Processing with pmap()
===========================

* pmap post processing
* Usually comes at end
* custom function for multiplying
* The value of the pfield is passed in as the first arg, x, and 0.707 as y. Pfield 4 is replaced with the value returned by the multipy function

.. literalinclude:: ../../demo/pysco/evolving_amen_pmap.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Pre-processing Events with p_callback()
=======================================

* What is p_callback. Pre-processor version.
* Should be placed for the events to be processed
* math for pefect 5th
* Increasing the pitch by a 5th requires the duration to be reduced by the inverse of the perfect 5th

.. literalinclude:: ../../demo/pysco/evolving_amen_p_callback.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Transpose
=========

* That code might be useful, so let's wrap it into a function
* Requires 1 arg, 1 optional

.. literalinclude:: ../../demo/pysco/evolving_amen_transpose.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Default Def Values
==================

* def with default value
* used in order from left to right
* or calling them by name
* user input is for all 3 args is designed to accept ratios

.. literalinclude:: ../../demo/pysco/evolving_amen_default_args.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Swell
=====

* Gesture
* Possible because kick, snare, hat have identical interfaces
* Describe parameters
* A pattern is emerging, and Python objects could be used, but that's the subject of another tutorial

.. literalinclude:: ../../demo/pysco/evolving_amen_swell.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

.. literalinclude:: ../../demo/pysco/evolving_amen_swell.csd
    :language: python
    :pyobject: swell

Algorithmic Flair Drum Pattern
==============================

* import random
* for each point in time, if event is generated, play a random instrument with a random amplitude

.. literalinclude:: ../../demo/pysco/evolving_amen_flair.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

.. literalinclude:: ../../demo/pysco/evolving_amen_flair.csd
    :language: python
    :pyobject: drum_pattern_flair

Write Some Music
================


