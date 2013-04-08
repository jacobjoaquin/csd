###############################
Amen Break PythonScore Tutorial
###############################

By Jacob Joaquin

jacobjoaquin@gmail.com

************
Introduction
************

*"Y'all ready for this?"* - Michael J. Nelson [#michaeljnelson]_

PythonScore is a fully modular score environment for the Csound
unified CSD file. Unlike other alternative text-based score
environements, PythonScore is non-imposing and does its best to get
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

PythonScore is not meant as a full replacement of the classical
Csound score, but as an enhancement. Any and all existing classical
score commands still work, and PythonScore itself outputs classical
score code. Perhaps PythonScore should be thought as a user-friendly
higher level abstraction of the classic score.

PythonScore is still early in development, though the library of
use cases and examples is rapidly growing. And all from a single
developer, which will hopefully change soon. The secondary purpose
of this tutorial is to attract a small group of people to start
experimenting with this alternative Csound score environment, to
find out what works, what's easy and what's not, and to collect new
ideas for future upgrades. It is also the belief of the author that
once people have some hands-on experience, many of the advantages
of working with PythonScore will become obvious. Until then, it's
just the ramblings of one person's perspective.

Since PythonScore is under development, consider this tutorial a
living document, as it will be updated to keep up with any future
changes. Send questions, comments, and bugs to jacobjoaquin@gmail.com,
or write to the Csound Mailing List.

The Orchestra
=============

In order to bring focus to the enhanced set of features and
compositional techniques Python with the PythonScore module brings
to the score environment, every example uses the exact same orchestra
throughout the entirety of this tutorial. Let's take a look:

.. literalinclude:: ../../examples/tutorials/amen/amen_classic.csd
    :start-after: <CsInstruments
    :end-before: </CsInstruments

**Source:** :download:`amen_classic.csd <../../examples/tutorials/amen/amen_classic.csd>`

The orchestra contains only a single instrument, a basic sampler
with the Amen Break [#amen]_ as its only audio source. The instrument
includes support for three custom pfield inputs for amplitude, the
beat positional sample offset, and for tuning the sample. The fact
that this is only a very basic instrument is purposful as techniques
discussed in this tutorial will demonstrate that even simple
instruments can be greatly enhanced with using some of the new
techniques afforded by Python.

The output of this sampler has a very trashy [#trashy]_ quality to
it, and sounds like it was produced with a tracker [#tracker]_ such
as Fast Tracker II. [#ft2]_

The use of a drum loop is chosen for a very specific reason. The
ability to express occurances in time is a defining attribute of
PythonScore, and percussion-based events are great for honing in
on timing. *Do not get the wrong impression that PythonScore caters
to 4/4 drumm music, as this is far from the truth.*

The Python Interpreter
======================

Before diving into the tutorial, an introduction the the `Python
Interpreter <http://docs.python.org/2/tutorial/interpreter.html>`_
is in order as it a wonderful tool for quickly testing various
aspects of the Python language. This tutorial will occasionaly embed
examples using it as well.

Typically, the Python interpreter is used in the terminal, which
is invoked by typing "python"::

    Quorra ~ $ python

This starts an interactive Python session in which users can begin
entering various commands.

::

    >>> print 'hello world'
    hello world
    >>> 440 * 2 ** (-9 / 12.0)
    261.6255653005986
    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

The `CsoundQt <http://qutecsound.sourceforge.net/>`_ graphical front
end comes equipped with a Python console. There's also `IPython
<http://ipython.org/>`_ which supercharges the Python Interpreter
with a lot of great features for Python beginners and veterans
alike.

******************************
Classical Score to PythonScore
******************************

In this section, we'll walk you through some the basic
features of Python and PythonScore. The tutorial starts with a classical
Csound score, and adds new PythonScore idioums one by one until
the score as been fully translated. The end result is the new Python
score.

.. literalinclude:: ../../examples/tutorials/amen/amen_classic.csd
    :start-after: <CsScore
    :end-before: </CsScore>

**Source:** :download:`amen_classic.csd <../../examples/tutorials/amen/amen_classic.csd>`

The score code produces four measures of the same drum pattern. The
pattern itself is the classical drum 'n' bass. [#dnb]_

Upgrade
=======

Porting a classical score into the Python requires a few lines of
code to set up. First, set the argument of the CsScore bin utility
to "python". Then import PythonScore::

	from pysco import PythonScore

An object called ``score`` is instantiated from the ``PythonScore()``
class. Additionally, variable ``cue`` is created and points to the
``score.cue`` context manager. We'll go into details later as to
why. Classical Csound source code is entered into the ``score()``
object via the ``write()`` method. And last, add ``score.end()``
as the last statement in the score to tell PythonScore that it's
ready to generate the classical Csound score code and pass it to
Csound. The result is this new score::

.. literalinclude:: ../../examples/tutorials/amen/amen_upgrade.csd
    :language: python
    :start-after: </CsInstruments>
    :end-before: </CsoundSynthesizers>

**Source:** :download:`amen_upgrade.csd <../../examples/tutorials/amen/amen_upgrade.csd>`

If this worries you that you'll be required to throw out everything
you know about the classic Csound score, fear not as you can still
use it with the ``score()`` object virtually untouched, or in
combination with other Python features as you learn them.

Time is Relative
================

*"It's what makes time travel possible."* - Dr. Emmett Lathrop Brown
[#fluxcapacitor]_

For the most part, when events are entered into a classical Csound
score, the start times are in global beats. PythonScore changes
this with by introduction of the ``cue()`` object, a Python `context
manager
<http://docs.python.org/2/library/stdtypes.html#typecontextmanager>`_ for
moving the current postion time in the score. Like a needle on a
recored. All events entered into PythonScore are relative the current
positional value of ``cue()``.

::

    with cue(12):
        score('i 1 0 0.5 0.707 0 0')

While the start time value in pfield-2 is 0, this event will start
at 12 beats into the piece. This is because start time events are
processed to reflect the current position of the cue(). The output
looks like this:

::

    i 1 12 0.5 0.707 0 0

Remember when we set ``cue = score.cue`` earlier? This was done to
create a shorthand version to eliminate having to specify the full
score object and method.

As for translating the drum 'n' bass parts, each measure has been
split into its own chuck of events. The first event in measure 2
has been changed to 0.0, and the same goes for measures 3 and 4.
The ``cue()`` object allows the composer locally to the current
measure, rather than manually calculating the global time at all
times.

.. literalinclude:: ../../examples/tutorials/amen/amen_cue.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

**Source:** :download:`amen_cue.csd <../../examples/tutorials/amen/amen_cue.csd>`

There are of course many more benefits. For example, moving entire
sections of code is a fairly trivial process in PythonScore. Doing
the same in the classical score could require translating start
times down a long pfield-2 column. It is the assertion of the author
that this feature, and this feature alone, makes transitioning to
PythonScore more than worthwhile.

Measures
========

The drum 'n' bass score is in 4/4. While the cue() object allows
us to treat beats local to the current measure, the arguments for
the cue() are in absolute global time in the previous section. Out
of the box, PythonScore does not support measures. However, Python
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
to be multplied by 4. Testing the math in the Python Interpreter
with inputting 4::

    >>> def test_my_math(t):
    ...     return (t - 1) * 4.0
    ...
    >>> test_my_math(4)
    12.0

The value returned is 12, which is the starting time of the first
event in measure 4 in the original classical score. Applying measure()
to the PythonScore, were left with the following. Notice that the
comments have been factored out now that the code itself clearly
indicates what a measure is:

.. literalinclude:: ../../examples/tutorials/amen/amen_measure.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

**Source:** :download:`amen_measure.csd <../../examples/tutorials/amen/amen_measure.csd>`

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

**Source:** :download:`amen_i.csd <../../examples/tutorials/amen/amen_i.csd>`

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

**Source:** :download:`amen_nest.csd <../../examples/tutorials/amen/amen_nest.csd>`

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

Looking at the PythonScore code from the last example, there are
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

**Source:** :download:`amen_instr.csd <../../examples/tutorials/amen/amen_instr.csd>`

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

.. literalinclude:: ../../examples/tutorials/amen/amen_pattern.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

**Source:** :download:`amen_pattern.csd <../../examples/tutorials/amen/amen_pattern.csd>`

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
* Everything you can do with the classical score you can do in PythonScore. The opposite isn't true (not even close)

The score we're left with is fundamentally more readable than the original Csound score. The fact that drums are being played is much more obvious than in the original classical score.

Starting with the next section

*************************
Further Score Development
*************************

Python is an open-ended highly extensible language which allows
many new ways to developer a highly personalized score environment.
In the examples to come, new features and musical phrases are built
on top of the existing work covered in the previous examples. The
orchestra will remain unchanged, though the music will.

Looping Through Lists
=====================

A list is a Python container for storing various data, which may
include numbers, strings, other lists, functions, etc. And they
make a wonderful additional to the score environment. They're highly
versatile and time saving. This example is a list of integers::

    [1, 2, 3, 4]

A loop is created from a list with the ``for`` statment, as it will
iterate through each value. In the score as the ``for`` loop iterates
through the list, the ``m`` variable assumes the the value of the
current list item. This is shorthand for calling ``drum_pattern()``
for measures 1 through 4:

.. literalinclude:: ../../examples/tutorials/amen/amen_list.csd
    :language: python
    :start-after: score.write(
    :end-before: score.end

**Source:** :download:`amen_list.csd <../../examples/tutorials/amen/amen_list.csd>`

Range
=====

The Python ``range()`` generates lists of integers automatically
and is useful in a range of different contexts. Here are three
examples of lists generated with ``range()``::

    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> range(4, 8)
    [4, 5, 6, 7]
    >>> range(0, 32, 4)
    [0, 4, 8, 12, 16, 20, 24, 28]

Substituting that manually created list with ``range()`` leaves us
with this update to the loop in the score.

.. literalinclude:: ../../examples/tutorials/amen/amen_range.csd
    :language: python
    :start-after: score.write
    :end-before: score.end

**Source:** :download:`amen_range.csd <../../examples/tutorials/amen/amen_range.csd>`

Choice Variation
================

Python comes with the random module which includes the ``choice()``
function that returns a random value from a list. Prior to this
example, all kick and snare events use the sample from the Amen
break. Applied to the ``kick()`` and ``snare()`` score instruments,
these functions randomly choose samples from a fixed list of positions
in the drum loop.

The ``kick()`` function chooses from positions 0, 0.5, 4, and 4.5:

.. literalinclude:: ../../examples/tutorials/amen/amen_choice.csd
    :language: python
    :pyobject: kick

The ``snare()`` functions chooses from positions 1, 3, 5, and 7:

.. literalinclude:: ../../examples/tutorials/amen/amen_choice.csd
    :language: python
    :pyobject: snare

**Source:** :download:`amen_choice.csd <../../examples/tutorials/amen/amen_choice.csd>`

Hats
====

Once again, a new score instrument is created from a function by
repurposing the code used in ``kick()`` and ``snare()`` for a hihat:

.. literalinclude:: ../../examples/tutorials/amen/amen_hats.csd
    :language: python
    :pyobject: hat

A second drum pattern called ``drum_pattern_8th_hats()`` is created,
a variation on the original drum pattern. In fact, ``drum_pattern()``
is called right in this new function.

.. literalinclude:: ../../examples/tutorials/amen/amen_hats.csd
    :language: python
    :pyobject: drum_pattern_8th_hats

Both patterns are played side by side in the updated score:

.. literalinclude:: ../../examples/tutorials/amen/amen_hats.csd
    :language: python
    :start-after: score.write(
    :end-before: score.end()

**Source:** :download:`amen_hats.csd <../../examples/tutorials/amen/amen_hats.csd>`

Post Processing with pmap()
===========================

Any data entered into the ``score()`` object via the ``PythonScore``
``write()`` or ``i()`` methods can be treated as data and post-processed
with ``pmap()``. If you ran the last example multiple times, you
might have noticed the "samples out of range" warning. This can be
solved on fell swoop. The pmap() function takes the following input::

    pmap(event_type, instr, pfield, function, *args, **kwargs)

To avoid samples being played out of range, all the amplitudes in
the score must be lowered. Multiplying each pfield 4, the amplitude
input for the sampler, with a constant value will do this. First,
let's create a function that take two arguments, and returns the
product.

.. literalinclude:: ../../examples/tutorials/amen/amen_postprocess.csd
    :language: python
    :pyobject: multiply

The value of the pfield is passed in as the first arg, x, and 0.707
as y. Pfield 4 is replaced with the value returned by the multipy
function

.. literalinclude:: ../../examples/tutorials/amen/amen_postprocess.csd
    :language: python
    :start-after: cue = score.cue
    :end-before: </CsScore>

**Source:** :download:`amen_postprocess.csd <../../examples/tutorials/amen/amen_postprocess.csd>`

The pmap() function only works on data already in the score. For
this reason, the best place for most cases will be either after the
last even is created and/or at the very end of the score.

Pre-processing Events with p_callback()
=======================================

The p_callback() method is the pre-processing equivalent of pmap().
The p_callback() registers a function to use with a specific pfield
for a specific instrument, and manipulates data as it is entered
into the score.

As an example, two related set of p_callback()'s are created. The
first tunes all the drum events up a perfect 5th by altering the
pfield 6 column used for tuning the samples. Since changing the
pitch also affects the length of the sample, which in turn can cause
the more of the sample to bleed into the portion being played, a
second p_callback() modifies the duration by the inverse of the
perfect 5th.

.. literalinclude:: ../../examples/tutorials/amen/amen_preprocess.csd
    :language: python
    :start-after: cue = score.cue
    :end-before:  score.write(

Where these callbacks are placed matter. Typically it is good
practice to place p_callback() functions before any events are
placed in the score. In this example, these are placed just prior
to the first write to the ``score()``.

.. literalinclude:: ../../examples/tutorials/amen/amen_preprocess.csd
    :language: python
    :start-after: cue = score.cue
    :end-before:  </CsScore

**Source:** :download:`amen_preprocess.csd <../../examples/tutorials/amen/amen_preprocess.csd>`

Transpose
=========

The perfect 5th ratio was hard coded into the last example, but
transposing data is something that is useful enough that it's worth
taking the time to consolidate it into a reusable function.

The ``tranpose()`` function accepts two args, one which is required
and a second default value. The first arg is the value in halfsteps
in which to transpose. Without a second arg, it outputs a transposition
ratio. If the second arg is supplied, then it will apply the
transposition ratio to this and return the output.

.. literalinclude:: ../../examples/tutorials/amen/amen_transpose.csd
    :language: python
    :pyobject: transpose

The ``score.p_callback()`` calls are refectored using this new funtion.

.. literalinclude:: ../../examples/tutorials/amen/amen_transpose.csd
    :language: python
    :start-after: cue = score.cue
    :end-before: score.write(

**Source:** :download:`amen_transpose.csd <../../examples/tutorials/amen/amen_transpose.csd>`

Default Arguments
=================

Earlier in the tutorial when ``kick()``, ``snare()``, and ``hat()``
were created the instr number, start time, duration, amplitude,
sample position offset, and tuning were factored out of the interface.
Three of these are put back in as optional arguments: duration,
amplitude, and tuning. Since these are optional arguments, we can
continue using the existing short form. Here are the updated score
instruments:

.. literalinclude:: ../../examples/tutorials/amen/amen_default_args.csd
    :language: python
    :start-after: return value * 2 **
    :end-before: drum_pattern

A new pattern is created that simple plays four kicks on the beat
transposed down a perfect fourth.

.. literalinclude:: ../../examples/tutorials/amen/amen_default_args.csd
    :language: python
    :pyobject: drum_pattern_2

Here is ``drum_pattern_2()`` tested in context with two other
patterns:

.. literalinclude:: ../../examples/tutorials/amen/amen_default_args.csd
    :language: python
    :start-after: score.write(
    :end-before: score.pmap

**Source:** :download:`amen_default_args.csd <../../examples/tutorials/amen/amen_default_args.csd>`

Player Instruments
==================

Python functions can accept other functions as arguments. This is
taken advantage of in this example as we create a generic player
instrument that accepts either ``kick()``, ``snare()``, or ``hat()``
as its first argument, then plays the passed score instrument based
on the the proceeding arguments. This is possible since our score
instruments have identical interfaces.

In addition to the instrument to play, here is a description of the
rest of the args in order:

	* The duration of that phrase in beats.
	* The duration of the individual instrument events.
	* The number of beats to play through the lifespan of the player.
	* The amplitude of the first note.
	* The amplitude of the target last note.
	* Optional arg for tuning.

The player instrument is named ``swell()`` as it was originally
envisioned as way to play instruments with ramped amplitudes:

.. literalinclude:: ../../examples/tutorials/amen/amen_player.csd
    :language: python
    :pyobject: swell

Here is a new pattern that utilizes the new player instrument:

.. literalinclude:: ../../examples/tutorials/amen/amen_player.csd
    :language: python
    :pyobject: intro

**Source:** :download:`amen_player.csd <../../examples/tutorials/amen/amen_player.csd>`

Algorithmic Flair
=================

*"All right? There's my flair! Okay? And this is me expressing myself, okay?"* - Joanna, Office Space [#officespace]_

For the last drum pattern of this tutorial, we're going to create
one that has a bit of an algorithmic flair for randomly generating
kicks, snares, and hats. For this pattern, we're going to use the
random function from Python's random module, which is imported near
the top of the score::

    from random import random

The new pattern is called ``drum_pattern_flair()`` and looks like
this:

.. literalinclude:: ../../examples/tutorials/amen/amen_flair.csd
    :language: python
    :pyobject: drum_pattern_flair

The pattern excepts an optional argument ``r`` that determines the
odds of a note being randomly generated. If ``r`` is 0, then there
is no chance that extra notes will be played. When ``r`` is set to
1, the it'll generate an event every chance it gets.

The pattern uses the original ``drum_pattern()`` created earlier,
and then continues with some programming logic to add a bit of
algorithmic flair to it. A list is created with eight different
start times (in beats). A second list containing a list of score
instruments are created. Only one kick and snare are added, but
includes hat three times to increase the odds that this will be
chosen.

Using the ``for`` loop, the program iterates through each value in
list ``times``. It does a comparison to a randomly generated number
for each. If the random number is less than ``r``, then score
instrument is generated for the current value of ``time``. The
``cue()`` is set to the current value of variable ``time``. The
``choice()`` functions then chooses either kick, snare, hat, hat,
or hat. Then the event is created, with a random amplitude in the
range os 0.125 and 0.875.

The end result is the drum 'n' bass pattern as its foundatin, but
with a random extra samples.

.. literalinclude:: ../../examples/tutorials/amen/amen_flair.csd
    :language: python
    :start-after: score.write(
    :end-before: score.pmap

**Source:** :download:`amen_flair.csd <../../examples/tutorials/amen/amen_flair.csd>`

Form With Functions
===================

In this final example, rather adding a feature we're going to make
a point about readability. Look at this snippet of code from the
final score and see if you can figure out the form?

.. literalinclude:: ../../examples/tutorials/amen/amen_form.csd
    :language: python
    :start-after: score.write(
    :end-before: score.pmap

Granted, not all scores are built the same, and Python definitely
allows the creation of some horrendous code. Though the code can
also be used to bring greater clarity to the score.

**Source:** :download:`amen_form.csd <../../examples/tutorials/amen/amen_form.csd>`

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
.. [#officespace] Flair
