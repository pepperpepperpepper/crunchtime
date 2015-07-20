#!/usr/bin/env node
var _s = require('underscore.string');

function Scale(){
  this.current_note = "";
  this.current_octave = []; 


}


function Note(){
  this.name = 'C'
  this.current = this.name //an alias for convenience
  this.all_notes = [ 'C','Db','D','Eb','E','F','F#','G','Ab','A','Bb','B' ];
  this.halfsteps_up = function(halfsteps_count){
    var total = this.all_notes.length -1;
    var idx = this.all_notes.indexOf(this.name) + halfsteps_count;
    while(idx > total){
      idx -= this.all_notes.length
    } 
    this.name = this.all_notes[idx];
  }
  this.halfsteps_down = function(halfsteps_count){
    var total = this.all_notes.length -1;
    var idx = this.all_notes.indexOf(this.name) - halfsteps_count;
    while(idx < 0){
      idx += this.all_notes.length
    } 
    this.name = this.all_notes[idx];
  }
  this.build_scale_by_halfsteps_down = function(halfsteps_array, starting_pitch){
    if (typeof (starting_pitch) === 'undefined') starting_pitch = this.name;
    this.name = starting_pitch;
    var s = new Scale();
    s.current_note = this.name;
    halfsteps_array.forEach(function(steps){
      this.halfsteps_down(steps);
      console.log(_s.sprintf("steps: %s, name: %s", steps,this.name));
    }.bind(this));
    this.name = original_note;
  }
  this.build_scale_by_halfsteps_up = function(halfsteps_array, starting_pitch){
    if (typeof (starting_pitch) === 'undefined') starting_pitch = this.name;
    this.name = starting_pitch;
    var original_note = this.name;
    halfsteps_array.forEach(function(steps){
      this.halfsteps_up(steps);
      console.log(_s.sprintf("steps: %s, name: %s", steps,this.name));
    }.bind(this));
    this.name = original_note;
  }
}

var mynote = new Note();

var Scales = {
  pentatonic_minor : [ 0, 3, 2, 2, 3 ],
  ionian : [ 0, 2, 2, 1, 2, 2, 1 ],

}
mynote.build_scale_by_halfsteps_up(Scales.pentatonic_minor, 'A')
//mynote.build_scale_by_halfsteps_down(pentatonic, 'A')


