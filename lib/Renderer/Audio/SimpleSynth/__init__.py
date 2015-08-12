#!/usr/bin/python2.7 
from lib.Renderer.Audio import RendererAudio
import wave, struct, math
import scipy.signal
#http://blog.acipo.com/wave-generation-in-python/

class RendererAudioSimpleSynth(RendererAudio):
  def __init__(self, nchannels=1, sample_width=2, sample_rate=44100.0, wavetype="sine", **kwargs): 
    super(RendererAudioSimpleSynth, self).__init__(**kwargs) 
    self.sample_width = sample_width
    self.sample_rate = sample_rate
    self.nchannels = nchannels
    self.wavetype = wavetype
    self.filename = self.filename_new("wav",filename=kwargs.get("filename",None));
    self._wavefile_h = wave.open(self.filename, 'w');
    self._wavefile_h.setnchannels(self.nchannels)
    self._wavefile_h.setsampwidth(self.sample_width);
    self._wavefile_h.setframerate(self.sample_rate)

  def sound_write(self, freq=[440.0,550.0], duration=1.0, volume=.1, rest=0):
    if type(freq) in [  int , float ]:
      freq = [ float(freq) ];
    freq = map(lambda f: f * 2.0, freq);
    if rest:
      freq = [0];
    amp_width = math.pow(math.pow(2.0, 8.0), self.sample_width)/2.0 - 1.0 ;
    for i in range(int(duration * self.sample_rate)):
        value = 0.;
        for f in freq:
          if self.wavetype == "sawtooth":
            value += float(amp_width)*scipy.signal.sawtooth(f*math.pi*float(i)/float(self.sample_rate))
          elif self.wavetype == "square":
            value += float(amp_width)*scipy.signal.square(f*math.pi*float(i)/float(self.sample_rate))
          elif self.wavetype == "triangle":
            value += float(amp_width)*scipy.signal.triang(f*math.pi*float(i)/float(self.sample_rate))
          else:
            value += float(amp_width)*math.sin(f*math.pi*float(i)/float(self.sample_rate))
  
        value *= volume/len(freq)
        data = struct.pack('<h', int(value))
        self._wavefile_h.writeframesraw( data )
  def close(self):
    self._wavefile_h('')
    self._wavefile_h.close()
    
