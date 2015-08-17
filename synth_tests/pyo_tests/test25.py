#!/usr/bin/python2.7
from pyo import *
import mido
import re
output_filename =  "./rendered_mp3s/" + re.sub('\.py$', '.wav', __file__);
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename=output_filename, sampletype=0)
notes = Notein(poly=127, scale=1, mul=.5)
p = Port(notes['velocity'], .001, .5)
b = Sine(freq=notes['pitch'], mul=p).out()
c = Sine(freq=notes['pitch'] * 0.997, mul=p).out()
d = Sine(freq=notes['pitch'] * 1.005, mul=p).out()

output = mido.open_output()
output.send(mido.Message('note_on', note=60, velocity=64))
s.start()
