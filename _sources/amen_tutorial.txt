###############################
Amen Break PythonScore Tutorial
###############################

By Jacob Joaquin <jacobjoaquin@gmail.com>

*Updated April 8th, 2013*

************
Introduction
************

PythonScore is a fully modular score environment for the Csound
unified CSD file. Unlike other alternative text-based score
environments, PythonScore is non-imposing and does its best to get
out of the way rather than to impose a strict set of rules for
composition. Classical Csound score is fully supported, all of
Python 2.7 is available, and composers can pick and choose their
score tools *à la carte* as they see fit.

The purpose of this tutorial is to try and prove the merits of
using the Python language in favor of the classical Csound score.
The classical score is a fixed system while Python is a very mature
and highly extensible language with a vast collection of first and
third party modules. Despite being a general purpose language that
wasn't designed for music, Python is particularly well suited for
composition.

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

Files
=====

The Csound CSD files and amen break sample ship with the csd module in::

    /examples/tutorials/amen/

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
with the `Amen Break <http://en.wikipedia.org/wiki/Amen_break>`_
as its only audio source. The instrument includes support for three
custom pfield inputs for amplitude, the beat positional sample
offset, and for tuning the sample. The fact that this is only a
very basic instrument is purposeful as techniques discussed in this
tutorial will demonstrate that even simple instruments can be greatly
enhanced with using some of the new techniques afforded by Python.

The output of this sampler has a very trashy quality to it, and
sounds like it was produced with a `tracker
<http://en.wikipedia.org/wiki/Music_tracker>`_ such as `Fast Tracker
II <http://en.wikipedia.org/wiki/FastTracker_2>`_.

The use of a drum loop is chosen for a very specific reason. The
ability to express occurences in time is a defining attribute of
PythonScore, and percussion-based events are great for honing in
on timing. *Do not get the wrong impression that PythonScore caters
to 4/4 drum music, as this is far from the truth.*

The Python Interpreter
======================

Before diving into the tutorial, an introduction the the `Python
Interpreter <http://docs.python.org/2/tutorial/interpreter.html>`_
is in order as it a wonderful tool for quickly testing various
aspects of the Python language. This tutorial will occasionally embed
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
Csound score, and adds new PythonScore idioms one by one until
the score as been fully translated. The end result is the new Python
score.

.. literalinclude:: ../../examples/tutorials/amen/amen_classic.csd
    :start-after: <CsScore
    :end-before: </CsScore>

**Source:** :download:`amen_classic.csd <../../examples/tutorials/amen/amen_classic.csd>`

.. raw:: html

    <iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F86990916"></iframe>

The score code produces four measures of the same drum pattern. The
pattern itself is the classical `drum 'n' bass <http://en.wikipedia.org/wiki/Drum_and_bass>`_.

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
Csound. The result is this new score:

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

For the most part, when events are entered into a classical Csound
score, the start times are in global beats. PythonScore changes
this with by introduction of the ``cue()`` object, a Python `context
manager
<http://docs.python.org/2/library/stdtypes.html#typecontextmanager>`_ for
moving the current position time in the score. Like a needle on a
record. All events entered into PythonScore are relative the current
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

The drum 'n' bass score is in 4/4. While ``cue()`` allows us to
treat beats local to the current measure, the arguments for the
cue() are still in absolute global time. Out of the box, PythonScore
does not support measures. However, Python is highly extensible and
lets you *roll your own*. Implementing 4/4 measures is done by
`defining a new function
<http://docs.python.org/2/tutorial/controlflow.html#defining-functions>`_:

.. literalinclude:: ../../examples/tutorials/amen/amen_measure.csd
    :language: python
    :pyobject: measure

This two line custom function takes the measure number as its sole
argument and translates measure time to beat time, and returns an
instance of cue().

Let's focus little on the math. The global score starts at 0, but
measures start at 1. The is overcome with an offset of -1. In 4/4,
there are four beats per measure, which requires the offset value
to be multiplied by 4. Testing the math in the Python Interpreter
with inputting 4::

    >>> def test_measure(t):
    ...     return (t - 1) * 4.0
    ...
    >>> test_measure(4)
    12.0

