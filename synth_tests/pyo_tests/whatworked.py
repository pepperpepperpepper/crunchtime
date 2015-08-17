#!/usr/bin/python2.7 
from pyo import *
import mido
import time
output_filename = "test_render.wav" #made no difference
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='jack')
s.recordOptions(dur=50, fileformat=0, filename=output_filename, sampletype=0) #made no difference
#output = mido.open_output()
output = mido.open_output('Midi Through Port-0')
time.sleep(3)
s.boot()
s.start()
notes = Notein(poly=100, scale=1, mul=.5)
p = Port(notes['velocity'], .001, .5)
b = Sine(freq=notes['pitch'], mul=p).out()
rec = Record(osc, filename="./example_synth2.wav", fileformat=0, sampletype=1) #worked
clean = Clean_objects(50, rec)
clean.start()
#midi notes sent here
output.send(mido.Message('note_on', note=99, velocity=22))
output.send(mido.Message('note_on', note=77, velocity=22))
rec.stop()
clean.stop()
s.shutdown()

