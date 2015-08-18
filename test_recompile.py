#!/usr/bin/python2 
from lib.Renderer.Audio.Midi.File import RendererAudioMidiFile;
midifile = RendererAudioMidiFile("./rendered/1439631385.midi");
midifile.recompile(midifile.events)
