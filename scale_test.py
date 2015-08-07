#!/usr/bin/python2.7
import os, sys
import random
import abjad
from lib.Renderer.Abjad import RendererAbjad
from lib.Note.Constants import *
from lib.Theory.Scale import Scale
from lib.Renderer.Audio.Player import RendererAudioPlayer
from lib.Renderer.Audio.Fluidsynth import RendererAudioFluidsynth
import time
from subprocess import call


def choose_random_note_in_range(scale):
  upper_limit = 20;
  lower_limit = 0;
  choice = None
  note_number = None
  while not (note_number < upper_limit and note_number > lower_limit):
    choice = random.choice(scale)
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
  measures = 20;
  beats = 4 * measures
  
  tempo = abjad.Tempo(abjad.Duration(1, 4), 240)
  abjad.attach(tempo, score)
  
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

  abjad_renderer = RendererAbjad(clean=True, verbose=True)
  abjad_renderer.render(score, preview=False)
  audio_renderer = RendererAudioFluidsynth();  
  file_audio = audio_renderer.render(abjad_renderer.file_midi)
  audio_player = RendererAudioPlayer();
  audio_player.play(file_audio)

main()
