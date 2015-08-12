
#!/usr/bin/python2.7
from pyo import *
import re
output_filename =  "./rendered_mp3s/" + re.sub('\.py$', '.wav', __file__);
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename=output_filename, sampletype=0)
env = HannTable()
m = Metro(.125, poly=2).play()
te = TrigEnv(m, table=env, dur=.2, mul=.2)
c = Counter(m, min=0, max=4)
se = Select(c, 0)
tr = TrigRand(se, 400, 600)
a = Sine(freq=tr, mul=te).out()
s.start()
