#!/usr/bin/python2.7
import os, sys
from subprocess import call
import random
import abjad
from lib.Renderer.Abjad import RendererAbjad
from lib.Note.Constants import *
from lib.Theory.Chord import Chord
from lib.Audio.Player import AudioPlayer
from lib.Renderer.Audio.Fluidsynth import RendererAudioFluidsynth

def choose_random_note_in_range(notes, upper_limit=20, lower_limit=0):
  choice = None
  note_number = None
  while not (note_number < upper_limit and note_number > lower_limit):
    choice = random.choice(notes)
    note_number = choice.number
  return choice 

def notes_to_quarternotes(notes):
  return map(lambda n: abjad.Note(n.number, abjad.Duration(1,4)), notes)

def add_to_score(notes,score):
  notes = notes_to_quarternotes(notes) 
  container = abjad.Container(notes);
  staff = abjad.Staff([ container ])
  score.append(staff);
  return score
  
def main():
  score = abjad.Score([]);
  measures = 50;
  beats = 4 * measures
  
  tempo = abjad.Tempo(abjad.Duration(1, 4), 240)
  abjad.attach(tempo, score)
  
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

  abjad_renderer = RendererAbjad(clean=True, verbose=True)
  abjad_renderer.render(score, preview=False)
  audio_renderer = RendererAudioFluidsynth();  
  file_audio = audio_renderer.render(abjad_renderer.file_midi)
  audio_player = AudioPlayer();
  audio_player.play(file_audio)

main()
