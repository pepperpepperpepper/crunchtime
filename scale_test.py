#!/usr/bin/python2.7
import os, sys
import random
from abjad import *
from lib import render_all
from lib.note_constants import *
from lib.Scale import Scale
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
  
def main():
  score = Score([]);
  measures = 20;
  beats = 4 * measures
  
  tempo = Tempo(Duration(1, 4), 240)
  attach(tempo, score)
  
  scale1 = Scale(D, name="minor_pentatonic");
  scale2 = Scale(G, name="minor_pentatonic");
  part1 = []
  for i in xrange(0,beats):
    part1.append(choose_random_note_in_range(scale1.notes))
  score = add_to_score(part1,score)

  part2 = []
  for i in xrange(0,beats):
    part2.append(choose_random_note_in_range(scale2.notes))
  score = add_to_score(part2,score)

  render_all(score, clean=True, play=True, preview=True)

main()
