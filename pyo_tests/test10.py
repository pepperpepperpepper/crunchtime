

#!/usr/bin/python2.7
from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename='../rendered/test_pyo.wav', sampletype=0)

#ph = Phasor(freq=[7,8])
#tr = Between(ph, min=0, max=.25)
#amp = Port(tr, risetime=0.002, falltime=0.002, mul=.2)
#a = SineLoop(freq=[245,250], feedback=.1, mul=amp).out()



met = Metro(.125, poly=2).play()
rnd = TrigRand(met, min=0, max=1, port=.005)
omlf = Sine(.5, mul=700, add=1000)
fr = Scale(rnd, inmin=0, inmax=1, outmin=250, outmax=omlf, exp=1)
amp = TrigEnv(met, table=HannTable(), dur=.25, mul=.2)
out = SineLoop(fr, feedback=.07, mul=amp).out()
s.start()
