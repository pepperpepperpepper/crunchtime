class Note(object):
  def __init__(self, **kwargs):
  def __str__(self):
     return ('number: {number}\n'
        'role: {role}\n'
    ).format(**self.__dict__)

