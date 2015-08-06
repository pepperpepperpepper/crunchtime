import os, time, sys
from subprocess import call
import abjad
import signal
import sys
OUTPUT_DIR = "./rendered";
PDF_VIEWER="okular"
AUDIO_PLAYER="mplayer"

class Renderer(object):
  def __init__(self, audio_player=AUDIO_PLAYER, 
      pdf_viewer=PDF_VIEWER, 
      output_directory=OUTPUT_DIR, 
      clean=False,
      **kwargs):
    
    self.audio_player = audio_player
    self.pdf_viewer = pdf_viewer
    self.output_directory = output_directory
    if not os.path.isdir(self.output_directory):
      try:
        os.mkdir(self.output_directory)
      except OSError as e:
        sys.stderr.write("The path {} already exists.\n"
          "Clear that path or specify a different directory name.".format(self.output_directory)
        )
    if clean:
      self.filename_clean() #for debugging
    self._time_str = str(int(time.time()));
    
     
  def filename_new(self, ext, name=None):
    if not name:
      name = self._time_str
    return "{}.{}".format(os.path.join(self.output_directory, name), ext);


  def filename_clean(self):
    for f in os.listdir(self.output_directory):
      os.unlink(os.path.join(self.output_directory, f));

  def _reset_term(self, signal, frame):
        call(["reset", "-I"]);

  def render_abjad(self, score, verbose=True):
    file_midi = self.filename_new("midi");
    file_pdf = self.filename_new("pdf");
    if verbose:
      sys.stderr.write("rendering {}\n".format(file_midi));
    abjad.persist(score).as_midi(file_midi);
    if verbose: 
      sys.stderr.write("rendering {}\n".format(file_pdf));
    abjad.persist(score).as_pdf(file_pdf);
    return (file_midi, file_pdf);

  def render_all(self, score, play=False, preview=False):
    file_midi, file_pdf = self.render_abjad(score)
    file_audio = self.filename_new("wav");
    sys.stderr.write("rendering {} as {}...\n".format(file_midi, file_audio));
    signal.signal(signal.SIGINT, self._reset_term)
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
    call(["reset", "-I"]);
