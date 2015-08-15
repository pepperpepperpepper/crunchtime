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
    if data.get("type") == "Tempo":
      data["number"] = parts[3]
    elif data.get("type") == "Header":
      data["format"] = parts[3]
      data["nTracks"] = parts[4]
      data["division"] = parts[5]
    elif data.get("type") == "Note_on_c":
      data["channel"] = parts[3]
      data["note"] = parts[4]
      data["vel"] = parts[5]
    elif data.get("type") == "Note_off_c":
      data["channel"] = parts[3]
      data["note"] = parts[4]
    elif data.get("type") == "Time_signature":
      data["numerator"] = parts[3]
      data["denominator"] = parts[4]
      data["click"] = parts[5]
      data["notesQ"] = parts[6]
    elif data.get("type") in ["Text_t", "Title_t"]:
      data["value"] = parts[3]
    elif data.get("type") == "Control_c":
      data["channel"] = parts[3]
      data["control_num"] = parts[4]
      data["value"] = parts[5]
    elif data.get("type") in [ "Channel_aftertouch_c", "Pitch_bend_c" ] :
      data["channel"] = parts[3]
      data["value"] = parts[4]
    elif data.get("type") == "Program_c":
      data["channel"] = parts[3]
      data["program_num"] = parts[4]
    elif data.get("type") == "Poly_aftertouch_c":
      data["channel"] = parts[3]
      data["note"] = parts[4]
      data["value"] = parts[5]

    return data
    
