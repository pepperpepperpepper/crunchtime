#!/usr/bin/env python
import wavebender
from math import cos
import sys
from lib.Renderer import Renderer

class RendererAudioWavebender(Renderer):
  def __init__(self, nchannels=1, sample_width=2, sample_rate=44100.0, **kwargs): 
    super(RendererAudioWavebender, self).__init__(**kwargs) 
    self.sample_width = sample_width
    self.sample_rate = sample_rate
    self.nchannels = nchannels
    self.filename = self.filename_new("wav", filename=kwargs.get("filename",None));
    self.log_info("Wavebender writing to filename {}".format(self.filename))
    self._wavefile_h = open(self.filename, 'wb');

  def _samples_write(self, samples, duration):
    #wavebender.write_wavefile(f, samples, 44100 * duration * 1, nchannels=1)
    wavebender.write_wavefile(self._wavefile_h, samples, 
      self.sample_rate * duration * 1,
      nchannels=self.nchannels)

    


