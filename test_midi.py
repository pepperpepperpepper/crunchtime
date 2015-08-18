#!/usr/bin/python2.7
from lib.Renderer.Midi.Stream import RendererMidiStream
from lib.Renderer.Audio.SimpleSynth import RendererSimpleSynth 
from lib.Tuning.Midi import TuningMidi
#stream = RendererMidiStream.from_file("./rendered/1439631385.midi")
#events = stream.make_event_stream();
#print events.next()
#print stream.tempo
#print stream.division
#synth = RendererAudioSimpleSynth(filename="1439631385_just_intonation", )
#synth.midi_stream_process(events, tuning=TuningMidi(tuning="just_intonation", tonic_midi_note=77))
#synth.midi_stream_process(events )

#stream1 = RendererMidiStream.from_file("./rendered/equal_temperament.mid")
stream2 = RendererMidiStream.from_file("./rendered/just_intonation.mid")
#events1 = stream1.make_event_stream();
events2 = stream2.make_event_stream();
#synth1 = RendererAudioSimpleSynth(filename="equal_temperament")
synth2 = RendererAudioSimpleSynth(filename="just_intonation")
#synth1.midi_stream_process(events1, tuning=TuningMidi())
synth2.midi_stream_process(events2, tuning=TuningMidi(tuning="just_intonation", tonic_midi_note=77))

# Tempo, 500000
#tempo is microseconds/quarter_note
#
#
#division is clock_pulses/quarter_note

