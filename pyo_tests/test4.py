from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename='../rendered/test_pyo.wav', sampletype=0)
s.setVerbosity(8) #debug
#s.gui()

lfd = Sine([.4,.3], mul=.2, add=.5)
a = SuperSaw(freq=[49,50], detune=lfd, bal=0.7, mul=0.2).out()

s.start()
