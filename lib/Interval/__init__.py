import sys
from lib.Alias.Interval import AliasInterval

class Interval(object):
  def error(self, m):
    sys.stderr.write("{}\n".format(m))
    sys.exit(1);

  def __init__(self, **kwargs):
    if "name" in kwargs:
      self.length = self._length_set_by_name(kwargs.get("name"))
    elif "length" in kwargs:
      self.length = kwargs.get("length")
    else:
      self.error("must define a length for the interval")
  
  def _length_set_by_name(self, name):
     print AliasInterval(name).value; sys.exit(0);

  def __len__(self):
    return self.length

