<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 1
0dbfs = 1.0

instr 1
    a1 line 0.707, p3, 0
    a2 oscil a1, 478.8, 1
    out a2
endin

</CsInstruments>
<CsScore bin="./pysco.py">

quote = 'ALL COMPOSERS SHOULD BE AS LAZY AS POSSIBLE WHEN WRITING SCORES MAX V MATHEWS'

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

dur = {'.': 1, '-': 3, 'dit': 1, 'dah': 3, 'letter': 3, 'space': 7, 'none': 0}
last = 'none'
t = 0

score('f 1 0 512 7 0 50 1 155 1 101 -1 155 -1 50 0')
score('t 0 500')

# Process each character in quote
for c in quote:
    # Letter
    if c in morse:
        # Rest
        t += dur[last]
        last = 'letter'

        # Convert to morse
        for m in morse[c]:
            event_i(1, t, dur[m])
            t += dur[m]

    # Space
    elif c == ' ':
        last = 'space'

</CsScore>
</CsoundSynthesizer>
