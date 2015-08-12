#!/usr/bin/python2.7
from pyo import *
import re
output_filename =  "./rendered_mp3s/" + re.sub('\.py$', '.wav', __file__);
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename=output_filename, sampletype=0)
dens = Expseg([(0,1),(5,50)], loop=True, exp=5, initToFirstVal=True).play()
m = Cloud(density=dens, poly=2).play()
tr = TrigRand(m, min=300, max=1000)
tr_p = Port(tr, risetime=0.001, falltime=0.001)
a = Sine(freq=tr, mul=0.2).out()
s.start()
