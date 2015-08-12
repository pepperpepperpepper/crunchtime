#!/usr/bin/python2.7
from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename='../../rendered/test_pyo.wav', sampletype=0)




wav = SquareTable()
env = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
met = Metro(.125, 8).play()
amp = TrigEnv(met, table=env, mul=.2)
pit = TrigXnoiseMidi(met, dist=4, x1=20, mrange=(48,84))
hertz = Snap(pit, choice=[0,2,3,5,7,8,10], scale=1)
a = Osc(table=wav, freq=hertz, phase=0, mul=amp).out()
s.start()
