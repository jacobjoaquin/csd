######################
Evolving Amen Tutorial
######################

*"Y'all ready for this?"* - Michael J. Nelson [#michaeljnelson]_


..
    TODO: Update orchesta. Envelope was added in variation example.
    TODO: hat() before evolving_amen_default_args.csd need updating
    TODO: drum_pattern_2 isn't in everything

    Note. 4 spaces, not tabs. Indentation sensitve

************
Introduction
************

Python Score, also sometimes called Pysco, is a modular score environment. 

The reality is, Python Score is just Python.

The tutorial is based on an early example, which took surprisingly little time to make, clocking in around at around a few hours.

Pysco is also under development, and there will be changes made through its early life. And thus, any changes made to Pysco will be reflected in this tutorial. Consider this a living document.

The Sampler Instrument
======================

A simple stereo sampler instrument is used for the entirety of this tutorial. This is ensure that the focus solely on the techniques afforded by Python.

The sampler uses the famous Amen break. [#amen]_ It supports 3 custom pfield inputs for determining amplitude, the start position in beats of the sample, and an option for tuning the pitch of the sample.

.. literalinclude:: ../../demo/pysco/evolving_amen_1.csd
    :start-after: <CsInstruments
    :end-before: </CsInstruments

The output has a very trashy [#trashy]_ quality to it, and sounds like it was produced with a tracker [#tracker]_ such as Fast Tracker II.

The Python Interpretor
======================

The Python interpretor is an extremely convienient tool for tinkering with parts of the language you may not be familiar with. With it, you can safely test parts of the language.

Typically, the Python interpretor is used in the terminal, which is invoked by typing "python"::

    Quorra ~ $ python

This will starts an interactive Python session in which users can start entering various commands.

::

    >>> print 'hello world'
    hello world
    >>> 440 * 2 ** (7 / 12.0)
    659.2551138257398
    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In addition to the terminal, you can use CsoundQt comes with a Python Console built-in. There's also `IPython <http://ipython.org/>`_ which supercharges the Python Interpretor with a lot of great features for Python beginners and veterans alike.

************************
From Classical To Modern
************************

Some words here.

* Start with a classical score
* Port the score to Python
* Refactor classical score introducing Python score idioms one at a time
* End with a full conversion with identical output

Classical Csound Score
======================

The first phase of this tutorial starts with a classical Csound score. Over the course of several steps, the score is transformed into Python Score with new features slowly added and explained. The following is a four identical measures that plays the standard drum'n'bass beat. [#dnb]_

.. literalinclude:: ../../demo/pysco/evolving_amen_1.csd
    :start-after: <CsScore
    :end-before: </CsScore>

Porting the Classical Score to Python
=====================================

Porting a classical Csound score to Python Score is a straight forward process. First, the Csound Unified bin feature is specified to active pysco.bin. Second, the Csound score code is passed into the score() function as multiline string. Any and all Csound score code will work,

.. literalinclude:: ../../demo/pysco/evolving_amen_ported.csd
    :language: python
    :start-after: </CsInstruments>
    :end-before: </CsoundSynthesizers>

In Python, triple quotes allow for multi-line strings.

The Movable Cue() Object
========================

*"It's what makes time travel possible."* - Dr. Emmett Lathrop Brown

The “cue” is a bit like a flux capacitor, as it makes time travel possible. It allows the composer to move to any point in time in the score, treat the current time if it's time zero, and then move to somewhere else. 


All events entered are entered relative to the cue(). If the cue is at 33, then events placed at 0 and 4 will be placed into the score at 33 and 37.

The Python Score cue object is a device for moving the start pointer. The pfield 2 valu

The unit of time for cue is in beats, which is the same as the classical Csound score. Unless a tempo is specified, the default value is 60 beats per minute, which is the same as time in seconds.

The # symbol denotes a Python comment, and works similarly to the ; symbol in the Csound score.

* What is the cue?
* In beats
* pfield 2
* single quotes for score
* The # comment

Even in situations in which the timing of events are deeply nested with a complex algorithm, the structure of when things happen is far more transparent since time is factored out and exists as its own entity.

Instead of entering time-based events in absolute terms of the score, they are entered to relative to the position of the cue() object. For example, if the cumulative postion of the cue is 60 beats, entering an event at time 0 is actually 60, and a time of 4 would be 64.

Realative instead of absolute.

.. literalinclude:: ../../demo/pysco/evolving_amen_cue.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Beats to Measures
=================

Python is a highly extensible language and allows composers to shape their score environment by defining new features on the fly as functions. See `Defining Functions <http://docs.python.org/2/tutorial/controlflow.html#defining-functions>`_.

In the case the music we're dealing with is standard 4/4. Working in measures makes more sense than working in global beats. 


In this instance, the cue object is transformed from beats to measures. This is accomplished by this two line function:

.. literalinclude:: ../../demo/pysco/evolving_amen_measure.csd
    :language: python
    :pyobject: measure

Users pass in the measure they want to create events for, the math translates the from measure to beats, and then returns the cue object with the time set accordingly.

Since function itself is called measure, the "# Measure" comments are factored out.

.. literalinclude:: ../../demo/pysco/evolving_amen_measure.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

::

    >>> def measure_math(t):
    ...     return (t - 1) * 4
    ...
    >>> measure_math(1)
    0
    >>> measure_math(4)
    12

Generating Instrument Events
============================

A second method for entering score data exists in Python Score::

    event_i(1, 0, 1, 0.707, 8.00)

will generate this line of score code::

    i 1 0 1 0.707 8.00

In this iteration of the score, the instrument events that were previously entered through the score() function have been converted using event_i().

.. literalinclude:: ../../demo/pysco/evolving_amen_event_i.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Nested Cues
===========

The cue() object is designed to support multiple levels of nesting

..

    with cue(32):
        with cue(4):
            with cue(1):
                event_i(1, 0, 1)

Though the start time of the event is written as 0, the actual start time of the event is 37, which is the cumulation of all the args in the cue hierarchy.

* Start times are separated from event

In the score, all the start times are set to 0, giving the responsibility of when things happen to the cue().  

.. literalinclude:: ../../demo/pysco/evolving_amen_nested.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Score Instruments
=================

A orchestra instrument has only one interface, though it is possible to define multiple new interfaces in Python, which in a sense creates a new category of instruments.

The sampler instrument in the orchestra, even with the fixed Amen break, is designed to be non-specific in terms of what is played; It knows the position in the audio table to begin playing, but has no knowledge of what is being played.

Defining new interfaces to the sampler brings context to the score. In this case, the kick() and snare() functions are created.

This also being clarity to the score. In the clasical score, a composer is required to scan the positional numbers in the pfield 6 column to see what was being played, and they'd need to also know what these numbers meant.

In the Python score, if you play a kick() it sounds like a kick. Play a snare() it sounds like a snare. Play a snozberry() it sounds like a snozberry(). [#snozberry]_

The score we're left with is fundamentally more readable than the original Csound score. The fact that drums are being played is much more obvious than in the original classical score.

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


*************
The New Style
*************

*"Sometimes you have to run before you learn how to walk."* - Tony Stark

* Remeber, it's Python
* Aggresive with introducing Python concepts
* Continue doing 1 idiom at a time
* Excerpts as examples. Make sure you take the time to read them

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
    :pyobject: hat

New pattern. Musical phrases defined as functions can be embedded into other phrase functions.

.. literalinclude:: ../../demo/pysco/evolving_amen_hats.csd
    :language: python
    :pyobject: drum_pattern_8th_hats

One thing worth mentioning is to create the 8th note rhythms, the foor loop iterates through the values 0 through 7, and then each value is divided by 2.0 as the argument for cue().

.. literalinclude:: ../../demo/pysco/evolving_amen_hats.csd
    :language: python
    :start-after: score(
    :end-before: </CsScore>

Post Processing with pmap()
===========================

* pmap post processing
* Usually comes at end
* custom function for multiplying
* The value of the pfield is passed in as the first arg, x, and 0.707 as y. Pfield 4 is replaced with the value returned by the multipy function

.. literalinclude:: ../../demo/pysco/evolving_amen_pmap.csd
    :language: python
    :pyobject: multiply

The pmap() function only works on data already in the score. For this simple reason, the best place for most cases will be either after the last even is created and/or at the very end of the score.

.. literalinclude:: ../../demo/pysco/evolving_amen_pmap.csd
    :language: python
    :start-after: with cue(t / 2.0):
    :end-before: </CsScore>

Pre-processing Events with p_callback()
=======================================

* What is p_callback. Pre-processor version.
* Should be placed for the events to be processed
* math for pefect 5th
* Increasing the pitch by a 5th requires the duration to be reduced by the inverse of the perfect 5th

.. literalinclude:: ../../demo/pysco/evolving_amen_p_callback.csd
    :language: python
    :start-after: with cue(t / 2.0)
    :end-before:  score(

Where these callbacks are placed matter. Typically speak, good practice involves placing the p_callback() functions before any events are placed in the score. In this example, these are places just prior to score().

.. literalinclude:: ../../demo/pysco/evolving_amen_p_callback.csd
    :language: python
    :start-after: with cue(t / 2.0)
    :end-before:  </CsScore

Transpose
=========

* That code might be useful, so let's wrap it into a function
* Requires 1 arg, 1 optional

.. literalinclude:: ../../demo/pysco/evolving_amen_transpose.csd
    :language: python
    :pyobject: transpose

.. literalinclude:: ../../demo/pysco/evolving_amen_transpose.csd
    :language: python
    :start-after: with cue(t / 2
    :end-before: score(

Default Def Values
==================

* def with default value
* used in order from left to right
* or calling them by name
* user input is for all 3 args is designed to accept ratios

.. literalinclude:: ../../demo/pysco/evolving_amen_default_args.csd
    :language: python
    :pyobject: kick

.. literalinclude:: ../../demo/pysco/evolving_amen_default_args.csd
    :language: python
    :pyobject: snare

.. literalinclude:: ../../demo/pysco/evolving_amen_default_args.csd
    :language: python
    :pyobject: hat

.. literalinclude:: ../../demo/pysco/evolving_amen_default_args.csd
    :language: python
    :pyobject: drum_pattern_2

.. literalinclude:: ../../demo/pysco/evolving_amen_default_args.csd
    :language: python
    :start-after: score(
    :end-before: pmap

Swell
=====

* Gesture
* Possible because kick, snare, hat have identical interfaces
* Describe parameters
* A pattern is emerging, and Python objects could be used, but that's the subject of another tutorial

.. literalinclude:: ../../demo/pysco/evolving_amen_swell.csd
    :language: python
    :pyobject: intro

.. literalinclude:: ../../demo/pysco/evolving_amen_swell.csd
    :language: python
    :pyobject: swell

Algorithmic Flair Drum Pattern
==============================

* import random
* for each point in time, if event is generated, play a random instrument with a random amplitude

.. literalinclude:: ../../demo/pysco/evolving_amen_flair.csd
    :language: python
    :start-after: score(
    :end-before: pmap

.. literalinclude:: ../../demo/pysco/evolving_amen_flair.csd
    :language: python
    :pyobject: drum_pattern_flair

Form With Functions
===================

.. literalinclude:: ../../demo/pysco/evolving_amen_final.csd
    :language: python
    :start-after: score(
    :end-before: pmap

.. rubric:: Footnotes

.. [#michaeljnelson] Link to funny tweet
.. [#amen] Amen break description
.. [#trashy] Trashy is a good thing in the right context.
.. [#tracker] Trackers are the bee's knees
.. [#dnb] Drum'n'bass beat

