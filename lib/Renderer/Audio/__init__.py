
import sys 
import signal
from subprocess import call
from lib.Renderer import Renderer
import abjad
class RendererAbjad(Renderer):
  def __init__(self, **kwargs):
    super(RendererAbjad, self).__init__(kwargs) 

  def render_midi(self, play=False, format_type="wav"):
    

