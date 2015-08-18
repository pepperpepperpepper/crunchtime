#!/usr/bin/python2 
from lib.Renderer.Midi.File import RendererMidiFile;
from lib.Renderer.Midi.FileCollection import RendererMidiFileCollection
midifile = RendererMidiFile();
midifile.load_events(from_file="./rendered/1439631385.midi")
midifile_collection = RendererMidiFileCollection();
midifile_collection.split_by_channel(midifile);


#print midifile.events
print midifile.midifile_out()
print midifile_collection.midifiles_out()
