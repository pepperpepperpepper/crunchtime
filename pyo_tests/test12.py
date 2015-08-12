#!/usr/bin/python2.7
from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename='../rendered/test_pyo.wav', sampletype=0)
a = SineLoop(freq=[200,300,400,500], feedback=0.05, mul=.1).out()
def event_0():
    a.freq=[200,300,400,500]
def event_1():
    a.freq=[300,400,450,600]
def event_2():
    a.freq=[150,375,450,525]
m = Metro(1).play()
c = Counter(m, min=0, max=3)
sc = Score(c)
s.start()
