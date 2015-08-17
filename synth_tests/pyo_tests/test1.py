#!/usr/bin/python2.7
from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline_nb').boot()
s.recordOptions(dur=30.0, fileformat=0, filename='../../rendered/test_pyo.wav', sampletype=0)
s.setVerbosity(8) #debug
a = Sine(mul=0.01, freq=[44,550], add=1).out()
#wav = SquareTable()
#env = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
#met = Metro(.125, 12).play()
#amp = TrigEnv(met, table=env, dur=1, mul=.1)
#pit = TrigXnoiseMidi(met, dist='loopseg', x1=20, scale=1, mrange=(48,84))
#out = Osc(table=wav, freq=pit, mul=amp).out()
s.start()

