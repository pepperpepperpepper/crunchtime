#!/usr/bin/python2 
from lib.Renderer.Audio.Midi.File import RendererAudioMidiFile;
midifile = RendererAudioMidiFile();
midifile.load_events(from_file="./rendered/1439631385.midi")

#print midifile.events
print midifile.midifile_out()
