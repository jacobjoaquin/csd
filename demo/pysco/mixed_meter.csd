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
    def __init__(self, _meter_map):
        self._beat_map = {}
        self._last_measure = 0
        self._last_resolution = 0
        self._create_map(_meter_map)

    def _create_map(self, _meter_map):
        resolution = self._resolution((4, 4))
        measure = 1
        beats = 0

        for k, v in sorted(_meter_map.iteritems()):
            print 'for', k, v, measure, resolution
            while True:
                print "\twhile", measure, resolution
                self._beat_map.update({measure: beats})

                if measure == k:
                    resolution = self._resolution(v)
                    beats += resolution
                    measure += 1
                    break

                beats += resolution
                measure += 1
                if measure >= 20:
                    break

        self._last_measure = sorted(_meter_map.keys())[-1]
        self._last_resolution = self._resolution(
                _meter_map[self._last_measure])

    def _resolution(self, sig):
        return sig[1] / 4.0 * sig[0]
        
    def measure(self, m):
        if m in self._beat_map:
            return cue(self._beat_map[m])
        return cue((m - self._last_measure) * self._last_resolution +
                    self._beat_map[self._last_measure])

m = MixedMeter({
    1: (7, 4),
    5: (4, 4),
    9: (7, 4),
    13: (4, 4),
})

score('t 0 160')

# Prints to screen the measure and start time of measure in beats
for i in range(1, 17):
    with m.measure(i) as foo:
        print 'm', i, foo.now()

import sys
#sys.exit(0)
for this_measure in range(1, 5):
    with m.measure(this_measure):
        event_i(1, 0, 1, 0.707, 7.02)
        event_i(1, 1, 1, 0.707, 6.11)
        event_i(1, 2, 1, 0.707, 6.11)
        event_i(1, 3, 1, 0.707, 6.11)
        event_i(1, 4, 1, 0.707, 6.11)
        event_i(1, 5, 1, 0.707, 6.11)
        event_i(1, 6, 1, 0.707, 6.11)

for this_measure in range(5, 9):
    with m.measure(this_measure):
        event_i(1, 0, 1, 0.707, 7.07)
        event_i(1, 1, 1, 0.707, 7.04)
        event_i(1, 2, 1, 0.707, 7.04)
        event_i(1, 3, 1, 0.707, 7.04)

for this_measure in range(9, 13):
    with m.measure(this_measure):
        event_i(1, 0, 1, 0.707, 7.02)
        event_i(1, 1, 1, 0.707, 6.11)
        event_i(1, 2, 1, 0.707, 6.11)
        event_i(1, 3, 1, 0.707, 6.11)
        event_i(1, 4, 1, 0.707, 6.11)
        event_i(1, 5, 1, 0.707, 6.11)
        event_i(1, 6, 1, 0.707, 6.11)

for this_measure in range(13, 17):
    with m.measure(this_measure):
        event_i(1, 0, 1, 0.707, 7.07)
        event_i(1, 1, 1, 0.707, 7.04)
        event_i(1, 2, 1, 0.707, 7.04)
        event_i(1, 3, 1, 0.707, 7.04)
</CsScore>
</CsoundSynthesizer>
