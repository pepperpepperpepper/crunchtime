#!/usr/bin/python2 
from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline_nb') 
s.recordOptions(dur=50, fileformat=0, filename="./example_synth.wav")
s.boot();
from random import uniform
import os
t = HarmTable([1, 0, 0, .2, 0, 0, 0, .1, 0, 0, .05])
amp = Fader(fadein=.05, fadeout=2, dur=4, mul=.05).play()
osc = Osc(t, freq=[uniform(350,360) for i in range(10)], mul=amp).out()
# Records an audio file called "example_synth.aif" in the home folder
rec = Record(osc, filename="./example_synth2.wav", fileformat=0, sampletype=1)
clean = Clean_objects(50, rec)
clean.start()
s.start()
