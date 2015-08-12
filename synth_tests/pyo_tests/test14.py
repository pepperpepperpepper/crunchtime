#!/usr/bin/python2.7
from pyo import *
import re
output_filename =  "./rendered_mp3s/" + re.sub('\.py$', '.wav', __file__);
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename=output_filename, sampletype=0)
t = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
a = XnoiseMidi(dist="loopseg", freq=[2, 3], x1=1, scale=1, mrange=(60,73))
b = Change(a)
amp = TrigEnv(b, table=t, dur=[.5,.333], mul=.3)
out = SineLoop(freq=a, feedback=.05, mul=amp).out()
s.start()
