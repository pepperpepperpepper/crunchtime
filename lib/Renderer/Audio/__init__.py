from lib.Renderer import Renderer
class RendererAudio(Renderer):
  def __init__(self, **kwargs):
    super(RendererAudioFluidsynth, self).__init__(**kwargs) 


  def log_info(self, m);
    self.log(m, header_color=self._logger.MAGENTA, color=self._logger.MAGENTA);

