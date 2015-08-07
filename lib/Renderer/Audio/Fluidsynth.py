import sys 
from subprocess import call
from lib.Renderer.Audio import RendererAudio

SOUNDFONTS={
  "sinewav" : "./assets/soundfonts/pepsine.sf2",
}

class RendererAudioFluidsynth(RendererAudio):
  def __init__(self, **kwargs):
    """TODO: create a property for self.file_audio that when accessed as a NoneType 
      an attribute error is raised, saying that the file_audio has yet to be rendered!
    """
    super(RendererAudioFluidsynth, self).__init__(**kwargs) 
    self.SOUNDFONTS = SOUNDFONTS
  def render(self, midifile, soundfont=None, play=False, format_type="wav", filename=None):
    if not soundfont:
      soundfont = self.SOUNDFONTS.get("sinewav");
    self.file_audio = self.filename_new(format_type, filename=filename)
    if self._verbose:
      self.log_info("rendering {} with {}".format(self.file_audio, soundfont));
    try: 
      call(['fluidsynth', soundfont, midifile, '-F', self.file_audio ])
    except Exception as e:
      self.log_warn("WARNING: Unable to process {} with fluidsynth".format(midifile))
      self.log_warn(str(e))
    return self.file_audio
      
  def render_sine(self, midifile, play=False, format_type="wav"):
    self.render(midifile, play=play, format_type=format_type)
