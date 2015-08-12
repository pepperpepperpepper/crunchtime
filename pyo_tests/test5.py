from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename='../rendered/test_pyo.wav', sampletype=0)
s.setVerbosity(8) #debug
#s.gui()

fa = Fader(fadein=.5, fadeout=.5, dur=.5, mul=.1)
aa = BrownNoise(mul=fa).mix(2).out()
def repeat_a():
    fa.play()
pat1 = Pattern(function=repeat_a, time=.2).play()

f = Adsr(attack=.01, decay=.9, sustain=.1, release=.1, dur=2, mul=.1)
a = BrownNoise(mul=f).mix(2).out()
def repeat():
    f.play()
pat = Pattern(function=repeat, time=2).play()

s.start()
