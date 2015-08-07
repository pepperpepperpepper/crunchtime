import sys 
from subprocess import call
import signal
DEFAULT_AUDIO_PLAYER="mplayer"

class AudioPlayer(Audio):
  def __init__(self, audio_player=DEFAULT_AUDIO_PLAYER, **kwargs):
    self.audio_player = audio_player
    super(RendererAudioPlayer, self).__init__(**kwargs) 
  
  def play(self, file_audio):
    signal.signal(signal.SIGINT, self._reset_term)
    try: 
      call([self.audio_player, file_audio]);
    except Exception as e:
      self.log("WARNING: Couldn't call {}".format(self.audio_player), color=self._logger.YELLOW, header_color=self._logger.RED_WHITE);
      self.log(str(e), color=self._logger.YELLOW, header_color=self._logger.RED_WHITE)
      
