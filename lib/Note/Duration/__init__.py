from abjad import Duration as abjadDuration
class NoteDuration(object):
  def __init__(self, **kwargs):
    if beats in kwargs and type(kwargs[beats]) == "int":
       self.beats = beats

  def __str__(self):
     return ('beats: {beats}\n'
    ).format(**self.__dict__)

  def as_abjad(self):
    return abjadDuration(beats) 
