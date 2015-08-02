from lib.PitchClassSet import PitchClassSet;
class Chord(PitchClassSet):
  def __init__(self, root, **kwargs):
    """add modes next...needs a find by name function"""
    self._SCALE_INTERVALS = {
      "major" : [0,3,2,2,3]
    }
    if "name" in kwargs:
      if kwargs.get("name") not in self._SCALE_INTERVALS.keys():
        message = "Bad Chord Type:\n" + \
          "try one of these...\n" + \
          "\n".join(map(lambda x: "\t\"{}\"".format(x), self._SCALE_INTERVALS.keys()));
        self.error(message)
      super(Chord, self).__init__(self._SCALE_INTERVALS.get(kwargs.get("name")), root)
    elif intervals in kwargs: 
      super(Chord, self).__init__(intervals, root)
    else:
      self.error("no set of intervals or scale name provided");

  def intervals_find_by_name(self, s):
    """account for modes as well"""
    pass
