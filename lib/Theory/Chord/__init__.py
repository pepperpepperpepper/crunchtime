from lib.NoteSet import NoteSet;
from lib.Theory.Interval import Interval
class Chord(NoteSet):
  def __init__(self, root, position="close", inversion="root", nearest=True, **kwargs):
    self._CHORD_INTERVALS = {
      "major" : [0, 4, 3],
      "minor" : [0, 3, 4],
      "diminished" : [0, 3, 3],
      "augmented" : [0, 4, 4],
      "major_major7" : [0, 4, 3, 4],
      "minor_major7" : [0, 3, 4, 4],
      "diminished_major7" : [0, 3, 3, 5],
      "augmented_major7" : [0, 4, 4, 3],
      "major_minor7" : [0, 4, 3, 3],
      "minor_minor7" : [0, 3, 4, 3],
      "minor7_b5" : [0, 3, 3, 4],
      "augmented_minor7" : [0, 4, 4, 2],
    }
    if "name" in kwargs:
      if kwargs.get("name") not in self._CHORD_INTERVALS.keys():
        message = "Bad Chord Type:\n" + \
          "try one of these...\n" + \
          "\n".join(map(lambda x: "\t\"{}\"".format(x), self._CHORD_INTERVALS.keys()));
        self.error(message)
      intervals = map(lambda a: Interval(length=a), self._CHORD_INTERVALS.get(kwargs.get("name"))) 
      super(Chord, self).__init__(intervals, root)
    elif intervals in kwargs: 
      super(Chord, self).__init__(intervals, root)
    else:
      self.error("no set of intervals or scale name provided");
#    self.set_inversion(inversion);
    self.root = root
    if nearest: self.set_nearest();


  def set_nearest(self, voice_leading=False):
    import sys
    self.notes = []
    length = len(self._CHORD_INTERVALS)
    first_note = {}
    for note in self.notes_all:
      if note.number == self.root:
        first_note = note
        break;
    root_idx = self.notes_all.index(first_note)


    for i in xrange(0, length):
      self.notes.append(self.notes_all[root_idx + i]);

  def __iter__(self):
    for note in self.notes:
       yield note

