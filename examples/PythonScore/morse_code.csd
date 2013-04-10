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
<CsScore bin="python">

from csd.pysco import PythonScore

def tone(duration):
    score.i(1, 0, duration)

score = PythonScore()

quote = '''
ALL COMPOSERS SHOULD BE AS LAZY AS POSSIBLE WHEN WRITING SCORES MAX V MATHEWS
'''

dur = {'.': 1, '-': 3, 'letter': 3, 'space': 7, 'none': 0}
morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'}
last = 'none'
time = 0

score.write('''
f 1 0 512 7 0 50 1 155 1 101 -1 155 -1 50 0)
t 0 500
''')

# Process each character in quote
for c in quote:
    # Letter
    if c in morse:
        # Rest
        time += dur[last]
        last = 'letter'

        # Morse
        for m in morse[c]:
            with score.cue(time): tone(dur[m])
            time += dur[m]

    # Space
    elif c == ' ':
        last = 'space'

score.end()

</CsScore>
</CsoundSynthesizer>
