from lib.Tuning import Tuning
import math
#from lib.Tuning.EqualTemperament import TuningEqualTemperament
class TuningMidi(Tuning):
  def __init__(self, tonic_midi_note=69, **kwargs):
    self.tonic_midi_note = tonic_midi_note;
    super(TuningMidi, self).__init__(**kwargs) 
  def midi_note_to_frequency(self, midi_note): 
    if self.tuning == "equal_temperament":
      return math.pow(2,float((midi_note-69)/12.0)) * 440.0
    elif self.tuning == "just_intonation":
      basis = math.pow(2,float((self.tonic_midi_note - 69)/12.0)) * 440.0
      distance = midi_note - self.tonic_midi_note 
      oct_distance = distance % 12
      multipliers = [ 
        1.0/1.0,
        16.0/15.0,
        9.0/8.0,
        6.0/5.0,
        5.0/4.0,
        4.0/3.0,
        45.0/32.0,
        3.0/2.0,
        8.0/5.0,
        5.0/3.0,
        9.0/5.0,
        15.0/8.0,
      ]
      freq_val = basis * multipliers[oct_distance]
      
      relative_octave = float(math.floor(distance/12))
      if relative_octave and relative_octave > 0:
        freq_val *= relative_octave
      if relative_octave and relative_octave < 0:
        freq_val /= relative_octave
      if distance < 0:
        freq_val /= 2.0;
      return freq_val;
