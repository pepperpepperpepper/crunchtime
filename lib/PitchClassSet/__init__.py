import sys
class PitchClassSet(object):
  def error(self, m):
    sys.stderr.write("{}\n".format(m))
    sys.exit(1);

  def __init__(self, intervals, root):
    self.lower_limit = ABJAD_BOTTOM_LIMIT = -60;
    self.upper_limit = ABJAD_TOP_LIMIT = 67

    if not root >= self.lower_limit or not root <= self.upper_limit:
      self.error("Root out of range")

    self.intervals = intervals
    self.notes = []

    #find the lowest root in the range (just below the range)
    r = root
    while r > self.lower_limit:
      r -= 12
    
    position = 0;
    while r <= self.upper_limit:
      if not (position % 12):
        self._add_notes(r);
      r += 1
      position += 1;
    if not self.notes:
      error("Failed to build notes array");

  def _add_notes(self, root):
    pitch = root;
    role = 1;
    pitches = []
    for interval in self.intervals:
      pitch += interval
      if pitch >= self.lower_limit and pitch <= self.upper_limit:
        pitches.append({ "pitch_number" : pitch, "role" : role })
      role += 1
    self.notes += pitches;

  def __iter__(self):
    for note in self.notes:
       yield note

  def __len__(self):
    return len(self.notes)