#import simplejson as json
import os, time, sys
from subprocess import call
from abjad import *
OUTPUT_DIR = "./rendered";
PDF_VIEWER="okular"
AUDIO_PLAYER="mplayer"

class MyError(Exception):
    pass

def filename_new(ext):
  return "{}.{}".format(os.path.join(OUTPUT_DIR, str(int(time.time()))), ext);

def filename_clean():
  for f in os.listdir(OUTPUT_DIR):
    os.unlink(os.path.join(OUTPUT_DIR, f));

def render_all(score, clean=False, play=False, preview=False):
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
  if preview:
      try: 
        call([PDF_VIEWER, file_pdf]);
      except Exception as e:
        sys.stderr.write("WARNING: Couldn't call {}\n".format(PDF_VIEWER));
  if play:
    try: 
      call([AUDIO_PLAYER, file_audio]);
    except Exception as e:
      sys.stderr.write("WARNING: Couldn't call {}\n".format(AUDIO_PLAYER));
