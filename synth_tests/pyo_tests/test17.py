#!/usr/bin/python2.7
from pyo import *
import re
output_filename =  "./rendered_mp3s/" + re.sub('\.py$', '.wav', __file__);
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename=output_filename, sampletype=0)
t = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
beat = Euclide(time=.125, taps=16, onsets=[8,7], poly=1).play()
trmid = TrigXnoiseMidi(beat, dist=12, mrange=(60, 96))
trhz = Snap(trmid, choice=[0,2,3,5,7,8,10], scale=1)
tr2 = TrigEnv(beat, table=t, dur=beat['dur'], mul=beat['amp'])
a = Sine(freq=trhz, mul=tr2*0.3).out()
s.start()
