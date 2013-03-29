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

* event_i
* nested cue

.. literalinclude:: ../../demo/pysco/evolving_amen_event_i.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Score Instrument Interfaces
===========================

* def with default value
* 1 instrument, multiple def interfaces
* factor out instr number, start time 

.. literalinclude:: ../../demo/pysco/evolving_amen_instr_interface.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>












