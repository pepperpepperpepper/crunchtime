from lib.Renderer.Audio import RendererAudio
class RendererAudioMidi(RendererAudio):
  def __init__(self, **kwargs):
    super(RendererAudioMidi, self).__init__(**kwargs) 


  def log_info(self, m):
    self.log(m, header_color=self._logger.BLUE, color=self._logger.BLUE);
