import os, time, sys
from subprocess import call
import abjad
import sys
from lib.Logger import Logger
OUTPUT_DIR = "./rendered";
PDF_VIEWER="okular"
AUDIO_PLAYER="mplayer"

class Renderer(object):
  def __init__(self, 
      audio_player=AUDIO_PLAYER, 
      pdf_viewer=PDF_VIEWER, 
      output_directory=OUTPUT_DIR, 
      clean=False,
      verbose=False, 
      log_output="stderr",
      **kwargs):
    
    self._verbose = verbose
    self._logger = Logger(log_output=log_output, role=self.__class__.__name__)
    self._time_str = str(int(time.time()));

 
    self.audio_player = audio_player
    self.pdf_viewer = pdf_viewer
    self.output_directory = output_directory
    if not os.path.isdir(self.output_directory):
      try:
        os.mkdir(self.output_directory)
      except OSError as e:
        self.log("The path {} already exists.\n"
          "Clear that path or specify a different directory name.".format(self.output_directory)
        )
    if clean:
      self.filename_clean() #for debugging
    
   
  def log(self, m, header_color="", color=""):
    self._logger.log(m, header_color=header_color, color=color, time_str=self._time_str)

  def filename_new(self, ext, filename=None):
    if not filename:
      filename = self._time_str
    return "{}.{}".format(os.path.join(self.output_directory, filename), ext);


  def filename_clean(self):
    for f in os.listdir(self.output_directory):
      if self._verbose:
        self.log("Removing {}...".format(f), color=self._logger.BLUE, header_color=self._logger.BLUE)
      os.unlink(os.path.join(self.output_directory, f));

  def _reset_term(self, dummy_a, dummy_b):
        call(["reset", "-I"]);

