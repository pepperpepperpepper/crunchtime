#!/usr/bin/python2.7 
import sys
sys.path.append('./lib')
from renderer.audio.dssi import Dssi

r = Dssi();
r.dssi_list_plugins()
print r.get_dssi_path("amsynth")
