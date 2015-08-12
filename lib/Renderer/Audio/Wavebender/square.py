#!/usr/bin/env python
import wavebender
from math import cos
import sys

f =open ("test.wav", 'wb');
square_wave = wavebender.square_wave(440.0, amplitude=0.1)
channels = ((square_wave,),)
duration = 2
samples = wavebender.compute_samples(channels, 44100 * duration * 1)
wavebender.write_wavefile(f, samples, 44100 * duration * 1, nchannels=1)
