from lib.PitchClassSet import PitchClassSet;
from lib.Interval import Interval
class Scale(PitchClassSet):
  def __init__(self, root, **kwargs):
    """add modes next...needs a find by name function"""
    self._SCALE_INTERVALS = {
      "minor_pentatonic" : [0,3,2,2,3],
      "major_pentatonic" : [0,2,2,3,2],
      "major" :            [0,2,2,1,2,2,2],
      "ionian" :            [0,2,2,1,2,2,2],
      "natural_minor" :    [0,2,1,2,2,1,2],
      "aeolian" :    [0,2,1,2,2,1,2],
      "melodic_minor" :    [0,2,1,2,2,2,2],
      "harmonic_minor" :    [0,2,1,2,2,1,3],
      "half_whole" :       [0,1,2,1,2,1,2,1],
      "whole_half" :       [0,2,1,2,1,2,1,2],
      "whole_tone" :       [0,2,2,2,2,2],
      "chromatic" :        [0,1,1,1,1,1,1,1,1,1,1]
    }
    if "name" in kwargs:
      if kwargs.get("name") not in self._SCALE_INTERVALS.keys():
        message = "Bad Scale Type:\n" + \
          "try one of these...\n" + \
          "\n".join(map(lambda x: "\t\"{}\"".format(x), self._SCALE_INTERVALS.keys()));
        self.error(message)
      intervals = map(lambda a: Interval(length=a), self._SCALE_INTERVALS.get(kwargs.get("name"))) 
      super(Scale, self).__init__(intervals, root)
    elif intervals in kwargs: 
      super(Scale, self).__init__(intervals, root)
    else:
      self.error("No set of intervals or scale name provided");
    self.notes = self.notes_all;

  def intervals_find_by_name(self, s):
    """account for modes as well"""
    pass
  
