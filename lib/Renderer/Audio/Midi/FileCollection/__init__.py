from lib.Renderer.Audio.Midi.File import RendererAudioMidiFile
from copy import deepcopy
class RendererAudioMidiFileCollection(RendererAudioMidi):
   def __init__(self, files=[], **kwargs):
     super(RendererAudioMidiFileCollection, self).__init__(**kwargs) 
     self.files = files
   def split_by_channel(self, midifile):
     channels = midifile._find_channels();
     for idx in range(0, len(channels)):
       new_file = deepcopy(midifile)
       channel_file = channels.pop(idx); 
       for channel in channels:
         new_file.remove_track(channel.get("Track"))
       new_file.filename_set("{}-{}".format(new_file.filename, channel_file.get("Channel")))
       self.files.append(new_file) 
   def midifiles_out(self):
     return map(lambda f: f.midifile_out(), self.files)
