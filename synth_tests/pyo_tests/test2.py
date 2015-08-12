#!/usr/bin/env python2.7
# encoding: utf-8
"""
This script demonstrates how to use pyo to do offline batch processing.

"""
import os
import pyo
import random
s = pyo.Server(duplex=0, audio="offline").boot()

# input sound
sndpath = "./test.aif"
# output folder
recpath = os.path.join("./rendered")
if not os.path.isdir(recpath):
    os.mkdir(recpath)

# output file duration
NUM = 10
orig_dur = pyo.sndinfo(sndpath)[1]
dur = pyo.sndinfo(sndpath)[1] * NUM

s.recordOptions(dur=dur, filename=os.path.join(recpath, "pyo_test.wav"), fileformat=0, sampletype=0)

    ############################
# Start an oscillator with a frequency of 250 Hz
#syn = pyo.SineLoop(freq=[250,251], feedback=.07, mul=.2).out()
#def callback(arg):
#    # Change the oscillator's frequency to 300 Hz after 2 seconds
#    syn.freq = arg
#a = pyo.CallAfter(callback, 2, [300,301])




t = pyo.HarmTable([1,0,.33,0,.2,0,.143,0,.111])
a = pyo.Osc(table=t, freq=[250,251], mul=.2).out()
def pat():
    f = random.randrange(200, 401, 25)
    a.freq = [f, f+1]
p = pyo.Pattern(pat, .125)
p.play()

s.start() # s.stop() is automatically called when rendering is done
# do not reboot the server after the last pass

print "Batch processing done"

