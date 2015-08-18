from lib.Renderer.Audio.Midi import RendererAudioMidi
MIDICSV_PATH="midicsv"
CSVMIDI_PATH="csvmidi"
import subprocess, sys
from distutils.spawn import find_executable

class RendererAudioMidiFile(RendererAudioMidi):
  def __init__(self, filename, midicsv_path=MIDICSV_PATH, csvmidi_path=CSVMIDI_PATH):
    super(RendererAudioMidiFile, self).__init__(**kwargs) 
    self.filename_original = filename
    if not os.path.exits(self.filename_original):
      self.log_error("Could not find filename {}".format(self.filename_original);
      sys.exit(1);
    
    for filepath in [ midicsv_path, csvmidi_path ]:
      if not os.path.exists(filepath) and not find_executable(filepath):
        self.log_error("Could not find path {}".format(filepath));
        sys.exit(1)
    self._midicsv_path = midicsv_path 
    self._csvmidi_path = csvmidi_path
    self.events = []
    self._csv_decompile();

  def _csv_decompile(self):
    s = subprocess.Popen((self._midicsv_path, self.filename_original), stdout=subprocess.PIPE).communicate()[0]
    lines = s.split("\n");
    lines = map(lambda x: self._csv_line_to_obj(x), lines) 
    lines = filter(lambda x: x, lines)
    self.events = lines
    
  def _csv_line_to_obj(self, line):
    #{{{ line parsing 
    parts = line.split(",")
    parts = map(lambda x: x.replace(" ",""), parts)
    
    if len(parts) < 2:
      return {}
    data = { 
      "Track": parts[0],
      "Time" : parts[1],
      "Type": parts[2]
    }
    if data.get("Type") == "Header":
      data["format"] = parts[3]
      data["nTracks"] = parts[4]
      data["division"] = parts[5]
    elif data.get("Type") in [ "End_of_file", "Start_track" , "End_track" ]:
      pass
    elif data.get("Type") in [ 
        "Title_t", "Copyright_t", "Instrument_name_t", 
        "Marker_t", "Cue_point_t", "Lyric_t", "Text_t" 
      ]:
      data["Text"] = parts[3]
    elif data.get("Type") in [ "Sequence_number", "MIDI_port", "Channel_prefix" ]:
      data["Number"] = parts[3]
    elif data.get("Type") == "Time_signature":
      data["Num"] = parts[3]
      data["Denom"] = parts[4]
      data["Click"] = parts[5]
      data["NotesQ"] = parts[6]
    elif data.get("Type") == "Key_signature" :
      data["Key"] = parts[3]
      data["Major/Minor"] = parts[4]
    elif data.get("Type") == "Tempo":
      data["Number"] = parts[3]
    elif data.get("Type") == "SMPTE_offset":
      data["Hour"] = parts[3]
      data["Minute"] = parts[4]
      data["Second"] = parts[5]
      data["Frame"] = parts[6]
      data["FracFrame"] = parts[7]
    elif data.get("Type") == "Sequencer_specific":
      data["Length"] = parts[3]
      data["Data"] = parts[4:]
    elif data.get("Type") == "Unknown_meta_event":
      data["Type"] = parts[3]
      data["Length"] = parts[4]
      data["Data"] = parts[5:]

    elif data.get("Type") == "Note_on_c":
      data["Channel"] = parts[3]
      data["Note"] = parts[4]
      data["Velocity"] = parts[5]
    elif data.get("Type") == "Note_off_c":
      data["Channel"] = parts[3]
      data["Note"] = parts[4]
      data["Velocity"] = parts[4]
    elif data.get("Type") == "Control_c":
      data["Channel"] = parts[3]
      data["Control_Num"] = parts[4]
      data["Value"] = parts[5]
    elif data.get("Type") in [ "Channel_aftertouch_c", "Pitch_bend_c" ] :
      data["Channel"] = parts[3]
      data["Value"] = parts[4]
    elif data.get("Type") == "Program_c" : 
      data["Channel"] = parts[3]
      data["Program_num"] = parts[4]
    elif data.get("Type") == "Poly_aftertouch_c" : 
      data["Channel"] = parts[3]
      data["Note"] = parts[4]
      data["Value"] = parts[5]

    elif data.get("Type") in [ "System_exclusive" ] :
      data["Length"] = parts[3]
      data["Data"] = parts[4:]
    #}}}
    return data

  def _csv_recompile(self, events):
    _output_array = [];
    #{{{ line parsing 
    for event in self.events:
      event_list = [
        event.get("Track"),
        event.get("Time"),
        event.get("Type")
      ]
      if event.get("Type") == "Header":
        event_list += [ 
          event.get("format"),  
          event.get("nTracks"),
          event.get("division"),
        ]
      elif event.get("Type") in [
        "Title_t", "Copyright_t", "Instrument_name_t", 
        "Marker_t", "Cue_point_t", "Lyric_t", "Text_t" 
      ]:
        event_list.append(event.get("Text"))
      elif event.get("Type") in [ "Sequence_number", "MIDI_port", "Channel_prefix" ]:
        event_list.append(event.get("Number"))
      elif event.get("Type") == "Time_signature":
        event_list += [
          event.get("Num"),
          event.get("Denom"),
          event.get("Click"),
          event.get("NotesQ"),
        ]
      elif event.get("Type") == "Key_signature" :
        event_list += [
          event.get("Key"),
          event.get("Major/Minor"),
        ]
      elif event.get("Type") == "Tempo":
        event_list.append(event.get("Number"))
      elif event.get("Type") == "SMPTE_offset":
        event_list += [
          event.get("Hour"),
          event.get("Minute"),
          event.get("Second"),
          event.get("Frame"),
          event.get("FracFrame"),
        ]
      elif event.get("Type") == "Sequencer_specific":
        event_list += [
          event.get("Length"),
          event.get("Data"),
        ]
      elif event.get("Type") == "Unknown_meta_event":
        event_list += [
          event.get("Type"),
          event.get("Length"),
          event.get("Data"),
        ]
      elif event.get("Type") == "Note_on_c":
        event_list += [
          event.get("Channel"),
          event.get("Note"),
          event.get("Velocity"),
        ]
      elif event.get("Type") == "Note_off_c":
        event_list += [
          event.get("Channel"),
          event.get("Note"),
          event.get("Velocity"),
        ]
      elif event.get("Type") == "Control_c":
        event_list += [
          event.get("Channel"),
          event.get("Control_Num"),
          event.get("Value"),
        ]
      elif event.get("Type") in [ "Channel_aftertouch_c", "Pitch_bend_c" ] :
        event_list += [
          event.get("Channel"),
          event.get("Value"),
        ]
      elif event.get("Type") == "Program_c" :
        event_list += [
          event.get("Channel"),
          event.get("Program_num"),
        ]
      elif event.get("Type") == "Poly_aftertouch_c" :
        event_list += [
          event.get("Channel"),
          event.get("Note"),
          event.get("Value"),
        ]

      elif event.get("Type") in [ "System_exclusive" ] :
        event_list += [
          event.get("Length"),
          event.get("Data"),
        ]
      _output_array.append(", ".join(event_list));
    #}}}
    _output_str = "\n".join(_output_array); 
    _output_csv = self.filename_temporary_new("csv");
    try:
      f = open(_output_csv, "w");
      f.write(_output_str);
      f.close()
    except Exception as e:
      self.log_err(str(e));
      self.log_err("Could not write to file {}".format(_output_csv));
      sys.exit(1)
    file_midi_output = self.filename_new();
    self._csv_midi_cmd(inputfile=_output_csv, outputfile=file_midi_output)
    return file_midi_output;

