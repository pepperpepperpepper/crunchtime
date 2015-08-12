
#!/usr/bin/python2.7
from pyo import *
import re
output_filename =  "./rendered_mp3s/" + re.sub('\.py$', '.wav', __file__);
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename=output_filename, sampletype=0)
cl = Cloud(density=20, poly=2).play()
ti = Timer(cl, cl)
# Minimum waiting time before a new trig
cp = Compare(ti, comp=.05, mode=">")
trig = cl * cp
amp = TrigEnv(trig, table=HannTable(), dur=.05, mul=.25)
freq = TrigChoice(trig, choice=[100,150,200,250,300,350,400])
a = LFO(freq=freq, type=2, mul=amp).out()
s.start()
