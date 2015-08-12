
#!/usr/bin/python2.7
from pyo import *
import re
output_filename =  "./rendered_mp3s/" + re.sub('\.py$', '.wav', __file__);
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename=output_filename, sampletype=0)
a = Phasor(1)
b = Thresh(a, threshold=[0.25, 0.5, 0.66], dir=0)
t = LinTable([(0,0), (50,1), (250,.3), (8191,0)])
env = TrigEnv(b, table=t, dur=.5, mul=.3)
sine = Sine(freq=[500,600,700], mul=env).out()
s.start()
