#############################
The Amen Break Scorc Tutorial
#############################

By Jacob Joaquin jacobjoaquin@gmail.com

..
    TODO: Update orchesta. Envelope was added in variation example.
    TODO: hat() before evolving_amen_default_args.csd need updating
    TODO: drum_pattern_2 isn't in everything
    TODO: (1 / tune) should be float(tune). In many files near the end me thinks

scorc

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

.. literalinclude:: ../../examples/tutorials/amen/amen_classic.csd
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
in on timing. *Do not get the wrong impressiong that Python Score caters
to 4/4 drumming music, as this is far from the truth.*

The Python Interpretor
======================

Before moving into the tutorial, an introduction the the Python
Interpretor is in order as it a wonderful tool for quickly testing
various aspects of the Python language. This tutorial will occasionaly
use this as well.

Typically, the Python interpretor is used in the terminal, which
is invoked by typing "python"::

    Quorra ~ $ python

This will starts an interactive Python session in which users can
start entering various commands.

::

    >>> print 'hello world'
    hello world
    >>> 440 * 2 ** (-9 / 12.0)
    261.6255653005986
    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

The `CsoundQt <http://qutecsound.sourceforge.net/>`_ graphical front
end comes equimed with a Python console. There's also `IPython
<http://ipython.org/>`_ which supercharges the Python Interpretor
with a lot of great features for Python beginners and veterans
alike.

Seeing the Generated Classical Score
====================================

Python Score writes a copy of the generated score to a fild called
_pysco.sco. This is good to know in case you want to see exactly
what Python Score is doing, or need to debug an issues that arises.

****************************************
From the Classical Score to Python Score
****************************************

In this section, the will walk you through some the more basic
features of Python Score. The tutorial starts with a classical
Csound score, and adds new Python Score idioums one by one until
the score as been fully translated. The end result is the new Python
score.

.. literalinclude:: ../../examples/tutorials/amen/amen_classic.csd
    :start-after: <CsScore
    :end-before: </CsScore>

