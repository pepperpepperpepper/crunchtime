#!/usr/bin/python2.7
from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename='../../rendered/test_pyo.wav', sampletype=0)
l = Linseg([(0,500),(.03,1000),(.1,700),(1,500),(2,500)], loop=True)
a = Sine(freq=l, mul=.3).mix(2).out()
# then call:
l.play()
s.start()
