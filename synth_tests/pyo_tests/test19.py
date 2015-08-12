
#!/usr/bin/python2.7
from pyo import *
import re
output_filename =  "./rendered_mp3s/" + re.sub('\.py$', '.wav', __file__);
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename=output_filename, sampletype=0)
t = CosTable([(0,0), (50,1), (250,.3), (8191,0)])
met = Metro(time=.125, poly=2).play()
trig = Percent(met, percent=50)
amp = TrigEnv(trig, table=t, dur=.25, mul=.3)
fr = TrigRand(trig, min=400, max=1000)
freq = Port(fr, risetime=0.001, falltime=0.001)
a = Sine(freq=freq, mul=amp).out()
s.start()
