#!/usr/bin/python2.7
import sys
sys.path.append('./lib')
from renderer.midi.stream import Stream as MidiStream
from renderer.midi.file_ import File as MidiFile 
from renderer.audio.simplesynth import SimpleSynth 
from tuning.midi import Midi as TuningMidi

file2 = MidiFile()
file2.load_events(from_file="../Think_of_Rain.midi");
stream2 = file2.stream 
events2 = stream2.make_event_stream();
synth2 = SimpleSynth(filename="just_intonation", wavetype="sine")
synth2.midi_stream_process(events2, tuning=TuningMidi(tuning="just_intonation", tonic_midi_note=77))

