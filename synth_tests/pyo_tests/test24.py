
#!/usr/bin/python2.7
from pyo import *
import re
output_filename =  "./rendered_mp3s/" + re.sub('\.py$', '.wav', __file__);
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='offline').boot()
s.recordOptions(dur=30.0, fileformat=0, filename=output_filename, sampletype=0)

s.start()
