DSSI_RENDER_PATH="vendor/dssi-render/src/dssi-render"
DSSI_LIST_PLUGINS_PATH="/usr/bin/dssi_list_plugins"
import os
import re
from subprocess import call, PIPE, Popen
from lib.Renderer.Audio import RendererAudio

class RendererAudioDSSI(RendererAudio):
  def __init__(self, 
    channels=0, 
    sample_rate=44100,
    ignore_clips=True,
    **kwargs
  ):
    super(RendererAudioDSSI, self).__init__(**kwargs) 
    self.filename = self.filename_new("wav",filename=kwargs.get("filename",None));
    self.sample_rate = sample_rate
    self.ignore_clips = ignore_clips 

  def get_dssi_path(self, plugin_name):
    for plugin in self.dssi_list_plugins():
      if re.search(plugin_name, plugin['description'], re.IGNORECASE) or re.search(plugin_name, plugin['path'], re.IGNORECASE):
        return plugin
  
  def dssi_list_plugins(self):
    _data = Popen((DSSI_LIST_PLUGINS_PATH), stdout=PIPE).communicate()[0]
    _lines = _data.split("\n");
    plugins = []
    _description_reg = re.compile(r'\t');
    for l in xrange(0, len(_lines)):
      plugin = {}
      if re.match('.*\.so$', _lines[l], re.IGNORECASE):
        plugin['path'] = _lines[l]
        if l < len(_lines):
          plugin['description'] = re.sub(r'\s\s+', ' - ', re.sub(r'\t', '', _lines[l+1]))
        else:
          plugin['description'] = ""
        plugins.append(plugin)
    return plugins

  def _dssi_render_cmd(self, midi_filename, plugin_path, stdin=False, port_values="default"):
    cmd = [ DSSI_RENDER_PATH, plugin_path]
    if port_values == "default":
      cmd += [ "-p", "-1" ] 
    elif port_values == "random":
      cmd += [ "-p", "-2" ]
    cmd += [ "-i" , midi_filename ]
    cmd += [ "-o", self.filename ] 
    if not self.channels:
      cmd += [ "-c", "-1" ] #use the plugin's default channel count
    else:
      cmd += [ "-c", self.channels ]
    cmd += [ "-r", self.sample_rate ] 
    if self.ignore_clips:
      cmd += [ "-b" ]
    if self._verbose:
      self.log_info("Calling cmd: %s" % " ".join(cmd))
    self._call_cmd(cmd); 
    
  def render(filename, plugin_path=_default_plugin_path):
    pass
    

