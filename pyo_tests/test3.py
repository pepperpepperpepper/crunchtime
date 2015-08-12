from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename='../rendered/test_pyo.wav', sampletype=0)
s.setVerbosity(8) #debug
#s.gui()

f = Phasor(freq=[1, 1.5], mul=1000, add=500)
sine = Sine(freq=f, mul=.2).out()
a = Noise(.1).mix(2).out()

s.start()
