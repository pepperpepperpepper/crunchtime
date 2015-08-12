#!/usr/bin/python2 
from lib.Renderer.Audio.Wavebender.Squarewave import RendererAudioWavebenderSquarewave

test = RendererAudioWavebenderSquarewave();
#test.sound_write(frequency=440.0, duration=5);
test.sound_write(frequency=435.05, duration=5);

#test.sound_write(frequency=261.63, duration=0.4);
#test.sound_write(frequency=294.33, duration=0.4);
#test.sound_write(frequency=327.03, duration=0.4);
#test.sound_write(frequency=435.05, duration=0.4);
