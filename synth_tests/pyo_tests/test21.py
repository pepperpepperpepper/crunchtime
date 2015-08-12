
#!/usr/bin/python2.7
from pyo import *
import re
output_filename =  "./rendered_mp3s/" + re.sub('\.py$', '.wav', __file__);
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename=output_filename, sampletype=0)
env = CosTable([(0,0),(300,1),(1000,.3),(8191,0)])
seq = Seq(time=.125, seq=[2,1,1,2], poly=2).play()
tr = TrigRand(seq, min=250, max=500, port=.005)
amp = TrigEnv(seq, table=env, dur=.25, mul=.25)
a = SineLoop(tr, feedback=0.07, mul=amp).out()
s.start()
