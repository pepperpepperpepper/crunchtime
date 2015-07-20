#!/usr/bin/python2.7
import simplejson as json

SCALES = {
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
  "chromatic" :        [1,1,1,1,1,1,1,1,1,1,1]
}

ABJAD_BOTTOM_LIMIT = -60;
ABJAD_TOP_LIMIT = 67

def _add_scale_array(i, scale_array):
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

def make_scale_matrix(scale_name, scale_array):
  all_scales = []
  for offset in xrange(0, 12):
    new_scale = []
    for i in xrange(-100+offset,100+offset):
      if not ((i - offset) % 12):
        new_scale.append(_add_scale_array(i, scale_array))
    new_scale = [item for sublist in new_scale for item in sublist]
    new_scale_limited = []
    for item in new_scale:
      if item['pitch_number'] >= ABJAD_BOTTOM_LIMIT and \
        item['pitch_number'] <= ABJAD_TOP_LIMIT:
          new_scale_limited.append(item);
    all_scales.append(new_scale_limited)

  return all_scales

if __name__ == "__main__": 
  scales = {}
  for scale in SCALES.keys():
    scales[scale] = make_scale_matrix(scale, SCALES[scale])


#  f = open("scales_matrix.json", "w");
#  f.write(json.dumps(scales))
#  f.close();

  print make_scale_matrix("pentatonic_minor", SCALES["minor_pentatonic"]);
