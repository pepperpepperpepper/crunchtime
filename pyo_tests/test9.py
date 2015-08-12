
#!/usr/bin/python2.7
from pyo import *
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename='../rendered/test_pyo.wav', sampletype=0)

#ph = Phasor(freq=[7,8])
#tr = Between(ph, min=0, max=.25)
#amp = Port(tr, risetime=0.002, falltime=0.002, mul=.2)
#a = SineLoop(freq=[245,250], feedback=.1, mul=amp).out()



met = Metro(.125, poly=2).play()
mid = TrigChoice(met, choice=[60, 63, 67, 70], port=.005)
hz = MToF(mid)
syn = SineLoop(freq=hz, feedback=.07, mul=.2).out()
s.start()
