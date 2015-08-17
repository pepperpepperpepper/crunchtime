MIDICSV_PATH="midicsv"
import subprocess

class RendererAudioMidiFile(object):
  def __init__(self, filename):
    s = subprocess.Popen((MIDICSV_PATH, filename), stdout=subprocess.PIPE).communicate()[0]
    lines = s.split("\n");
    lines = map(lambda x: self._line_to_obj(x), lines) 
    lines = filter(lambda x: x, lines)
    self.events = lines
  def _line_to_obj(self, line):
    parts = line.split(",")
    parts = map(lambda x: x.replace(" ",""), parts)
    
    if len(parts) < 2:
      return {}
    data = { 
      "track_no": parts[0],
      "abs_time" : parts[1],
      "type": parts[2]
    }
    if data.get("type") == "Header":
      data["format"] = parts[3]
      data["nTracks"] = parts[4]
      data["division"] = parts[5]
    elif data.get("type") in [ "End_of_file", "Start_track" , "End_track" ]:
      pass
    elif data.get("type") in [ 
        "Title_t", "Copyright_t", "Instrument_name_t", 
        "Marker_t", "Cue_point_t", "Lyric_t", "Text_t" 
      ]:
      data["Text"] = parts[3]
    elif data.get("type") in [ "Sequence_number", "MIDI_port", "Channel_prefix" ]:
      data["Number"] = parts[3]
    elif data.get("type") == "Time_signature":
      data["Num"] = parts[3]
      data["Denom"] = parts[4]
      data["Click"] = parts[5]
      data["NotesQ"] = parts[6]
    elif data.get("type") == "Key_signature" :
      data["Key"] = parts[3]
      data["Major/Minor"] = parts[4]
    elif data.get("type") == "Tempo":
      data["Number"] = parts[3]
    elif data.get("type") == "SMPTE_offset":
      data["Hour"] = parts[3]
      data["Minute"] = parts[4]
      data["Second"] = parts[5]
      data["Frame"] = parts[6]
      data["FracFrame"] = parts[7]
    elif data.get("type") == "Sequencer_specific":
      data["Length"] = parts[3]
      data["Data"] = parts[4:]
    elif data.get("type") == "Unknown_meta_event":
      data["Type"] = parts[3]
      data["Length"] = parts[4]
      data["Data"] = parts[5:]

    elif data.get("type") == "Note_on_c":
      data["Channel"] = parts[3]
      data["Note"] = parts[4]
      data["Velocity"] = parts[5]
    elif data.get("type") == "Note_off_c":
      data["Channel"] = parts[3]
      data["Note"] = parts[4]
      data["Velocity"] = parts[4]
    elif data.get("type") == "Control_c":
      data["Channel"] = parts[3]
      data["Control_Num"] = parts[4]
      data["Value"] = parts[5]
    elif data.get("type") in [ "Channel_aftertouch_c", "Pitch_bend_c" ] :
      data["Channel"] = parts[3]
      data["Value"] = parts[4]
    elif data.get("type") == "Program_c" : 
      data["Channel"] = parts[3]
      data["Program_num"] = parts[4]
    elif data.get("type") == "Poly_aftertouch_c" : 
      data["Channel"] = parts[3]
      data["Note"] = parts[4]
      data["Value"] = parts[5]

    elif data.get("type") in [ "System_exclusive" ] :
      data["Length"] = parts[3]
      data["Data"] = parts[4:]

    return data

  def recompile(self, events):
    pass
