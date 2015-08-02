from lib.Alias import Alias
class AliasInterval(Alias):
  def __init__(self, name):
    self.alias_list = [
      {"name" : "m2", "value" : 1}, 
      {"name" : "M2", "value" : 2},
      {"name" : "m3", "value" : 3},
      {"name" : "M3", "value" : 4},
      {"name" : "p4", "value" : 5}, 
      {"name" : "s4", "value" : 6},
      {"name" : "b5", "value" : 6}, 
      {"name" : "p5", "value" : 7},
      {"name" : "s5", "value" : 8},
      {"name" : "m6", "value" : 8},
      {"name" : "M6", "value" : 9}, 
      {"name" : "m7", "value" : 10},
      {"name" : "M7", "value" : 11},
    ];
    super(AliasInterval, self).__init__(name, self.alias_list)
    
