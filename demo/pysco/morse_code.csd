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

DIT = 1
DAH = 3
LETTER = 3
SPACE = 7

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
   
last = None
t = 0

score('''
f 1 0 512 7 0 50 1 155 1 101 -1 155 -1 50 0')
t 0 500
''')

# Process each letter in quote
for c in quote:
    if c in morse:
        # Space between letters and words
        if last == 'letter':
            t += LETTER
        elif last == 'space':
            t += SPACE

        # Write letter and morse code to score
        score('; ' + c + ' ' + morse[c])

        # Audio process letter
        for m in morse[c]:
            with cue(t): 
                if m == '.':
                    event_i(1, 0, DIT)
                    t += DIT
                elif m == '-':
                    event_i(1, 0, DAH)
                    t += DAH

        last = 'letter'

    # Blank space
    elif c == ' ':
        score('; SPACE')
        last = 'space'

</CsScore>
</CsoundSynthesizer>
