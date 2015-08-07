import sys 
import signal
from subprocess import call
from lib.Renderer import Renderer
import abjad
DEFAULT_SOUNDFONT="./assets/pepsine.sf2"
AUDIO_PLAYER="mplayer"
class RendererAbjad(Renderer):
  def __init__(self, **kwargs):
    super(RendererAbjad, self).__init__(**kwargs) 

  def render(self, score, pdf=False, midi=False, render_all=True, preview=True, filename=None):
    """TODO: experiment with as_module...! http://abjad.mbrsi.org/api/tools/agenttools/PersistenceAgent.html"""
    self.filename=filename
    self.file_lily = self.filename_new("ly", filename=self.filename)
    if self._verbose:
      self.log("rendering {}".format(self.file_lily), color=self._logger.GREEN, header_color=self._logger.GREEN);
    if pdf or render_all:
      self.file_pdf = self.filename_new("pdf", filename=self.filename);
      if self._verbose: 
        self.log("rendering {}".format(self.file_pdf), color=self._logger.GREEN, header_color=self._logger.GREEN);
      abjad.persist(score).as_pdf(self.file_pdf);
      if preview:
          try: 
            call([self.pdf_viewer, self.file_pdf]);
          except Exception as e:
            self.log("WARNING: Couldn't call {}".format(self.pdf_viewer), color=self._logger.YELLOW);
    if midi or render_all:
      self.file_midi = self.filename_new("midi", filename=filename);
      if self._verbose:
        self.log("rendering {}".format(self.file_midi), color=self._logger.GREEN, header_color=self._logger.GREEN);
      abjad.persist(score).as_midi(self.file_midi);
      if preview:
        try: 
#          signal.signal(signal.SIGINT, self._reset_term)
          self.file_audio = self.filename_new("wav", filename=filename)
          call(['fluidsynth', DEFAULT_SOUNDFONT, self.file_midi, '-F', self.file_audio ])
          call([AUDIO_PLAYER, self.file_audio]);
        except Exception as e:
          self.log("WARNING: Couldn't call {}".format(AUDIO_PLAYER), color=self._logger.YELLOW, header_color=self._logger.RED_WHITE);
          self.log(str(e), color=self._logger.YELLOW, header_color=self._logger.RED_WHITE)
      self._reset_term()
    

