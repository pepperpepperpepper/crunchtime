#!/usr/bin/python2.7
from lib.Renderer.Audio.Midi.Stream import RendererAudioMidiStream
from lib.Renderer.Audio.SimpleSynth import RendererAudioSimpleSynth 
from lib.Tuning.Midi import TuningMidi
stream = RendererAudioMidiStream.from_file("./rendered/1439631385.midi")
events = stream.make_event_stream();
print events.next()
print stream.tempo
print stream.division
synth = RendererAudioSimpleSynth(filename="1439631385_equal_temperament")
#synth.midi_stream_process(events, tuning=TuningMidi(tuning="just_intonation", tonic_midi_note=77))
synth.midi_stream_process(events )


# Tempo, 500000
#tempo is microseconds/quarter_note
#
#
#division is clock_pulses/quarter_note

