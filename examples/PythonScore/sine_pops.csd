<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 2
0dbfs = 1.0

instr 1
    p3 = p4     ; Time in seconds
    iamp = p5
    ifreq = p6
    ipan = p7

    a1 oscils iamp, ifreq, 0
    aleft, aright pan2 a1, ipan
    outs aleft, aright
endin

</CsInstruments>
<CsScore bin="python">

from csd.pysco import PythonScoreBin
from math import e
from math import log
from random import choice
from random import random
from random import uniform

def exprand(a, b):
    '''Returns a random value between a and b for
    exponential distribution.'''

    return a * e ** (log(b / float(a)) * random())

def sine_pops(start, dur, amp, freq_min, freq_max, density):
    '''Asynchronous single cycle sine wave event generator.

    Args:
        start: Start time of generator in beats.
        dur: Duration of generator.
        amp: Maximum amplitude of pops.
        freq_min: Minimum wavelength.
        freq_max: Maximum wavelength.
        denstity: Number of pops per beat.
    '''

    for i in xrange(int(density * dur)):
        time = uniform(start, start + dur)
        amplitude = uniform(0, amp)
        freq = exprand(freq_min, freq_max)
        duration = 1 / freq
        freq *= choice([1, -1])
        pan = random()
        score.i(1, time, 1, duration, amplitude, freq, pan)

score = PythonScoreBin()
sine_pops(0, 20, 0.5, 1000, 20000, 60)

</CsScore>
</CsoundSynthesizer>
