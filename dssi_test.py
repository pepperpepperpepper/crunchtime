#!/usr/bin/python2.7 
from lib.Renderer.Audio.DSSI import RendererAudioDSSI

r = RendererAudioDSSI();
r.dssi_list_plugins()
print r.get_dssi_path("amsynth")
