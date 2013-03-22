<CsoundSynthesizer>
<CsInstruments>
sr = 44100
kr = 44100
ksmps = 1
nchnls = 1
0dbfs = 1.0

instr 1
    idur = p3          ; Duration
    iamp = p4          ; Amplitude
    ipch = cpspch(p5)  ; Pitch

    kenv line iamp, idur, 0      ; Line envelope
    a1 vco2 kenv, ipch, 12, 0.5  ; Triangle wave
    out a1
endin

</CsInstruments>
<CsScore bin="python pysco.py">

class MixedMeter:
    def __init__(self, meters):
        self._beat_map = {}
        self._tail = 0
        self._res = 0
        self._create_map(meters)

    def _create_map(self, meters):
        resolution = self._resolution((4, 4))
        measure = 1
        beats = 0

        for k, v in sorted(meters.iteritems()):
            while True:
                self._beat_map.update({measure: beats})

                if measure == k:
                    resolution = self._resolution(v)
                    beats += resolution
                    measure += 1
                    break

                beats += resolution
                measure += 1

        self._tail = max(meters.keys())
        self._res = resolution

    def _resolution(self, sig):
        return 4.0 / sig[1] * sig[0]
        
    def measure(self, m):
        return cue(self._beat_map.get(m,
            (m - self._tail) * self._res + self._beat_map[self._tail]))

m = MixedMeter({
    1: (3, 4),
    5: (4, 4),
    9: (7, 4),
    13: (6, 8),
})

score('t 0 160')

# Measures 1 - 4 in 3/4
for this_measure in range(1, 5):
    with m.measure(this_measure):
        event_i(1, 0, 1, 0.707, 7.02)
        event_i(1, 1, 1, 0.707, 6.11)
        event_i(1, 2, 1, 0.707, 6.11)

# Measure 5 - 8 in 4/4
for this_measure in range(5, 9):
    with m.measure(this_measure):
        event_i(1, 0, 1, 0.707, 7.07)
        event_i(1, 1, 1, 0.707, 7.04)
        event_i(1, 2, 1, 0.707, 7.04)
        event_i(1, 3, 1, 0.707, 7.04)

# Measure 9 - 12 in 7/4
for this_measure in range(9, 13):
    with m.measure(this_measure):
        event_i(1, 0, 1, 0.707, 7.02)
        event_i(1, 1, 1, 0.707, 6.11)
        event_i(1, 2, 1, 0.707, 6.11)
        event_i(1, 3, 1, 0.707, 6.11)
        event_i(1, 4, 1, 0.707, 6.11)
        event_i(1, 5, 1, 0.707, 6.11)
        event_i(1, 6, 1, 0.707, 6.11)

# Measure 13 - 16 in 4/4
for this_measure in range(13, 17):
    with m.measure(this_measure):
        event_i(1, 0.0, 0.5, 0.707, 7.07)
        event_i(1, 0.5, 0.5, 0.707, 7.04)
        event_i(1, 1.0, 0.5, 0.707, 7.04)
        event_i(1, 1.5, 0.5, 0.707, 6.07)
        event_i(1, 2.0, 0.5, 0.707, 7.04)
        event_i(1, 2.5, 0.5, 0.707, 7.04)

</CsScore>
</CsoundSynthesizer>
