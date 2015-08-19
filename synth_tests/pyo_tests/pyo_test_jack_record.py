from pyo import *
import time, os

filename = "test2.wav"
s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1,  audio='jack')
s.boot()
s.recstart(filename)

a = Sine(mul=0.3).out()

s.start()

time.sleep(10)

s.recstop()
