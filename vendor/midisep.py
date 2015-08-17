




def _correct_bad_note_ons(self, event):
  if event.get("type") == "Note_on_c" and event.get("vel") == 0:
    event["type"] = "Note_off_c" 
  return $event;
  
