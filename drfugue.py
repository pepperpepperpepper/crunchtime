#!/usr/bin/python2.7
import simplejson as json
import os, sys, time
from subprocess import call
import random
from abjad import *
from lib import Scale, render_all

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

#def choose_harmony(previous_harmony, overall_harmony):
#  upper_limit = 20;
#  lower_limit = 0;
#  choice = None
#  note_number = None
#  while not (note_number < upper_limit and note_number > lower_limit):
#    choice = random.choice(scale)
#    note_number = choice["pitch_number"]
#  return choice 

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

def main():
  score = Score([]);

  measures_total = 32;  
  beats_total = measures_total * 4;
  bpm = 240;

  tempo = Tempo(Duration(1, 4), bpm)
  attach(tempo, score)

  scale1 = Scale("minor_pentatonic", D);
  scale2 = Scale("minor_pentatonic", G);

  notes_to_use = []
  for i in xrange(0,20):
    notes_to_use.append(choose_random_note_in_range(scale1.notes))
  score = add_to_score(notes_to_use,score)
  notes_to_use = []
  for i in xrange(0,20):
    notes_to_use.append(choose_random_note_in_range(scale2.notes))
  score = add_to_score(notes_to_use,score)

  render_all(score, clean=True)

main()
