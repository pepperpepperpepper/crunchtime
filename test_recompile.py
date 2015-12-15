#!/usr/bin/python2 
import sys
sys.path.append('./lib')
from renderer.midi.file_ import File as MidiFile
from renderer.midi.filecollection import FileCollection as MidiFileCollection
midifile = MidiFile();
midifile.load_events(from_file="./rendered/1439631385.midi")
midifile_collection = MidiFileCollection();
midifile_collection.split_by_channel(midifile);


#print midifile.events
print midifile.midifile_out()
print midifile_collection.midifiles_out()
