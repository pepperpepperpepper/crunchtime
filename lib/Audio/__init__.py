from lib.Logger import Logger
from subprocess import call
import time

class Audio(object):
  def __init__(self, 
      verbose=False, 
      log_output="stderr",
      **kwargs):
    
    self._verbose = verbose
    self._logger = Logger(log_output=log_output, role=self.__class__.__name__)
    self._time_str = str(int(time.time()));
   
  def log(self, m, header_color="", color=""):
    self._logger.log(m, header_color=header_color, color=color, time_str=self._time_str)

  def _reset_term(self, dummy_a, dummy_b):
        call(["reset", "-I"]);

