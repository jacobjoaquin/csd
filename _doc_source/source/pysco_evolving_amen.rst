#######################################
The Evolving Amen Python Score Tutorial
#######################################

By Jacob Joaquin

jacobjoaquin@gmail.com

..
    TODO: Update orchesta. Envelope was added in variation example.
    TODO: hat() before evolving_amen_default_args.csd need updating
    TODO: drum_pattern_2 isn't in everything

    Note. 4 spaces, not tabs. Indentation sensitve

************
Introduction
************

Python Score, or Pysco for short, is a fully modular score environment
for the Csound unified CSD file. Unlike other alternative text-based
score environements, Pysco is non-imposing and does its best to get
out of the way rather than to impose a strict set of rules for
composition. Classical Csound score is fully supported, all of
Python 2.7 is available, and composers can pick and choose their
score tools A La Carte as the see fit.

This purpose of this tutorial is to try and prove the merits of
using the Python language in favor of the classical Csound score.
The classical score is a fixed system while Python is a very mature
and highly extensible language with a vast collection of first and
third party modules. Despite being a general purpose language that
wasn't designed for music, Python is particularly well suited for
compostion.

It should be noted that Python Score is not meant as a full replacement
of the classical Csound score, but as an enhancement. Any and all
existing classical score commands still work, and Python Score
itself outputs classical score code. Perhaps Python Score should
be thought as a user-friendly higher level abstraction of the classic
score, as is the case with Processing and Java.

Python Score is still early in development, though the library of
use cases and examples are rapidly growing, and all from a single
developer. The secondary purpose of this tutorial is to attract a
small group of people to start experimenting with this alternative
Csound score environment, to find out what works, what's easy and
what's not, and to collect new ideas for future upgrades. It is
also the belief of the author that once people have some hands-on
experience, many of the advantages of working with Python Score
will become obvious. Until then, it's just the ramblings of one
person's perspective.

Since Pysco is under development, consider this tutorial a living
document, and be updated to keep up with any changes. Send questions,
comments, and bugs to jacobjoaquin@gmail.com, or write to the Csound
Mailing List.

