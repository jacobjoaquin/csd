<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 4410
ksmps = 10
nchnls = 1
0dbfs = 1.0

instr 1
    idur = p3   ; Duration

    kenv line 0.707, idur, 0       ; Line envelope
    a1 vco2 kenv, 440, 12, 0.5  ; Triangle wave
    out a1
endin

</CsInstruments>
<CsScore bin="./pysco.py">

morse = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'}
   
DIT = 1
DAH = 3
LETTER = 3
SPACE = 7

foo = 'The quick brown fox jumped over the lazy dog'
last = None
t = 0

# Pre-process string
pass

score('t 0 700')

for c in foo:
    c = c.upper()

    if c in morse:
        # Space between letters and words
        if last == 'letter':
            t += LETTER
        elif last == 'space':
            t += SPACE

        score('; ' + c + ' ' + morse[c])
        for m in morse[c]:
            with cue(t): 
                if m == '.':
                    event_i(1, 0, DIT, )
                    t += DIT
                elif m == '-':
                    event_i(1, 0, DAH)
                    t += DAH

        last = 'letter'

    elif c == ' ':
        score('; SPACE')
        last = 'space'

</CsScore>
</CsoundSynthesizer>
