import sys 
import signal
from subprocess import call
from lib.Renderer import Renderer
import abjad
class RendererAbjad(Renderer):
  def __init__(self, **kwargs):
    super(RendererAbjad, self).__init__(**kwargs) 

  def render(self, score, pdf=False, midi=False, render_all=True, preview=True, filename=None):
    self.filename=filename
    if pdf or render_all:
      self.file_pdf = self.filename_new("pdf", filename=self.filename);
      if self._verbose: 
        self.log("rendering {}\n".format(self.file_pdf), color=self._logger.GREEN, header_color=self._logger.GREEN);
      abjad.persist(score).as_pdf(self.file_pdf);
      if preview:
          try: 
            call([self.pdf_viewer, self.file_pdf]);
          except Exception as e:
            self.log("WARNING: Couldn't call {}\n".format(self.pdf_viewer), color=self._logger.YELLOW);
    if midi or render_all:
      self.file_midi = self.filename_new("midi", filename=filename);
      if self._verbose:
        sys.stderr.write("rendering {}\n".format(self.file_midi));
      abjad.persist(score).as_midi(self.file_midi);
      if preview:
        try: 
          signal.signal(signal.SIGINT, self._reset_term)
          call(['fluidsynth', '/home/pepper/pepsine.sf2', file_midi, '-F', file_audio ])
          call([AUDIO_PLAYER, file_audio]);
        except Exception as e:
          self.log("WARNING: Couldn't call {}\n".format(AUDIO_PLAYER), color=self._logger.YELLOW);
      self._reset_term()
    

