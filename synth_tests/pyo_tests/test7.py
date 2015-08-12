#!/usr/bin/python2.7
from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename='../../rendered/test_pyo.wav', sampletype=0)
fr = Sig(value=400)
p = Port(fr, risetime=0.001, falltime=0.001)
a = SineLoop(freq=p, feedback=0.08, mul=.3).out()
b = SineLoop(freq=p*1.005, feedback=0.08, mul=.3).out(1)
def pick_new_freq():
    fr.value = random.randrange(300,601,50)
pat = Pattern(function=pick_new_freq, time=0.5).play()
s.start()
