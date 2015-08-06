import sys
from lib.Note import Note
class NoteSet(object):
  def error(self, m):
    sys.stderr.write(m)
    sys.exit(1);

  def __init__(self, intervals, root):
    self.lower_limit = ABJAD_BOTTOM_LIMIT = -60;
    self.upper_limit = ABJAD_TOP_LIMIT = 67
    self.intervals = intervals
    self.notes_all = []

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
    if not self.notes_all:
      error("Failed to build notes array");

  def _add_notes(self, root):
    number = root;
    role = 1;
    notes = []
    for interval in self.intervals:
      number += interval.length
      if number >= self.lower_limit and number <= self.upper_limit:
        notes.append(Note(number=number, role=role ))
      role += 1
    self.notes_all += notes;

  def _interval_accum(self, intervals):
    o_intervals = [0]
    for i in xrange(0, len(intervals)):
      o_intervals.append(o_intervals[i] + intervals[i])

  def __iter__(self):
    for note in self.notes_all:
       yield note

  def __len__(self):
    return len(self.notes_all)