Inputting 4 into our test the value returned is 12, which is the
starting time of the first event in measure 4 in the original
classical score. Applying ``measure()`` to the PythonScore, were
left with the following. Notice that the comments have been factored
out now that the code itself clearly indicates what a measure is:

.. literalinclude:: ../../examples/tutorials/amen/amen_measure.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

**Source:** :download:`amen_measure.csd <../../examples/tutorials/amen/amen_measure.csd>`

Instrument Event Function
=========================

The ``score.i()`` method is another way for entering in data into
the score. Instead of a string, it accepts any number of arguments
and constructs a valid classical score event string. For example::

    score.i(1, 0, 1, 0.707, 8.00)

Outputs::

    i 1 0 1 0.707 8.00

Replacing the calls to ``score.write()`` with the ``i()`` method in the Amen score, the
updated code looks like this:

.. literalinclude:: ../../examples/tutorials/amen/amen_i.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

**Source:** :download:`amen_i.csd <../../examples/tutorials/amen/amen_i.csd>`

Nesting Time
============

A ``with cue()`` statement can be placed inside a hierarchy of other
``with cue()`` statements. This allows composers to reset the
relative positional time to zero regardless of the current scope of
time by writing another ``with cue()`` statement: For example, this
is possible::

    with cue(32):
        with cue(4):
            with cue(1):
                score.i(1, 0, 1, 0.707, 0, 1)

Though the start time of the event is written as 0, the actual start
time of the event is 37, which is the accumulation of all the args
in the cue nesting hierarchy plus pfield-2: ``32 + 4 + 1 + 0``

The greater implication is that time can be completely decoupled
from events. In this version of the score the start times are moved
from the pfield-2 column to the the ``cue()``, and then set to 0.

.. literalinclude:: ../../examples/tutorials/amen/amen_nest.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

**Source:** :download:`amen_nest.csd <../../examples/tutorials/amen/amen_nest.csd>`

Score Instruments
=================

Composers can create named Python functions that call their
corresponding orchestra instruments. Furthermore, multiple functions
can be created for the same instrument, but with more specific
intent as to what the resultant behavior of the instrument is, like
a patch.

The sampler instrument in the orchestra is fairly simple and generic
in design. While the Amen Break loop is fixed, the instrument itself
has no knowledge of kicks or snares. It only accesses the part of
the sample denoted by the beat positional offset passed into pfield-5.

Looking at the PythonScore code from the last example, there are
only two unique calls to ``score.i()``, and even then all the
arguments are identical except for pfield-5::

    score.i(1, 0, 0.5, 0.707, 0, 1)
    score.i(1, 0, 0.5, 0.707, 1, 1)

