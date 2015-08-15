from lib.Tuning import Tuning
import math
#from lib.Tuning.EqualTemperament import TuningEqualTemperament
class TuningMidi(Tuning):
  def __init__(self, **kwargs):
    super(TuningMidi, self).__init__(**kwargs) 
  def midi_note_to_frequency(self, midi_note): 
    return math.pow(2,float((midi_note-69)/12.0)) * 440.0

