#!/usr/bin/env python
'''Extracts a score from a Csound csd file.

.. warning:: This module currently prepends a newline to the beginning
   of the score.

Example::
    
    $ cat score_from_csd.csd | ./score_from_csd.py

Before::
    
    <CsoundSynthesizer>
    <CsInstruments>
    sr     = 44100
    kr     = 4410
    ksmps  = 10
    nchnls = 1
    
    0dbfs = 1.0
    
    instr 1
        iamp = p4
        ipitch = cpspch(p5)
        itable = p6
        
        asig oscil iamp, ipitch, itable, -1
        out asig
    endin
        
    </CsInstruments>
    <CsScore>
    f 1 0 8192 10 1  ; Sinewave
    
    i 1 0 0.125 1 8.00 1
    i 1 + .     . 8.07 .
    i 1 + .     . 8.04 .
    i 1 + .     . 8.00 .
    i 1 + .     . 8.07 .
    i 1 + .     . 8.04 .
    i 1 + .     . 8.00 .
    i 1 + .     . 8.07 .
    i 1 + .     . 8.04 .
    i 1 + .     . 8.00 .
    i 1 + .     . 8.07 .
    i 1 + .     . 8.04 .
    i 1 + .     . 8.00 .
    i 1 + .     . 8.07 .
    i 1 + .     . 8.04 .
    i 1 + .     . 8.00 .
    
    e
    </CsScore>
    </CsoundSynthesizer>

After::

    f 1 0 8192 10 1  ; Sinewave
    
    i 1 0 0.125 1 8.00 1
    i 1 + .     . 8.07 .
    i 1 + .     . 8.04 .
    i 1 + .     . 8.00 .
    i 1 + .     . 8.07 .
    i 1 + .     . 8.04 .
    i 1 + .     . 8.00 .
    i 1 + .     . 8.07 .
    i 1 + .     . 8.04 .
    i 1 + .     . 8.00 .
    i 1 + .     . 8.07 .
    i 1 + .     . 8.04 .
    i 1 + .     . 8.00 .
    i 1 + .     . 8.07 .
    i 1 + .     . 8.04 .
    i 1 + .     . 8.00 .
    
    e

'''

import sys

sys.path.append('../')  # Fix this.
import csd

if __name__ == '__main__':

    # Get input
    stdin = sys.stdin.readlines()
    s = ''.join(stdin)

    print csd.get_score(s),