The former plays a kick drum while the latter plays a snare. Though
looking at the code *who knows which is which and who is
who*. [#darksideofthemoon]_ This is because the classic Csound events
are more or less just data, and don't naturally signify what's
behind the data.

These statements are also unnecessarily long in Python, which makes
them ripe to for consolidation. Defining functions for the kick and
snare avoids the extra overhead by factoring out all the args.
Something is made possible by the ``cue()`` object.

.. literalinclude:: ../../examples/tutorials/amen/amen_instr.csd
    :language: python
    :start-after: return cue(
    :end-before: score =

An equally important benefit to this approach is that with proper
names, this technique creates code that is self documenting and
easier to read. If you type ``kick()`` it plays a kick. Type
``snare()`` it plays a snare. Type ``snozberry()`` it plays a
snozberry(). [#snozberry]_

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
a simple four notes drum 'n' bass pattern.

.. literalinclude:: ../../examples/tutorials/amen/amen_pattern.csd
    :language: python
    :pyobject: drum_pattern

These events will not be generated until the function is called.
For each measure, four lines of score instruments is replaced with
``drum_pattern()``.

.. literalinclude:: ../../examples/tutorials/amen/amen_pattern.csd
    :language: python
    :start-after: <CsScore
    :end-before: </CsScore>

**Source:** :download:`amen_pattern.csd <../../examples/tutorials/amen/amen_pattern.csd>`

Functions aren't limited to storing measures of data. Notes, licks,
phrases, bars, sections, scores, can all be placed inside a function.
Later when it's time to start arranging, musical patterns like these
can be more or less dropped into ``measure()`` blocks.

Interlude
=========

The score we're left with is fundamentally more expressive and more
readable than the original Csound score. Even if all the intricacies
of Python may still a mystery, reading through the code you should
be able to pick up on the instrumentation as well as seeing that
the score is divided into measures.

In the examples to come, new features and musical phrases are built
on top of the existing work covered in the previous examples. The
orchestra will remain unchanged, though the music will. Some of
these new idioms are more complex, so it worth playing with what
has be presented thus far. Though do read on even if you just skim
that material to get a sense as to what other compositional advantages
that Python brings to composing with code.

Looping Through Lists
=====================

A `Python list
<http://docs.python.org/2/library/functions.html?highlight=list#list>`_ is
a container for storing various data, which may include numbers,
strings, other lists, functions, etc. And they make a wonderful
additional to the score environment. They're highly versatile and
time saving. This example is a list of integers::

    [1, 2, 3, 4]

A loop is created from a list with the `for
<http://docs.python.org/2/tutorial/controlflow.html#for-statements>`_
statement, as it will iterate through each value. In the score as
the ``for`` loop iterates through the list, the ``m`` variable
assumes the the value of the current list item. This is shorthand
for calling ``drum_pattern()`` for measures 1 through 4:

.. literalinclude:: ../../examples/tutorials/amen/amen_list.csd
    :language: python
    :start-after: score.write(
    :end-before: score.end

**Source:** :download:`amen_list.csd <../../examples/tutorials/amen/amen_list.csd>`

Range
=====

The Python `range()
<http://docs.python.org/2/tutorial/controlflow.html#the-range-function>`_
generates lists of integers automatically and is useful in a range
of different contexts. Here are three examples of lists generated
with ``range()``::

    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> range(4, 8)
    [4, 5, 6, 7]
    >>> range(0, 32, 4)
    [0, 4, 8, 12, 16, 20, 24, 28]

Substituting that manually created list with ``range()`` leaves us
with this score update.

.. literalinclude:: ../../examples/tutorials/amen/amen_range.csd
    :language: python
    :start-after: score.write
    :end-before: score.end

**Source:** :download:`amen_range.csd <../../examples/tutorials/amen/amen_range.csd>`

Choice Variation
================

Python comes with the `random module
<http://docs.python.org/2/library/random.html>`_ which includes the
`choice() <http://docs.python.org/2/library/random.html#random.choice>`_
function that returns a random value from a list. Prior to this
example, all kick and snare events use the same sample from the
Amen break. Applied to the ``kick()`` and ``snare()`` score
instruments, these functions randomly choose samples from a fixed
list of beat positional offsets in the drum loop.

The ``kick()`` function chooses from positions 0, 0.5, 4, and 4.5:

.. literalinclude:: ../../examples/tutorials/amen/amen_choice.csd
    :language: python
    :pyobject: kick

The ``snare()`` functions chooses from positions 1, 3, 5, and 7:

.. literalinclude:: ../../examples/tutorials/amen/amen_choice.csd
    :language: python
    :pyobject: snare

**Source:** :download:`amen_choice.csd <../../examples/tutorials/amen/amen_choice.csd>`

.. raw:: html

    <iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F86990915"></iframe>

Hats
====

Once again, a new score instrument is created from a function by
re purposing the code used in ``kick()`` and ``snare()`` for a hihat:

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

.. raw:: html

    <iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F86990921"></iframe>

Post-Processing Score Data
==========================

Any data entered into the ``score()`` object via the ``PythonScore``
``write()`` or ``i()`` methods can be treated as data and post-processed
with ``pmap()``. If you ran the last example multiple times, you
might have noticed the *"samples out of range"* warning. This can
be solved in fell swoop. The ``pmap()`` method takes the following
input::

    pmap(event_type, instr, pfield, function, *args, **kwargs)

To avoid samples being played out of range, all the amplitudes in
the score are lowered. Pfield-4 is designated for amplitude, and
each value in the pfield-4 column multiplied by a constant value.
The process uses a custom definition for returning the product of
two numbers:

.. literalinclude:: ../../examples/tutorials/amen/amen_postprocess.csd
    :language: python
    :pyobject: multiply

The value of the pfield is passed in as the first arg `x` and 0.707
as `y`. Pfield-4 is replaced with the value returned by the `multiply()`
function

.. literalinclude:: ../../examples/tutorials/amen/amen_postprocess.csd
    :language: python
    :start-after: cue = score.cue
    :end-before: </CsScore>

**Source:** :download:`amen_postprocess.csd <../../examples/tutorials/amen/amen_postprocess.csd>`

.. raw:: html

    <iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F86990923"></iframe>

The `pmap()` function only works on data already in the score. For
this reason, the best place for most cases will be either after the
last event is generated and/or just before ``score.end()`` is called.

Pre-Processing Score Data
=========================

The ``p_callback()`` method is the pre-processing equivalent of ``pmap()``.
The ``p_callback()`` method registers a function to use with a specific pfield
for a specific instrument, and manipulates data as it is entered
into the score.

As an example, two related set of ``p_callback()`` functions are
created. The first tunes all the drum events up a perfect 5th by
altering the pfield-6 column used for tuning the samples. Since
changing the pitch also affects the length of the sample, which in
turn can cause the more of the sample to bleed into the next sample
in the audio file, a second ``p_callback()`` modifies the duration
by the inverse of a perfect 5th.

.. literalinclude:: ../../examples/tutorials/amen/amen_preprocess.csd
    :language: python
    :start-after: cue = score.cue
    :end-before:  score.write(

Where these callbacks are placed matter. Typically it is good
practice to place ``p_callback()`` functions before any events are
placed in the score. In this example, these are placed just prior
to the first write to the ``score()``.

.. literalinclude:: ../../examples/tutorials/amen/amen_preprocess.csd
    :language: python
    :start-after: cue = score.cue
    :end-before:  </CsScore

**Source:** :download:`amen_preprocess.csd <../../examples/tutorials/amen/amen_preprocess.csd>`

.. raw:: html

    <iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F86990924"></iframe>

Transpose
=========

The perfect 5th ratio was hard coded into the last example, but
transposing data is something that is useful enough that it's worth
taking the time to consolidate it into a reusable function.

The ``transpose()`` function accepts two args, one which is required
and a second optional default argument. The first arg is the value
in half steps in which to transpose. Without a second arg, it outputs
the ratio of transposition.  If the second arg is supplied, then
it will apply the transposition ratio to this before returning the
output.

.. literalinclude:: ../../examples/tutorials/amen/amen_transpose.csd
    :language: python
    :pyobject: transpose

The ``score.p_callback()`` calls are refactored using this new function.

.. literalinclude:: ../../examples/tutorials/amen/amen_transpose.csd
    :language: python
    :start-after: cue = score.cue
    :end-before: score.write(

**Source:** :download:`amen_transpose.csd <../../examples/tutorials/amen/amen_transpose.csd>`

Default Arguments
=================

Earlier in the tutorial when ``kick()``, ``snare()``, and ``hat()``
were created, the instr number, start time, duration, amplitude,
beat positional offset, and tuning were factored out of the interface.
Three of these are put back in as optional arguments: duration,
amplitude, and tuning. Since these are optional arguments, we can
continue using the existing short form. Here are the updated score
instruments:

.. literalinclude:: ../../examples/tutorials/amen/amen_default_args.csd
    :language: python
    :start-after: return value * 2 **
    :end-before: drum_pattern

A new pattern is created that plays four kicks on the beat transposed
down a perfect fourth.

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

.. raw:: html

    <iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F86990917"></iframe>

Player Instruments
==================

Python functions can accept other functions as arguments. This is
taken advantage of in this example as we create a generic player
instrument that accepts either ``kick``, ``snare``, or ``hat`` as
the first argument, then plays the passed score instrument based
on the the proceeding arguments. This is possible since our score
instruments have identical interfaces/signatures.

The player instrument is named ``swell()`` as it was originally
envisioned as way to play instruments with ramped amplitudes. Here
is a description of the rest of the arguments in order in which
they appear:

    * The duration of that phrase in beats.
    * The duration of the individual instrument events.
    * The number of beats to play through the lifespan of the player.
    * The amplitude of the first note.
    * The amplitude of the target last note.
    * Optional arg for tuning.

.. literalinclude:: ../../examples/tutorials/amen/amen_player.csd
    :language: python
    :pyobject: swell

Here is a new pattern that utilizes the new player instrument:

.. literalinclude:: ../../examples/tutorials/amen/amen_player.csd
    :language: python
    :pyobject: intro

**Source:** :download:`amen_player.csd <../../examples/tutorials/amen/amen_player.csd>`

.. raw:: html

    <iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F86990922"></iframe>

Algorithmic Flair
=================

For the last drum pattern of this tutorial, we're going to create
one that has a bit of an algorithmic flair for randomly generating
kicks, snares, and hats. For this pattern, we're going to use the
`random function
<http://docs.python.org/2/library/random.html#random.random>`_ from
Python's random module, which is imported near the top of the score::

    from random import random

The new pattern is called ``drum_pattern_flair()`` and looks like
this:

.. literalinclude:: ../../examples/tutorials/amen/amen_flair.csd
    :language: python
    :pyobject: drum_pattern_flair

The pattern excepts an optional argument ``r`` that determines the
odds of an event being randomly generated. If ``r`` is 0, then there
is no chance that extra notes will be played. When ``r`` is set to
1, it'll generate an event every chance it gets.

The pattern uses the original ``drum_pattern()`` created earlier,
and then continues with some programming logic to add a bit of
algorithmic flair to it. A list is created with eight different
start times (in beats). A second list containing a list of score
instruments is created; Only one kick and snare are added, but
includes hat three times to increase the odds that this will be
chosen.

Using the ``for`` loop, the program iterates through each value in
list ``times``. It does a comparison to a randomly generated number
for each. If the random number is less than ``r``, then a score
instrument is generated for the current value of ``time``. The
``cue()`` is set to the current value of variable ``time``. The
``choice()`` functions then chooses either kick, snare, hat, hat,
or hat. Then the event is created, with a random amplitude in the
range of 0.125 and 0.875.

The end result is the original drum pattern plus some extra random
notes, maybe.

.. literalinclude:: ../../examples/tutorials/amen/amen_flair.csd
    :language: python
    :start-after: score.write(
    :end-before: score.pmap

**Source:** :download:`amen_flair.csd <../../examples/tutorials/amen/amen_flair.csd>`

.. raw:: html

    <iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F86990918"></iframe>

Form With Functions
===================

In this final example, rather adding a feature we're going to make
a point about readability. Look at this snippet of code from the
final score and see if you can figure out the form?

.. literalinclude:: ../../examples/tutorials/amen/amen_form.csd
    :language: python
    :start-after: score.write(
    :end-before: score.pmap

**Source:** :download:`amen_form.csd <../../examples/tutorials/amen/amen_form.csd>`

.. raw:: html

    <iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F86990919"></iframe>

Granted, not all scores are built the same, and Python definitely
allows the creation of some horrendous code. Though the code can
also be used to bring greater clarity to the score.

.. rubric:: Footnotes

.. [#darksideofthemoon] Pink Floyd, "Us and Them", The Dark Side of the Moon, 1973
.. [#snozberry] Willy Wonka and the Chocolate Factory, movie, 1971
