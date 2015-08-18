#!/usr/bin/python2 
from lib.Renderer.Audio.Midi.File import RendererAudioMidiFile;
from lib.Renderer.Audio.Midi.FileCollection import RendererAudioMidiFileCollection
midifile = RendererAudioMidiFile();
midifile.load_events(from_file="./rendered/1439631385.midi")
midifile_collection = RendererAudioMidiFileCollection();
midifile_collection.split_by_channel(midifile);


#print midifile.events
print midifile.midifile_out()
print midifile_collection.midifiles_out()