*"Y'all ready for this?"* - Michael J. Nelson [#michaeljnelson]_

The Orchestra
=============

In order to bring focus to the enhanced set of features and
compositional techniques Python and the Pysco module brings to the
score, every example uses the exact same orchestra throughout the
entirety of this tutorial. Let's quickly review:

.. literalinclude:: ../../demo/pysco/evolving_amen_1.csd
    :start-after: <CsInstruments
    :end-before: </CsInstruments

The orchestra contains only a single instrument, a basic sampler
with the Amen Break [#amen]_ as its only audio source. The instrument
includes support for three custom pfield insputs for amplitude, the
starting position in the sample (in beats), and for tuning the
sample. The fact that this is only a very basic instrument is on
purpose, as techniques discusse will include that even very simple
intruments can be enhanced using the newly available score functions.

The output of this device has a very trashy [#trashy]_ quality to
it, and sounds like it was produced with a tracker [#tracker]_ such
as Fast Tracker II.

There's also a reason for using a drum loop as an example. The
ability to express time and occurances in time is a defining attribute
of Python score, and percussion-based events are great for honing
in on timing. *Do not be mislead into thinking Python Score caters
to 4/4 drumming music, as this is far from the truth.*

The Python Interpretor
======================

The Python interpretor is an extremely convienient tool for tinkering with parts of the language you may not be familiar with. With it, you can safely test parts of the language.

Typically, the Python interpretor is used in the terminal, which is invoked by typing "python"::

    Quorra ~ $ python

This will starts an interactive Python session in which users can start entering various commands.

::

    >>> print 'hello world'
    hello world
    >>> 440 * 2 ** (-9 / 12.0)
    261.6255653005986
    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In addition to the terminal, you can use CsoundQt comes with a Python Console built-in. There's also `IPython <http://ipython.org/>`_ which supercharges the Python Interpretor with a lot of great features for Python beginners and veterans alike.

::

    In [53]: range?
    Type:       builtin_function_or_method
    String Form:<built-in function range>
    Namespace:  Python builtin
    Docstring:
    range([start,] stop[, step]) -> list of integers

    Return a list containing an arithmetic progression of integers.
    range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
    When step is given, it specifies the increment (or decrement).
    For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
    These are exactly the valid indices for a list of 4 elements.

Seeing the Output
=================

Python Score writes a copy of the generated score to a fild called _pysco.sco. This is good to know in case you want to see exactly what Python Score is doing, or need to debug an issues that arises.

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

It is the assertion of this author that this feature, and this feature alone, makes transitioning to Python Score worthwhile. 

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

::

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

.. literalinclude:: ../../demo/pysco/evolving_amen_instr_interface.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Pause For A Moment (Interlude)
==============================

* Data to structure
* fundamentally more expressive (which is a good thing with music)
* Even if you don't know python, this is fundamentally more readable
* Definitely read on, but practice the preceeding examples
* Everything you can do with the classical score you can do in Python Score. The opposite isn't true (not even close)

The score we're left with is fundamentally more readable than the original Csound score. The fact that drums are being played is much more obvious than in the original classical score.

*************************
Developing a Python Score
*************************

*"Sometimes you have to run before you learn how to walk."* - Tony Stark

Since Python is an open-ended environment, there are many ways in which to develop a personalized score environment for a piece. In this section, we'll build new features into our environment one by one. Many of these concepts may be used in other pieces either together, or individually.

The goal of this section is to introduce concepts that are readily available, while at the same time trying to make aware how much Python has to offer. The approach maybe a little aggressive at times, but at the same time none of the concepts introduced here are necessariy for your scores.

Each new Python Score idiom is distilled to a stand alone example. Entire scores are phased out to only the code added with each new example.

The orchestra will remain unchanged, though the score and audio examples will change through out.

Drum Pattern
============

We've seen function defintions for our custom measure-based cue() oobject and for defining score-based instrument interfaces. Python functions can also be used to consolidate snippets of score code into reusable musical phrases.

The four measures in the piece are identical, which makes it perfect for consolidating it into a single measure phrase.

.. literalinclude:: ../../demo/pysco/evolving_amen_hats.csd
    :language: python
    :pyobject: drum_pattern

Events that exist inside a function are not added into the score until the function is called. The updates to the score code does this once for each measure:

.. literalinclude:: ../../demo/pysco/evolving_amen_pattern.csd
    :language: python
    :start-after: score(
    :end-before: </CsScore>

It's worth noting that functions aren't limited to measures. Notes, licks, phrases, bars, sections, entire scores, can all be placed inside a function. We'll see more of this as we continue along.

Looping Through Lists
=====================

A list is a Python container for storing various data, which may include numbers, strings, other lists, functions, etc. And they make a wonderful additional to the score environment. They're highly versatile, capable of evertything from saving time for the composer through automation, to generating granular synthesis events, to algorithmic composition.

The for statement is used to loop through each value in the specified list. As the program loops through the list, the m variable becomes the value of the current value in the list. Thus, calling drum_pattern() for measures 1, 2, 3, and 4.

.. literalinclude:: ../../demo/pysco/evolving_amen_list.csd
    :language: python
    :start-after: score(
    :end-before: </CsScore>

Now that much of the score code has been consolidated into a function and a foor loop, this score is now 2 lines shorter than the original Csound classical score in the first example.

Range
=====

The Python range() generates lists of integers automatically. It's a very commonly used function in Python, and one you should learn sooner rather than later.

::

    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> range(1, 5)
    [1, 2, 3, 4]

The score substitues range(1, 5) for [1, 2, 3, 4]. 

.. literalinclude:: ../../demo/pysco/evolving_amen_range.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Sample Variation with Choice
============================

So far, all the functions we've used come either built-in or built by hand with a function. Python has an easy process for importing existing functions from various libraries. Python itself comes with a bunch of useful libraries that can be used within the context of a compositional environment. And then there are a bunch of a third party libraries that can be used as well. In fact, Pysco itself is a Python library.

To add a little variation to our kick() and snare() score instruments, the choice() function is imported and used to randomly select from different positions within the Amen break.

Changes are made to the kick() and snare() functions.

The choice() function is really simple to use. Pass a list of data to choice, and it randomly selects one of the values. Using the kick() score instrument as an example, choice selects from 4 different possible start positions in the Amen break where a kick is.

.. literalinclude:: ../../demo/pysco/evolving_amen_hats.csd
    :language: python
    :pyobject: kick

The snare() works the same way, with the only difference being the start positions.

.. literalinclude:: ../../demo/pysco/evolving_amen_hats.csd
    :language: python
    :pyobject: snare

Hats
====



The reaffirms the concept of single a instrument with multiple score-based interfaces.

* Reinforce one instrument, multiple score interfaces
* Include phrases within new phrases

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

Playing back the last example will sometimes lead to samples out range. Not everytime because of the random nature of our kick(), snare(), and hat() score instruments. There are many approaches one could take to fix this problem, with one using the Python Score pmap() function for post processing of pfield data.

To avoid samples being played out of range, we need to change all the amplitudes uniformly in the score. Multiplying each pfield 4, the amplitude input for the sampler, with a constant value will do this. First, let's create a function that take two arguments, and returns the product.

.. literalinclude:: ../../demo/pysco/evolving_amen_pmap.csd
    :language: python
    :pyobject: multiply

The pmap() function takes the following input::

    pmap(event_type, instr, pfield, function, *args, **kwargs)


The value of the pfield is passed in as the first arg, x, and 0.707 as y. Pfield 4 is replaced with the value returned by the multipy function

.. literalinclude:: ../../demo/pysco/evolving_amen_pmap.csd
    :language: python
    :start-after: with cue(t / 2.0):
    :end-before: </CsScore>

The pmap() function only works on data already in the score. For this reason, the best place for most cases will be either after the last even is created and/or at the very end of the score.

Pre-processing Events with p_callback()
=======================================

The p_callback() function is the pre-processing equivalent of pmap(). There are a few differences. First, the p_callback() registers a function to use against a specific pfield for a specific instrument ebefore data is entered into the score. When score data is entered, any events that match the selector of p_callback(), the data is then transformed before being entered into the score.

As an example, two related set of p_callback()'s are created. The first tunes all the drum events up a perfect 5th by altering the pfield 6 column used to tuning an instrument. Since this changing the pitch affects the length of the sample played back, causing to bleed into the next drum sample in the loop, a second p_callback() modifies the duration by the inverse of the perfect 5th.

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

The perfect 5th ratio was hard coded into the last example, but transposing data is something that is useful enough, especially in music, that it's worth taking the time to creating a function from it so that it may be used again and again.

The createdtranpose() function accepts two args, one which is required and one with a default value. The first arg is the value in halfsteps in which to transpose. Without a second arg, it gives the ratio of the transposition. If a second arg is supplied it will be applied absolutely.

.. literalinclude:: ../../demo/pysco/evolving_amen_transpose.csd
    :language: python
    :pyobject: transpose

The transpose() function is then used to refactor the p_callback()s.

.. literalinclude:: ../../demo/pysco/evolving_amen_transpose.csd
    :language: python
    :start-after: with cue(t / 2
    :end-before: score(

Upgrading Score Instruments with Defaults
=========================================

Earlier in the tutorial when score instruments were created for kick() and snare(), the ability to modify duration, amplitude, postion, and sampling tunig was factored out. We're going to factor everything except for the position argument back into these score instruments using keyword default values. The keywords for all three instruments are: dur, amp, and tune.

Since these are being refactored back in as keyword default args, all our existing calls to these score instruments will continue to work as is, and we're gaining the ability to use these args if we choose to use them.

Here is what the three score instruments look like now they all have default args:

.. literalinclude:: ../../demo/pysco/evolving_amen_default_args.csd
    :language: python
    :start-after: return value * 2 **
    :end-before: drum_pattern

Now that they're in, a test drum pattern is in order. This pattern just plays four kicks on the beat, transposed down a perfect 4th.

.. literalinclude:: ../../demo/pysco/evolving_amen_default_args.csd
    :language: python
    :pyobject: drum_pattern_2

The score and audio:

.. literalinclude:: ../../demo/pysco/evolving_amen_default_args.csd
    :language: python
    :start-after: score(
    :end-before: pmap

Player Instruments
==================

Functions can also be used to generate gestures. In a sense these are another for of score instruments. The implemented in this example takes as its first argument the function in which we want to play.

Since kick(), snare(), and hat() all have identical signatures for their argument inputs, creating a player instrument that can treat them equally is iis easy.

For the argument, we can pass kick, snare, or hat. The duration of the phrase is passed in as the second arg. The duration of the indivual notes is arg 3. The number of beats to play through the lifespan of the instrument if arg 4. The start_amp and end_amp args do a linear envelop from the first and last nights, which is similiar to the classical score ramp function. And then there is one optional keyword arg for consistant tuning for all samples played by swell().

.. literalinclude:: ../../demo/pysco/evolving_amen_swell.csd
    :language: python
    :pyobject: swell

Wrapping this up into a reuasable phrase:

.. literalinclude:: ../../demo/pysco/evolving_amen_swell.csd
    :language: python
    :pyobject: intro

Invocation and audio:

Algorithmic Flair Drum Pattern
==============================

For the last drum pattern of this tutorial, we're going to create one that has a bit of an algorithmic flair for randomly generating kicks, snares, and hats.

For this pattern, we're going to use the random function from Python's random library, which needs to be imported::

    from random import random

The pattern is defiend as:

.. literalinclude:: ../../demo/pysco/evolving_amen_flair.csd
    :language: python
    :pyobject: drum_pattern_flair

This pattern extends drum_pattern() by calling it first. If any chages are ever made to drum_pattern(), than drum_pattern_flair() would also reflect these changes.

The rest of the pattern works like this. Eight different start times, in beats, are placed in a list. A list of score instrument functions is also created. As a way to increase the probability that a hat() will play, it has been added to this list three times.

It then iterates through the times list. For each of these predeterimined potential start times, it checks a randomly generated number against the input argument r. If the number generated by random() is less than r then a new event is created.

The cue() object is set to the current value of variable time. The choice() functions chooses either kick, snare, hat, hat, or hat. Then the event is created, with a random amplitude in the range os 0.125 and 0.875.

The end result is something common in many drum and bass tracks in which is sounds as if percussional elements were generated at random, but still has the familiar kick and snare pattern.

.. literalinclude:: ../../demo/pysco/evolving_amen_flair.csd
    :language: python
    :start-after: score(
    :end-before: pmap

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
.. [#snozberry] Snozberry
