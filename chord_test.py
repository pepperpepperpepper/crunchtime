#!/usr/bin/python2.7
import os, sys
import random
from abjad import *
from lib import render_all
from lib.note_constants import *
from lib.Chord import Chord
import time
import os
from subprocess import call

def choose_random_note_in_range(notes, upper_limit=20, lower_limit=0):
  choice = None
  note_number = None
  while not (note_number < upper_limit and note_number > lower_limit):
    choice = random.choice(notes)
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
  measures = 50;
  beats = 4 * measures
  
  tempo = Tempo(Duration(1, 4), 360)
  attach(tempo, score)
  
  chord1 = Chord(C, name="major_major7");
  chord2 = Chord(G, name="major_minor7");
  part1 = []
  for i in xrange(0,beats):
    if i % 3:
      part1.append(choose_random_note_in_range(chord2.notes_all))
    else:
      part1.append(choose_random_note_in_range(chord1.notes_all))
  score = add_to_score(part1,score)

  part2 = []
  for i in xrange(0,beats):
    if i % 3:
      part2.append(choose_random_note_in_range(chord2.notes_all))
    else:
      part2.append(choose_random_note_in_range(chord1.notes_all))
  score = add_to_score(part2,score)

  render_all(score, clean=True, play=True, preview=True)

main()
