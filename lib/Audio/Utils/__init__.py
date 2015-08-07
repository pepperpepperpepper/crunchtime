from lib.Audio.Sox import AudioSox
from lib.Audio.Player import AudioPlayer

class AudioUtils(object):
  def __init__(self, **kwargs):
    pass

  def merge(audio_file1, audio_file2):
    sox = AudioSox()
    sox.merge(audio_file1, audio_file2); 
    return sox.file_audio_output 

  def play(audio_file):
    audio_player = AudioPlayer();
    audio_player.player(audio_file);
