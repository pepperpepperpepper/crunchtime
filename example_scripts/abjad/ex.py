#!/usr/bin/python2.7

from abjad import *
import copy
#score = Score([]);
#piano_staff = scoretools.StaffGroup([], context_name="PianoStaff");
#upper_staff = Staff([]);
#lower_staff = Staff([]);
#
#piano_staff.append(upper_staff);
#piano_staff.append(lower_staff);
#score.append(piano_staff);
#
#lower_measures = copy.deepcopy(upper_measures);
#upper_staff.extend(upper_measures)
#lower_staff.extend(lower_measures)
#
#upper_measures[0].extend("a'8 g'8 f'8 e'8");

import sys
score = Score([]);
scale = tonalanalysistools.Scale('c', 'major')
#FIND OUT DIFFERENCE BETWEEN PITCH SEGMENT AND PITCH CLASS SEGMENT
#just use containers, don't worry too much about segments
#expr = pitchtools.PitchSegment("d' c' e'")
expr = pitchtools.PitchClassSegment("c d e")
pitch = pitchtools.NamedPitch.from_hertz('459');
note = Note(pitch, .125);
notes = expr.make_notes(3);
container = Container(notes);
selection = SimultaneousSelection(container);
#like this
#Selection(Note("e'4"), Note("d'4"), Note("e'4"), Note("f'4"), Note("g'1"), Note("c'2."), Note('b8'), Note('a8'), Note('b1'))

sys.exit(0);
container.append(note);
pitch = pitchtools.NamedPitch.from_hertz('466');
note = Note(pitch, .125);
container.append(note);
pitch = pitchtools.NamedPitch.from_hertz('461');
note = Note(pitch, .125);
container.append(note);
pitch = pitchtools.NamedPitch.from_hertz('459');
note = Note(pitch, .125);
container.append(note);
pitch = pitchtools.NamedPitch.from_hertz('455');
note = Note(pitch, .125);
container.append(note);
pitch = pitchtools.NamedPitch.from_hertz('450');
note = Note(pitch, .125);
container.append(note);
pitch = pitchtools.NamedPitch.from_hertz('445');
note = Note(pitch, .125);
container.append(note);
pitch = pitchtools.NamedPitch.from_hertz('440');
note = Note(pitch, .125);
container.append(note);

#notes = scale.make_notes(16)
staff = Staff([ container ])
score.append(staff);

persist(score).as_midi('test2.midi');

persist(score).as_pdf('test2.pdf');
