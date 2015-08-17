import simplejson as json
import subprocess
import itertools
import sys
#MIDI_JSON_PATH="vendor/midi-json/midi-json"
from lib.Renderer.Audio.Midi.File import RendererAudioMidiFile



class RendererAudioMidiStream(object):
  def __init__(self, events):
    self.events = events
    self._tempo_find()
    self._division_find()
    self._channels_separate() 
    self.notes_current = []
    self.time_current = 0
  @classmethod
  def from_file(cls, filename):
    midifile = RendererAudioMidiFile(filename)
    events = midifile.events
    return cls(events) 

  @staticmethod
  def midi_json(filename):
     return json.loads(
       subprocess.Popen((MIDI_JSON_PATH, filename), stdout=subprocess.PIPE).communicate()[0]
     )

  def _tempo_set(self, event=None, tempo=None):
    if event:
      self.tempo = event.get("Number");
    else:
      self.tempo = tempo
    if not self.tempo:
      raise ValueError("no tempo value found")

  def _tempo_find(self):
    for event in self.events:
      if event.get("type") == "Tempo":
        self._tempo_set(event)
        break;

  def _division_set(self, event=None, division=None):
    if event:
      self.division = event.get("division");
    else:
      self.division = division
    if not self.division:
      raise ValueError("no division value found")

  def _division_find(self):
    for event in self.events:
      if event.get("type") == "Header":
        self._division_set(event)
        break;

  def _channels_separate(self):
    self.tracks = {}
    for event in self.events:
      track_no = event.get("track_no")
      if track_no:
        if track_no in self.tracks.keys():
          self.tracks[track_no].append(event)
        else:
          self.tracks[track_no] = [event]
    self.channels = map(lambda x: self.tracks[x], sorted(self.tracks.keys())[3:])
    self.channels = map(lambda x: { "current_event" : {} , "events": itertools.chain(x) }, [ self.channels[0] ])

  def make_event_stream(self):
     total_events = []
     self.abs_time = 0
     events_to_process = []
     channels_left_to_process = len(self.channels)
     while channels_left_to_process: 
       for channel in self.channels:
         if channel["current_event"].get("type") == "End_track":
           channels_left_to_process -= 1;
           continue;
         if not channel["current_event"] and channels_left_to_process:
           channel["current_event"] = channel["events"].next()
         while int(channel["current_event"].get("abs_time")) <= self.abs_time and channel["current_event"].get("type") != "End_track":
           events_to_process.append(channel["current_event"])
           channel["current_event"] = channel["events"].next();
       total_events.append(events_to_process)
       events_to_process = []
       self.abs_time += 1;
     return itertools.chain(total_events)

