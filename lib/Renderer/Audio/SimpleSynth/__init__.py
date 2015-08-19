#!/usr/bin/python2.7 
from lib.Renderer.Audio import RendererAudio
import wave, struct, math
import random
import scipy.signal
import sys
from lib.Tuning.Midi import TuningMidi
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

  def sound_write(self, freq=[440.0,550.0], duration=1.0, volume=.4, rest=0, midi_tick=0):
    """duration is in seconds"""
    if not freq:
      return
    if type(freq) in [  int , float ]:
      freq = [ float(freq) ];
    freq = map(lambda f: f * 2.0, freq);
    if rest:
      freq = [0];
    amp_width = math.pow(math.pow(2.0, 8.0), self.sample_width)/2.0 - 1.0 ;
    samples_count = duration * self.sample_rate
    #this calculation allows for the synth to not oscillate 
    #when writing short sample frames
    if midi_tick:
      midi_tick *= samples_count;
    for i in range(int(midi_tick), int(midi_tick+samples_count)):
        value = 0.;
        for f in freq:
          if self.wavetype == "sawtooth":
            value += float(amp_width)*scipy.signal.sawtooth(f*math.pi*float(i)/float(self.sample_rate))
          elif self.wavetype == "square":
            value += float(amp_width)*scipy.signal.square(f*math.pi*float(i)/float(self.sample_rate))
          elif self.wavetype == "triangle":
            value += float(amp_width)*scipy.signal.triang(f*math.pi*float(i)/float(self.sample_rate))
          elif self.wavetype == "whitenoise":
            value += float(amp_width)* random.uniform(-1.0, 1.0)
          else:
            value += float(amp_width)*math.cos(f*math.pi*float(i)/float(self.sample_rate))
  
        value *= volume/len(freq)
        data = struct.pack('<h', int(value))
        self._wavefile_h.writeframesraw( data )

  def midi_stream_process(self, stream, division=384, tempo=25000, tuning=TuningMidi(tuning="equal_temperament")):
     self._current_tick = 0;
     self._current_notes = []
      
     
     
     tick_duration = float((1.0/float(division) * float(tempo))/100000.0)
     try: 
       while True:
         events = stream.next();
         self._current_tick += 1;
         
         for event in events:
           if event.get("Type") == "Note_on_c":
             if int(event.get("Velocity")): 
               self._current_notes.append(int(event.get("Note")))
               if self._verbose:
                 self.log_info("processing frequency data: {}".format(
                   map(lambda n: tuning.midi_note_to_frequency(n), self._current_notes)
                 ))
             else:
               try:
                 self._current_notes.remove(int(event.get("Note")))
               except Exception as e:
                 sys.stderr.write(str(e))
           elif event.get("Type") == "Note_off_c":
             self._current_notes.remove(int(event.get("Note")))
         self.sound_write(
           freq=map(lambda n: tuning.midi_note_to_frequency(n), self._current_notes),
           duration=tick_duration,
           midi_tick=self._current_tick
         )
     except StopIteration:
       pass 
     finally:
       del stream; 
       self.log_info("Wrote to {}".format(self.filename))


  def close(self):
    self._wavefile_h('')
    self._wavefile_h.close()
    
