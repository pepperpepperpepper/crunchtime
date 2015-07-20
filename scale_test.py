#!/usr/bin/python2.7
import simplejson as json
import os, sys
import random
from abjad import *
from lib import Scale, render_all
from lib import scale_lib
import time
import os
from subprocess import call

def choose_random_note_in_range(scale):
  upper_limit = 20;
  lower_limit = 0;
  choice = None
  note_number = None
  while not (note_number < upper_limit and note_number > lower_limit):
    choice = random.choice(scale)
    note_number = choice["pitch_number"]
  return choice 

def pitches_to_quarter_notes(pitches):
  notes = []
  for pitch in pitches:
    notes.append(Note(pitch['pitch_number'], Duration(1,4)))
  return notes

def add_to_score(pitches,score):
  notes = pitches_to_quarter_notes(pitches) 
  container = Container(notes);
  staff = Staff([ container ])
  score.append(staff);
  return score
  
def make_abjad_segment(score):
  persist(score).as_midi('test.midi'.format(int(time.time())));
  persist(score).as_pdf('test.pdf'.format(int(time.time())));
  call(['fluidsynth', '/home/pepper/pepsine.sf2', 'test.midi', '-F', 'test.wav' ])

def main():
  score = Score([]);
  measures = 20;
  beats = 4 * measures
  
  tempo = Tempo(Duration(1, 4), 240)
  attach(tempo, score)

  C = 0
  Cs = 1
  D = 2
  Eb = 3
  E = 4
  F = 5
  Fs = 6
  G = 7
  Ab = 8
  A = 9
  Bb = 10
  B = 11
  
  
  scale1 = Scale("minor_pentatonic", D);
  scale2 = Scale("minor_pentatonic", G);
  part1 = []
  for i in xrange(0,beats):
    part1.append(choose_random_note_in_range(scale1.notes))
  score = add_to_score(part1,score)

  part2 = []
  for i in xrange(0,beats):
    part2.append(choose_random_note_in_range(scale2.notes))
  score = add_to_score(part2,score)

  make_abjad_segment(score)

main()
