#!/usr/bin/python2.7
from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename='../../rendered/test_pyo.wav', sampletype=0)
fr = SigTo(value=200, time=0.5, init=200)
a = SineLoop(freq=fr, feedback=0.08, mul=.3).out()
b = SineLoop(freq=fr*1.005, feedback=0.08, mul=.3).out(1)
def pick_new_freq():
    fr.value = random.randrange(200,501,50)
pat = Pattern(function=pick_new_freq, time=1).play()
s.start()
