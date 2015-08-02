import re
class Alias(object):
  def error(self, m):
    sys.stderr.write("{}\n".format(m))
    sys.exit(1);
  def __init__(self, name, alias_list):
    self.value = 0;
    for i in alias_list:
      if self._name_match(name, i.get("name")):
        self.value = i.get("value")
        return
    if not self.value:
      self.error("No such name or alias: {}".format(name))

  def _name_match(self, name, match):
    original = name;
    name = re.sub(r'[_\s\-]', "", name)
    subs_list = [
      (r'tritone', "s4"),
      (r'(one|first|halfstep)', "1"),
      (r'(second|two|wholestep)', "2"),
      (r'(third|three)', "3"),
      (r'(fourth|four)', "4"),
      (r'(fifth|five)', "5"),
      (r'(sixth|six)', "6"),
      (r'(seventh|seven)', "7"),
      (r'(sharped|sharp|augmented|aug|\+)', "s"),
      (r'(flatted|flat|diminished|dim)', "b"),
      (r'(major|maj)', "M"),
      (r'(minor|min)', "m"),
      (r'(p)([0-9])', r'p\2'),
      (r'(s)([0-9])', r's\2'),
      (r'(b)([0-9])', r'b\2'),
    ]
    for i in subs_list:
      name = re.sub(i[0], i[1], name, flags=re.I);
    if name == match:
      return True
    return False      
