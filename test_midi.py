#!/usr/bin/python2.7
from lib.Renderer.Audio.Midi.Stream import RendererAudioMidiStream

stream = RendererAudioMidiStream.from_file("./rendered/1439244018.midi")
events = stream.make_event_stream();
print events.next()
print stream.tempo
print stream.division
# Tempo, 500000
#tempo is microseconds/quarter_note
#
#
#division is clock_pulses/quarter_note

