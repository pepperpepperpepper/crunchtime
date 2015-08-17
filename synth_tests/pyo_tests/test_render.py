import mido
from pyo import *
output_filename = "test_render.wav" 
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='jack') 
s.recordOptions(dur=50, fileformat=0, filename=output_filename, sampletype=0)

s.setMidiInputDevice(1)

#output = mido.open_output()
output = mido.open_output('Midi Through Port-0')
s.boot()
s.start()
notes = Notein(poly=100, scale=1, mul=.5)


#for message in mido.MidiFile("./rendered/1439631385.midi").play():
#  print message
#  output.send(message)
p = Port(notes['velocity'], .001, .5)
b = Sine(freq=notes['pitch'], mul=p).out()

#s.recstart(filename="test_render.wav")
s.noteout(80, 77, timestamp=0)
s.noteout(90, 77, timestamp=20)
#s.recstop();
#output.send(mido.Message('note_on', note=88, velocity=64))
