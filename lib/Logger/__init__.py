from colorama import Fore, Back, Style
import sys
import time

class Logger(object):
  def __init__(self, role="", log_output="stderr", header_color=None):
    self._role = role
    self._log_output = log_output
    self._header_color = header_color

    self.RED = Fore.RED
    self.BLUE = Fore.BLUE
    self.GREEN = Fore.GREEN
    self.YELLOW = Fore.YELLOW
    self.MAGENTA = Fore.MAGENTA
    self.CYAN = Fore.CYAN
    self.WHITE = Fore.WHITE
    self.RED_WHITE = Fore.RED + Back.WHITE 
    self.BLUE_WHITE = Fore.BLUE + Back.WHITE 
    self.RESET = Fore.RESET + Back.RESET + Style.RESET_ALL 
  
  def _set_color(self, color):
    self._header_color = color;
    
  def log(self, m, color=None, header_color=None, time_str=None):
    
    if not header_color:
      header_color = self.RESET
    if not color:
      color = self.RESET 
    if not time:
      time_str = str(time.time())
    if not self._log_output:
      sys.stderr.write("Must specificy \"stderr\", \"stdout\", or filename" +\
        "to use log");
      sys.exit(1);
    header = "{}-log:\t".format(self._role)
    if self._log_output == "stderr":
      m = "{}{}{}\t{}{}\n".format(header_color, header, time_str, color, str(m))
      sys.stderr.write(m)
      sys.stderr.write(self.RESET);
      
    elif self._log_output == "stdout":
      m = "{}{}{}\t{}{}\n".format(header_color, header, time_str, color, str(m))
      sys.stdout.write(m)
      sys.stdout.write(self.RESET)
    else: 
      m = "{}{}--{}\n".format(header, time_str, str(m))
      try:
        f = open(self._log_output, "a");
        f.write(m);
        f.close();
      except Exception as e:
        sys.stderr.write("Could not write to log file {}\n".format(self._log_output))
        raise e
