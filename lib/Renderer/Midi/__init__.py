from lib.Renderer import Renderer
class RendererMidi(Renderer):
  def __init__(self, **kwargs):
    super(RendererMidi, self).__init__(**kwargs) 


  def log_info(self, m):
    self.log(m, header_color=self._logger.BLUE, color=self._logger.BLUE);
