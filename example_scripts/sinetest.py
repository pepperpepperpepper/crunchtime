#!/usr/bin/python2.7 
#import wave
#wave_write = wave.open('sinetest.wav', 'wb')
#wave_write.setnchannels(1)
#wave_write.setsampwidth('


import wave, struct, math

sampleRate = 44100.0 # hertz
duration = 1.0       # seconds
frequency = 440.0    # hertz

wavef = wave.open('sound.wav','w')
wavef.setnchannels(1) # mono
wavef.setsampwidth(2) 
wavef.setframerate(sampleRate)

for i in range(int(duration * sampleRate)):
    #so first we have cos/sin function, it accept value in radians, that means we need to *mpath.pi to get value from "i" we have (which is increasing with each sample)
    cos( freq * pi )
    #float(i)/float(samplerate) is basically just so i won't be very big and overflow, sort of  mod (%) operation on i here.
    #next is 32767 part.  we have  two channels here, that means that we need to write two bytes, one for each channel. two bytes can have values from 0 to 65535,
    #but cos/sin will return value from -1 to 1, so we need only half from 65535, which is 32767.
    # next we just make an int from it, and do struct.pack which is basically converting an int into string with two bytes.
    #ok well the part that I understood off the bat was the conversion from radians. Why do we need half? is that the nyquist theorem or something?
    #well two bytes hcan have from 0 to 65535, so if we for example  have -1 from cos() function we get  -1 * 32767, if we have  1 we will get 32767. both of them
    # fit into two bytes. if it was 65535, it would truncate. I think I actually get it! ok

    #ok so the struct.pack still not sure about that one, why a string? wave module want a string, just two or more bytes depending on channel settings. if we have
    # like 16 channells there would be no int which could hold info for all of them, so module use strings to hold it. got it
    #ok so the last thing is the samplewidth, why exactly is it 2? it's two bytes, so sample can have values from -32767 to 32767, it's 16-bit audio. so that
    #just allows it to store the info at sort of a higher resolution (than 1, which would be 8 bit audio)? yep ok awesome
    #so to do more sophisticated synthesis with this, well for one I could adjust the amplitude of the cos function, right? yep. and then I could create a function
    #of my own that modulates that...well anyway, I think I know where to go from here. this is awesome
    #so we are dealing with mono here, right? yep that's just because we're writing the same thing to both channels, or are we only writing to one channel? only one channel
    #if I wanted to have more than one pitch simultaneously, what do I do, add them? yes so value += the same calculation with the other frequency? yep ok awesome
    #alright this is all I needed help with for now, I'll let you know how it goes? actually...one last question



    #so this is NOT wavetable synthesis, right? nope ok but soundfonts are? so the soundfont library uses the a short sample, and just repeats it at the different
    #frequency rates to produce audio? yes if we were going to make this into a primitive wavetable synth, we would just write one frame to disk, and keep information
    #about how fast we would need to repeat that frame to produce audio? well yeah, it's same a function below, just instead of calulcating cos/sin we get raw wav frames
    #from sample file. ok awesome. thanks a lot for the help! this was great no problems
    value = int(32767.0*math.cos(frequency*math.pi*float(i)/float(sampleRate))) #ok these two lines are confusing me here
    data = struct.pack('<h', value)
    wavef.writeframesraw( data )

wavef.writeframes('')
wavef.close()
is this it? yep ok let's make sure I know what's going on
