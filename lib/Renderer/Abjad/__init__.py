import sys 
import signal
from subprocess import call
from lib.Renderer import Renderer
import abjad

class RendererAbjad(Renderer):
  def __init__(self, **kwargs):
    super(RendererAbjad, self).__init__(**kwargs) 

  def render(self, score, pdf=False, midi=False, render_all=True, filename=None, preview=False):
    """TODO: experiment with as_module...! http://abjad.mbrsi.org/api/tools/agenttools/PersistenceAgent.html"""
    self.filename=filename
    self.file_lily = self.filename_new("ly", filename=self.filename)
    if self._verbose:
      self.log_info("rendering {}".format(self.file_lily));
    if pdf or render_all:
      self.file_pdf = self.filename_new("pdf", filename=self.filename);
      if self._verbose: 
        self.log_info("rendering {}".format(self.file_pdf));
      abjad.persist(score).as_pdf(self.file_pdf);
      if preview:
          try: 
            call([self.pdf_viewer, self.file_pdf]);
          except Exception as e:
            self.log_warn("Couldn't call {}".format(self.pdf_viewer));
    if midi or render_all:
      self.file_midi = self.filename_new("midi", filename=filename);
      if self._verbose:
        self.log_info("rendering {}".format(self.file_midi));
      abjad.persist(score).as_midi(self.file_midi);
