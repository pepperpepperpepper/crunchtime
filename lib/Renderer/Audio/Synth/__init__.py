#!/usr/bin/python2.7 
from lib.Renderer import Renderer
import wave, struct, math

class RendererAudioSynth(Renderer):
  def __init__(self, nchannels=1, sample_width=2, sample_rate=44100.0, **kwargs): 
    super(RendererAudioSynth, self).__init__(**kwargs) 
    self.sample_width = sample_width
    self.sample_rate = sample_rate
    self.nchannels = nchannels
    self.filename = self.filename_new(filename=kwargs.get("filename",None));
    self._wavefile_h = wave.open(self.filename, 'w');
    self._wavefile_h.setnchannels(self.nchannels)
    self._wavefile_h.setsampwidth(self.sample_width);
    self._wavefile_h.setframerate(self.sample_rate)

  def sound_write(self, frequency=440.0, duration=1.0):
    amp_width = 2 ^ (self.sample_width * 8) - 1 ;
    for i in range(int(duration * self.sample_rate)):
        cos( freq * pi )
        value = int(amp_width*math.cos(frequency*math.pi*float(i)/float(self.sample_rate))) #ok these two lines are confusing me here
        data = struct.pack('<h', value)
        self._wavefile_h.writeframesraw( data )
  def close(self):
    self._wavefile_h('')
    self._wavefile_h.close()
    
