import wavebender
from math import cos
import sys
from lib.Renderer.Audio.Wavebender import RendererAudioWavebender

class RendererAudioWavebenderSquarewave(RendererAudioWavebender):
  def __init__(self, nchannels=1, sample_width=2, sample_rate=44100.0, **kwargs): 
    super(RendererAudioWavebenderSquarewave, self).__init__(**kwargs) 
  def sound_write(self, frequency=440.0, duration=10.0, amplitude=0.1):
    square_wave = wavebender.square_wave(frequency, amplitude=amplitude);
    channels = ((square_wave,),)
    samples = wavebender.compute_samples(channels, 44100 * duration * 1)
    self._samples_write(samples, duration);



