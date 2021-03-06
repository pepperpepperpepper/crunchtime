from lib.RendererMidi import RendererMidi
from lib.RendererMidi.File import RendererMidiFile
from copy import deepcopy
import re
import sys;
class RendererMidiFileCollection(RendererMidi):
   def __init__(self, files=[], **kwargs):
     super(RendererMidiFileCollection, self).__init__(**kwargs) 
     self.files = files
   def split_by_channel(self, midifile):
     channels = midifile._find_channels();
     for channel_file in channels:
       new_file = deepcopy(midifile)
       for channel in channels:
         if channel.get("Channel") != channel_file.get("Channel"):
           new_file.remove_track(channel.get("Track"))
       new_file.filename_set(re.sub(r'(\.[a-zA-Z]+$)', r'-{}\1'.format(channel_file.get("Channel")), new_file.filename_get()))
       self.files.append(new_file) 
   def midifiles_out(self):
     return map(lambda f: f.midifile_out(), self.files)
