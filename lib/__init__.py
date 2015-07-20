import simplejson as json
import os, time, sys
from subprocess import call
from abjad import *
OUTPUT_DIR = "./rendered";



#load scales_lib
f = open("./lib/scales_matrix.json", "r");
scale_lib = json.loads(f.read());
f.close()

class MyError(Exception):
    pass

class Scale(object):
  def __init__(self, scale_type, root):
    self.notes = []
    try:
      for scale in scale_lib[scale_type]:
        for note in scale:
          if note['pitch_number'] == root and note['role'] == 1:
            self.notes = scale
    except KeyError as e:
      message = "Bad Scale Type:\n" + \
        "try one of these...\n" + \
        + "\n".join(map(lambda x: "\"{}\"".format(x), scale_lib.keys()));
      MyError(message)
    if not self.notes:
      raise ValueError

  def __iter__(self):
    for note in self.notes:
       yield note

  def __len__(self):
    return len(self.notes)

def filename_new(ext):
  return "{}.{}".format(os.path.join(OUTPUT_DIR, str(int(time.time()))), ext);

def filename_clean():
  for f in os.listdir(OUTPUT_DIR):
    os.unlink(os.path.join(OUTPUT_DIR, f));

def render_all(score, clean=False):
  if clean:
    filename_clean() #for debugging
  file_midi = filename_new("midi");
  file_audio = filename_new("wav");
  file_pdf = filename_new("pdf");
  sys.stderr.write("rendering {}\n".format(file_midi));
  persist(score).as_midi(file_midi);
  sys.stderr.write("rendering {}\n".format(file_pdf));
  persist(score).as_pdf(file_pdf);
  sys.stderr.write("rendering {} as {}...\n".format(file_midi, file_audio));
  call(['fluidsynth', '/home/pepper/pepsine.sf2', file_midi, '-F', file_audio ])
