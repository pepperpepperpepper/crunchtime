import os, time, sys
from subprocess import call
import abjad
import signal
import sys
from lib.Renderer.Defaults import RendererDefaults;
RENDERER_DEFAULTS = RendererDefaults();

class RendererAbjad(object):
  def __init__(self, number=None, role=None, output_dir=RENDERER_DEFAULTS.output_directory, ):
    pass
  def __str__(self):
     return ('number: {number}\n'
        'role: {role}\n'
    ).format(**self.__dict__)

