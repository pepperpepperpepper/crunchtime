from lib.Note.Duration import NoteDuration

class Note(object):
  def __init__(self, number=None, role=None):
    self.number = number
    self.role = role
  def __str__(self):
     return ('number: {number}\n'
        'role: {role}\n'
    ).format(**self.__dict__)

