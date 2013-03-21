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
        self.beat_map = {}
        self._last_measure = 0
        self._last_resolution = 0
        self._create_map(_meter_map)

    def _create_map(self, _meter_map):
        resolution = self._resolution((4, 4))
        measure = 2
        beats = 0
        self.beat_map.update({1: beats})
        print 'update ', 1, beats

        for k, v in _meter_map.iteritems():
            print k, v
            while True:
                if measure > k:
                    resolution = self._resolution(v)

                beats += resolution
                self.beat_map.update({measure: beats})
                print 'update ', measure, beats
                measure += 1

                if measure > k:
                    break

        self._last_measure = sorted(_meter_map.keys())[-1]
        self._last_resolution = self._resolution(_meter_map[self._last_measure])
        #self._last_meaure = measures
        #print self._last_measure

    def _resolution(self, sig):
        return sig[1] / 4 * sig[0]
        
    def measure(self, m):
        if m in self.beat_map:
            return cue(self.beat_map[m])
        return cue((m - self._last_measure) * self._last_resolution +
                    self.beat_map[self._last_measure])


# Allow lead-in
# Multi-meters
# 
def measure(t):
    return cue((t - 1) * 4.0)

meter_map = {
    1: (4, 4),
    2: (3, 4),
    4: (4, 4)
}

m = MixedMeter(meter_map)

score('t 0 120')

for i in range(1, 8):
    with m.measure(i) as foo:
        print 'm', i, foo.now()


</CsScore>
</CsoundSynthesizer>