The score code produces 4 measures of the same drum pattern. The
pattern itself is the classical drum 'n' bass. [#dnb]_

AUDIO HERE

Upgrade
=======



Porting a classical score into the Python Score environment requires
only two changes. First, one needs to set the argument of the CsScore
bin utility to "python pysco.py". Second, the classical score code
needs to be passed as a string to the score() object. These changes
result in the followin Python Score code:

.. literalinclude:: ../../examples/tutorials/amen/amen_upgrade.csd
    :language: python
    :start-after: </CsInstruments>
    :end-before: </CsoundSynthesizers>

If you are worried that you would have to throw out everything you
know about the classic Csound score, fear not because you can still
use it with the score() object  virtually untouched, or in combination
with other Python features as you learn them.

Time is Relative
================

*"It's what makes time travel possible."* - Dr. Emmett Lathrop Brown
[#fluxcapacitor]_

For the most part, when events are entered into a classical Csound
score, the start times are in global beats. Python Score changes
with by introducing the cue() object, which is a Python context
manager for moving the current postion in time in the score. All
events entered into Python Score are relative the current positional
value of the cue().

::

    with cue(12):
        score('i 1 0 0.5 0.707 0 0')

While the start time value in pfield 2 is 0, this event will start
at 12 beats into the piece. This is because start time events are
process to reflect the current position of the cue(). The output
looks like this:

::

    i 1 12 0.5 0.707 0 0

As for translating the drum 'n' bass parts, each measure has been
split into its own chuck of events. The first event in measure 2
has been changed to 0.0, and the same goes for measures 3 and 4.
The cue() object allows the composer to think of time local to the
current measure, rather than manually calculate the global time.

.. literalinclude:: ../../examples/tutorials/amen/amen_cue.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

There are of course many more benefits. For example, moving entire
sections of code is a fairly trivial process in Pysco. Doing the
same in the classical score could require translating start times
down a long pfield 2 column. It is the assertion of the author that
this feature, and this feature alone, makes transitioning to Python
Score more than worthwhile.

Measures
========

The drum 'n' bass score is in 4/4. While the cue() object allows
us to treat beats local to the current measure, the arguments for
the cue() are in absolute global time in the previous section. Out
of the box, Python Score does not support measures. However, Python
lets you *roll your own*. Implementing 4/4 measures is done by
`defining a new function
<http://docs.python.org/2/tutorial/controlflow.html#defining-functions>`_.

.. literalinclude:: ../../examples/tutorials/amen/amen_measure.csd
    :language: python
    :pyobject: measure

This two line custom function takes the measure number as its sole
argument and translates measure time to beat time, and returns an
instance of cue().

*"Mathematical!"* - Jake the Human [#adventuretime]_

Let's focus little on the math. The global score starts at 0, but
measures start at 1. The is overcome with an offset of -1. In 4/4,
there are four beats per measure, which requires the offset value
to be multplied by 4. Testing the math in the Python Interpretor
with inputting 4::

    >>> def test_my_math(t):
    ...     return (t - 1) * 4.0
    ...
    >>> test_my_math(4)
    12.0

The value returned is 12, which is the starting time of the first
event in measure 4 in the original classical score. Applying measure()
to the Python score, were left with the following. Notice that the
comments have been factored out now that the code itself clearly
indicates what a measure is:

.. literalinclude:: ../../examples/tutorials/amen/amen_measure.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Instrument Event Function
=========================

The event_i() function is another way for entering in data into the
score. Instead of a string, it accepts any number of arguments and
constructs a valid classical score event string. For example::

    score.i(1, 0, 1, 0.707, 8.00)

Outputs::

    i 1 0 1 0.707 8.00

Replacing the calls to score() with event_i in the Amen score, the
updated code looks like this:

.. literalinclude:: ../../examples/tutorials/amen/amen_i.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Nesting Time
============

A ``with cue()`` statement can be placed inside a heiarchy of other
``with cue()`` statements. This allows composers to reset the
relative positional time to 0 regardless of the current scope of
time by writing another ``with cue()`` statement: For example, this
is possible::

    with cue(32):
        with cue(4):
                event_i(1, 0, 1)

Though the start time of the event is written as 0, the actual start
time of the event is 37, which is the cumulation of all the args
in the cue nesting hierarchy plus pfield 2: ``32 + 4 + 1 + 0``

The greater implication is that time can be completely decoupled
from the event within the code. In this version of the score the
start times are moved from the pfield 2 column to the the ``cue()``,
and then set to 0.

.. literalinclude:: ../../examples/tutorials/amen/amen_nest.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

The code right is a little messy, but this will be cleaned up.

Score Instruments
=================

Composers can create named Python functions that call their
corresponding orchestra instruments. Furthermore, multiple functions
can be created to the same instrument, but with more specific intent
as to the resulting behavoir of the intruments.

The sampler instrument in the orchestra is fairly simple and generic
in design. While the Amen Break loop is fixed, the instrument itself
has no knowledge of kicks or hats. It only accesses the part of the
sample denoted by the positional value passed in through pfield-5.

Looking at the Python Score code from the last example, there are
only two unique calls to score.i(), and even then all the arguments
are identical except for pfield-5::

	score.i(1, 0, 0.5, 0.707, 0, 1)
	score.i(1, 0, 0.5, 0.707, 1, 1)

The former plays a kick drum while the latter plays a snare. Though
looking at the code you might not know which is which and who is
who. [#darksideofthemoon]_ This is because the difference is just
the data used in pfield 5.

These statements are also unnecessirly long in Python and are ripe
to for consolidation. Defining functions for the kick and snare
avoids the extra overhead by factoring out all the args. Something
is made possible by the ``cue()`` object.

.. literalinclude:: ../../examples/tutorials/amen/amen_instr.csd
    :language: python
    :start-after: return cue(
    :end-before: score =

An equally important benefit to this approach is that with proper
names, this techinique creates code that is self documenting and
easier to read. If you type kick() it plays a kick. Type snare()
it plays a snare. Type snozberry() it plays a snozberry(). [#snozberry]_

.. literalinclude:: ../../examples/tutorials/amen/amen_instr.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Drum Pattern
============

The score contains four measures that contain identical content.
Functions can store musical phrases, everything from a single note
to complete works of Beethoven if necessary. In this case, we have
a simple 4 notes drum 'n' bass pattern.

.. literalinclude:: ../../examples/tutorials/amen/amen_pattern.csd
    :language: python
    :pyobject: drum_pattern

These events will not be generated until the function is accessed.
For each measure, four lines of score instruments is replaced with
drum_pattern().

.. literalinclude:: ../../demo/pysco/evolving_amen_pattern.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Functions aren't limited to storing measures of data. Notes, licks,
phrases, bars, sections, entire scores, can all be placed inside a
function. Later when it's time to start arranging, musical patterns
like these can be more or less dropped into ``measure()`` blocks.

Interlude
=========

This is a good moment to pause and take a close look at the concepts introduced.

* Data to structure
* fundamentally more expressive (which is a good thing with music)
* Even if you don't know python, this is fundamentally more readable
* Definitely read on, but practice the preceeding examples
* Everything you can do with the classical score you can do in Python Score. The opposite isn't true (not even close)

The score we're left with is fundamentally more readable than the original Csound score. The fact that drums are being played is much more obvious than in the original classical score.

Starting with the next section

*************************
Further Score Development
*************************

Since Python is an open-ended environment, there are many ways in which to develop a personalized score environment for a piece. In this section, we'll build new features into our environment one by one. Many of these concepts may be used in other pieces either together, or individually.

The goal of this section is to introduce concepts that are readily available, while at the same time trying to make aware how much Python has to offer. The approach maybe a little aggressive at times, but at the same time none of the concepts introduced here are necessariy for your scores.

Each new Python Score idiom is distilled to a stand alone example. Entire scores are phased out to only the code added with each new example.

The orchestra will remain unchanged, though the score and audio examples will change through out.

Looping Through Lists
=====================

A list is a Python container for storing various data, which may include numbers, strings, other lists, functions, etc. And they make a wonderful additional to the score environment. They're highly versatile, capable of evertything from saving time for the composer through automation, to generating granular synthesis events, to algorithmic composition.

The for statement is used to loop through each value in the specified list. As the program loops through the list, the m variable becomes the value of the current value in the list. Thus, calling drum_pattern() for measures 1, 2, 3, and 4.

.. literalinclude:: ../../examples/tutorials/amen/amen_list.csd
    :language: python
    :start-after: score.write(
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

.. literalinclude:: ../../examples/tutorials/amen/amen_range.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

Choice Variation
================

So far, all the functions we've used come either built-in or built by hand with a function. Python has an easy process for importing existing functions from various libraries. Python itself comes with a bunch of useful libraries that can be used within the context of a compositional environment. And then there are a bunch of a third party libraries that can be used as well. In fact, Pysco itself is a Python library.

To add a little variation to our kick() and snare() score instruments, the choice() function is imported and used to randomly select from different positions within the Amen break.

Changes are made to the kick() and snare() functions.

The choice() function is really simple to use. Pass a list of data to choice, and it randomly selects one of the values. Using the kick() score instrument as an example, choice selects from 4 different possible start positions in the Amen break where a kick is.

.. literalinclude:: ../../examples/tutorials/amen/amen_choice.csd
    :language: python
    :pyobject: kick

The snare() works the same way, with the only difference being the start positions.

.. literalinclude:: ../../examples/tutorials/amen/amen_choice.csd
    :language: python
    :pyobject: snare

Hats
====

The reaffirms the concept of single a instrument with multiple score-based interfaces.

* Reinforce one instrument, multiple score interfaces
* Include phrases within new phrases

.. literalinclude:: ../../examples/tutorials/amen/amen_hats.csd
    :language: python
    :pyobject: hat

New pattern. Musical phrases defined as functions can be embedded into other phrase functions.

.. literalinclude:: ../../examples/tutorials/amen/amen_hats.csd
    :language: python
    :pyobject: drum_pattern_8th_hats

One thing worth mentioning is to create the 8th note rhythms, the foor loop iterates through the values 0 through 7, and then each value is divided by 2.0 as the argument for cue().

.. literalinclude:: ../../examples/tutorials/amen/amen_hats.csd
    :language: python
    :start-after: score.write(
    :end-before: score.end()

Post Processing with pmap()
===========================

Playing back the last example will sometimes lead to samples out range. Not everytime because of the random nature of our kick(), snare(), and hat() score instruments. There are many approaches one could take to fix this problem, with one using the Python Score pmap() function for post processing of pfield data.

To avoid samples being played out of range, we need to change all the amplitudes uniformly in the score. Multiplying each pfield 4, the amplitude input for the sampler, with a constant value will do this. First, let's create a function that take two arguments, and returns the product.

.. literalinclude:: ../../examples/tutorials/amen/amen_postprocess.csd
    :language: python
    :pyobject: multiply

The pmap() function takes the following input::

    pmap(event_type, instr, pfield, function, *args, **kwargs)


The value of the pfield is passed in as the first arg, x, and 0.707 as y. Pfield 4 is replaced with the value returned by the multipy function

.. literalinclude:: ../../examples/tutorials/amen/amen_postprocess.csd
    :language: python
    :start-after: cue = score.cue
    :end-before: </CsScore>

The pmap() function only works on data already in the score. For this reason, the best place for most cases will be either after the last even is created and/or at the very end of the score.

Pre-processing Events with p_callback()
=======================================

The p_callback() function is the pre-processing equivalent of pmap(). There are a few differences. First, the p_callback() registers a function to use against a specific pfield for a specific instrument ebefore data is entered into the score. When score data is entered, any events that match the selector of p_callback(), the data is then transformed before being entered into the score.

As an example, two related set of p_callback()'s are created. The first tunes all the drum events up a perfect 5th by altering the pfield 6 column used to tuning an instrument. Since this changing the pitch affects the length of the sample played back, causing to bleed into the next drum sample in the loop, a second p_callback() modifies the duration by the inverse of the perfect 5th.

.. literalinclude:: ../../examples/tutorials/amen/amen_preprocess.csd
    :language: python
    :start-after: cue = score.cue
    :end-before:  score.write(

Where these callbacks are placed matter. Typically speak, good practice involves placing the p_callback() functions before any events are placed in the score. In this example, these are places just prior to score().

.. literalinclude:: ../../examples/tutorials/amen/amen_preprocess.csd
    :language: python
    :start-after: cue = score.cue
    :end-before:  </CsScore

Transpose
=========

The perfect 5th ratio was hard coded into the last example, but transposing data is something that is useful enough, especially in music, that it's worth taking the time to creating a function from it so that it may be used again and again.

The createdtranpose() function accepts two args, one which is required and one with a default value. The first arg is the value in halfsteps in which to transpose. Without a second arg, it gives the ratio of the transposition. If a second arg is supplied it will be applied absolutely.

.. literalinclude:: ../../examples/tutorials/amen/amen_transpose.csd
    :language: python
    :pyobject: transpose

The transpose() function is then used to refactor the p_callback()s.

.. literalinclude:: ../../examples/tutorials/amen/amen_transpose.csd
    :language: python
    :start-after: cue = score.cue
    :end-before: score.write(

Default Values for Score Instruments
====================================

Earlier in the tutorial when score instruments were created for kick() and snare(), the ability to modify duration, amplitude, postion, and sampling tunig was factored out. We're going to factor everything except for the position argument back into these score instruments using keyword default values. The keywords for all three instruments are: dur, amp, and tune.

Since these are being refactored back in as keyword default args, all our existing calls to these score instruments will continue to work as is, and we're gaining the ability to use these args if we choose to use them.

Here is what the three score instruments look like now they all have default args:

.. literalinclude:: ../../examples/tutorials/amen/amen_default_args.csd
    :language: python
    :start-after: return value * 2 **
    :end-before: drum_pattern

Now that they're in, a test drum pattern is in order. This pattern just plays four kicks on the beat, transposed down a perfect 4th.

.. literalinclude:: ../../examples/tutorials/amen/amen_default_args.csd
    :language: python
    :pyobject: drum_pattern_2

The score and audio:

.. literalinclude:: ../../examples/tutorials/amen/amen_default_args.csd
    :language: python
    :start-after: score.write(
    :end-before: score.pmap

Player Instruments
==================

Functions can also be used to generate gestures. In a sense these are another for of score instruments. The implemented in this example takes as its first argument the function in which we want to play.

Since kick(), snare(), and hat() all have identical signatures for their argument inputs, creating a player instrument that can treat them equally is iis easy.

For the argument, we can pass kick, snare, or hat. The duration of the phrase is passed in as the second arg. The duration of the indivual notes is arg 3. The number of beats to play through the lifespan of the instrument if arg 4. The start_amp and end_amp args do a linear envelop from the first and last nights, which is similiar to the classical score ramp function. And then there is one optional keyword arg for consistant tuning for all samples played by swell().

.. literalinclude:: ../../examples/tutorials/amen/amen_player.csd
    :language: python
    :pyobject: swell

Wrapping this up into a reuasable phrase:

.. literalinclude:: ../../examples/tutorials/amen/amen_player.csd
    :language: python
    :pyobject: intro

Invocation and audio:

Algorithmic Flair Drum Pattern
==============================

For the last drum pattern of this tutorial, we're going to create one that has a bit of an algorithmic flair for randomly generating kicks, snares, and hats.

For this pattern, we're going to use the random function from Python's random library, which needs to be imported::

    from random import random

The pattern is defiend as:

.. literalinclude:: ../../examples/tutorials/amen/amen_flair.csd
    :language: python
    :pyobject: drum_pattern_flair

This pattern extends drum_pattern() by calling it first. If any chages are ever made to drum_pattern(), than drum_pattern_flair() would also reflect these changes.

The rest of the pattern works like this. Eight different start times, in beats, are placed in a list. A list of score instrument functions is also created. As a way to increase the probability that a hat() will play, it has been added to this list three times.

It then iterates through the times list. For each of these predeterimined potential start times, it checks a randomly generated number against the input argument r. If the number generated by random() is less than r then a new event is created.

The cue() object is set to the current value of variable time. The choice() functions chooses either kick, snare, hat, hat, or hat. Then the event is created, with a random amplitude in the range os 0.125 and 0.875.

The end result is something common in many drum 'n' bass tracks in which is sounds as if percussional elements were generated at random, but still has the familiar kick and snare pattern.

.. literalinclude:: ../../examples/tutorials/amen/amen_flair.csd
    :language: python
    :start-after: score.write(
    :end-before: score.pmap

Form With Functions
===================

And finally, a musical example with all the pieces put together. Looking at this code, what do you think the form of the compostion is? 

.. literalinclude:: ../../examples/tutorials/amen/amen_form.csd
    :language: python
    :start-after: score.write(
    :end-before: score.pmap

**********
Conclusion
**********

So yeah, that's it.


.. rubric:: Footnotes

.. [#michaeljnelson] The MST3K guy
.. [#amen] Amen break description. Everything from N.W.A. to the Power Puff Girls
.. [#trashy] Trashy is a good thing in the right context.
.. [#tracker] Trackers are the bee's knees
.. [#dnb] Drum'n'bass beat
.. [#snozberry] Who's every heard of a snozberry?
.. [#fluxcapacitor] BTTF
.. [#adventuretime] Episode 3 Season 1
.. [#darksideofthemoon] Which is which
