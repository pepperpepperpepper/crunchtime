#!/usr/bin/python2 
import sys 
sys.path.append("../");

from lib.Renderer.Audio.SimpleSynth import RendererAudioSimpleSynth

synth = RendererAudioSimpleSynth();
synth.log_info(synth.filename);
synth.sound_write(freq=[440.0, 880.0], duration=2);
synth.sound_write(freq=261.63, duration=0.4, rest=1);
synth.sound_write(freq=294.33, duration=0.4);
#test.sound_write(freq=327.03, duration=0.4);
#test.sound_write(freq=435.05, duration=0.4);
