#!/usr/bin/python2.7
from pyo import *
import re
output_filename =  "./rendered_mp3s/" + re.sub('\.py$', '.wav', __file__);
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename=output_filename, sampletype=0)
l1 = [300, 350, 400, 450, 500, 550]
l2 = [300, 350, 450, 500, 550]
t = CosTable([(0,0), (50,1), (250,.3), (8191,0)])
met = Metro(time=.125, poly=2).play()
amp = TrigEnv(met, table=t, dur=.25, mul=.3)
it = Iter(met, choice=[l1, l2])
si = Sine(freq=it, mul=amp).out()
s.start()
