#!/usr/bin/python2.7
import simplejson as json
ABJAD_BOTTOM_LIMIT = -60;
ABJAD_TOP_LIMIT = 67

_CHORD_SPELLINGS = {
  "sus2" : [0,2,5],
  "major" : [0,4,3],
  "minor" : [0,3,4],
  "sus4" : [0,5,2],
  "major6" : [0,4,3,2],
  "minor6" : [0,3,4,2],
  "majorb7" : [0,4,3,3],
  "minorb7" : [0,3,4,3],
  "majorM7" :  [0,4,3,4],
  "minorM7" :  [0,3,4,4],
  "majorb7b9" : [0,4,3,3,3],
  "minorb7b9" : [0,3,4,3,3],
  "majorb7M9" : [0,4,3,3,4],
  "minorb7M9" : [0,3,4,3,4],
  "majorb7s9" : [0,4,3,3,5],
  "majorM7b9" :  [0,4,3,4,2],
  "minorM7b9" :  [0,3,4,4,2],
}



def _add_inversions(spelling):
  _inversions = [spelling];
  for s in xrange(0, len(spelling) - 1):
    spelling = spelling[1:]+ [spelling[0] ]
    _inversions.append(spelling)
  return _inversions


def build_chord_matrix():
  chords = {}
  for chord_type in _CHORD_SPELLINGS.keys():
    spelling = _CHORD_SPELLINGS[chord_type]
    chords[chord_type] = {
      "spelling" : spelling,
      "inversions" : _add_inversions(spelling) 
    }
  return chords

class Chord(object):
  def __init__(self, name, starting_pitch):
    self._spelling = _CHORD_SPELLINGS[name]
    self._inversions = _add_inversions(self._spelling)
  def inversion(self, number=1):
    pass
  def spell_nearest(self, pitch):
    pass
  



def _add_chord(i, scale_array):
  new_array = []
  s = sum(scale_array)
  position = 0;
  for role in xrange(0,len(scale_array)):
    distance = scale_array[role]
    position += distance
    new_array.append(
      { 
        "role" : role + 1,
        "pitch_number" : i+position,
      }
    );
  return new_array

def make_chord_matrix(chord_name, chord):
  all_chords = []
  for offset in xrange(0, 12):
    new_chord = []
    for i in xrange(-100+offset,100+offset):
      if not ((i - offset) % 12):
        print i
#        new_chord.append(_add_scale_array(i, scale_array))
#    new_scale = [item for sublist in new_scale for item in sublist]
#    new_scale_limited = []
#    for item in new_scale:
#      if item['pitch_number'] >= ABJAD_BOTTOM_LIMIT and \
#        item['pitch_number'] <= ABJAD_TOP_LIMIT:
#          new_scale_limited.append(item);
#    all_scales.append(new_scale_limited)

#  return { 
#    "name" : scale_name,
#    "data" : all_scales
#  }



if __name__ == "__main__":
#  scales = []
#  for scale in SCALES.keys():
#    scales.append(make_scale_matrix(scale, SCALES[scale]))
  make_chord_matrix("","");
#  f = open("chord_matrix.json", "w");
#  f.write(json.dumps(scales))
#  f.close();
