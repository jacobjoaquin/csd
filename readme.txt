Csound Score Processing Python Module
v0.0.1a 
-------------------------------------
By Jacob Joaquin

jacobjoaquin@gmail.com
http://www.thumbuki.com/
http://jacobjoaquin.tumblr.com/
http://twitter.com/JacobJoaquin

copyright (c) Jacob Joaquin 2009
-------------------------------------




This is an early release of the score module for processing Csound
score code.

This python module along with the command-line demos accepts Csound
score code at the standard input and processes them.

This package is currently a rough draft, and development will
definitely continue for the near future.  There are some definite
quirks, which will eventually be ironed out.

score.py contains the core functions that can be used to create
custom python scripts.  Everything is in a state of flux, so do
expect things to chage.

In the demo folder, you'll find five demo scripts: align.py,
arpeggiator.py, carry.py and swap_columns.py.  There are descriptions
beloew.  These scripts aren't thoroughly test, but you still may
find them useful.  align.py is probably the most reliable at the
moment.

In the test folder, there are many py scripts used to test the
functions defined in score.py.



Warning!!
---------
These scripts are still experimental.  Back up any Csound work you
plan on running through these scripts.



License
-------
LGPL



Demos
-----
Using the Terminal in OS X:
    Change directory to the score/demo/ directory to run these.


    Chaining pipes - Link multipe processes together to save steps.
    
        (Aligns score after processing it with sum.py)
    
        $cat carry.sco | ./sum.py -si -i2 -p4 -v0.99999 | ./align.py

    
    
    align.py - Aligns i-events in score
    
        $ cat unfactored.sco | ./align.py 
    
    
        (with optional flags)
    
        $ cat unfactored.sco | ./align.py -i0 -p2 -c4
        $ cat unfactored.sco | ./align.py -m6
    
    
        (using score code copied into the pasteboard)
    
        $ pbpaste | ./align.py 
        
    
        (copy results into pasteboard for pasting back into your text editor)
    
        $ pbpaste | ./align.py | pbcopy


      -i IPAD, --ipad=IPAD  amount of whitespace between i and instr number/name
      -p PFIELDPAD, --pfieldpad=PFIELDPAD
                            amount of whitespace between pfields
      -c COMMENTPAD, --commentpad=COMMENTPAD
                            amount of whitespace between last pfield and comment
      -m MINPFIELDWIDTH, --min-pfield-width=MINPFIELDWIDTH
                            minimum pfield width

                            
                            
    arpeggiator.py - Replaces pfields in a column, cycling through specified
                    values.
                    
        $ cat arp.sco | ./arpeggiator.py -si -i2 -p5 -v"7.00 7.03 7.07 7.10"

        
        -s STATEMENT   statement.  (i for ievent, f for function table event)
        -i IDENTIFIER  identifier  (instrument number or function table)
        -p PFIELD      pfield      (pfield to arpeggiate)
        -v VALUES      values      (quoted list of values to cycle through)


        
    carry.py - Converts duplicate values in proceeding pfields to the carry
               symbol.  (.)
               
        $ cat carry.sco | ./carry.py
        

        NO FLAG OPTIONS
        
        
        
    sum.py - Sums the specified value (-v) with existing pfield values.
    
        $ cat carry.sco | ./sum.py -si -i2 -p4 -v0.999


        -s STATEMENT   statement   (i for ievent, f for function table event)
        -i IDENTIFIER  identifier  (instrument number or function table)
        -p PFIELD      pfield      (pfield to sum)
        -v VALUE       value       (value to sum pfield with)

        
        
    swap_columns.py - Swaps two pfield columns.    
    
        (Swaps pfield columns 4 and 5 for instrument 1 events)
        
        $ cat swap.sco | ./swap_columns.py -si -i1 -a4 -b5

        
        -s STATEMENT  statement  (i for ievent, f for function table event)
        -i INSTR      instr      (instrument number or function table)
        -a PFIELD_A   pfield a   (Pfield column index)
        -b PFIELD_B   pfield b   (Pfield column index)
        
        
