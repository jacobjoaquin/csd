#!/usr/bin/env python
'''Aligns groups of i-events.

.. program:: align
.. cmdoption:: -i  Pad amount between statement and identifier
.. cmdoption:: -p  Pad amount between pfields 1 and higher
.. cmdoption:: -c  Pad amount between last pfield and trailing comment
.. cmdoption:: -m  Minimum pad amount between pfields 1 and higher

Example::
    
    $ cat unfactored.sco | ./align.py -m4

Before::
    
    i1 0 4 6.04 15000 2 100 81 50 56 20 1 ; No alignment
    i1 + . . . . 101 . . . . . 
    i1 + . 5.04 . . 100 . . . . . 
    i1 + . . . . 101 . . . . . 
    i1 + . 6.04 . 2 100 . . . . . 
    i1 + . . . . 101 . . . . . 
    i1 + . 5.04 . . 100 . . . . . 
    i1 + . . . . 101 . . . . . 
    
    
    i1 0 1 0.1 8.00 0.5 0.333333  ; Begin new section
    i1 + . .   .    .   .  ; Comment
    i1 + . .   .    .   .  ; Another comment
    i1 + . .   .    0.75   .  ; And one more
    i1 10 0.44 0.99 5.05 0 1  ; Swap mix-rates of last 2 pfields
    i1 + 0.44 0.99 5.02 < <
    i1 + 0.44 [~ * 0.5 + 0.5] 5.01 < <  ; Expressions work
    i 1 + 0.44 [~ * 0.8 + 0.2] 5.00 < <
    i 1  + 0.44 . 5.00 < <
    i 1 + 0.6333 0.88 6.04 1 0
    
    
    i 7 16.4 3.5 8000 5.019 0.2 0.7 0.5 2 3 0.1 ; Mangled snippet from Trapped
    i 7 19.3 6.4 8000 5.041 . 0.9 1 3 2 0.1
    i 9 26.7 1.9 "file.wav" 4.114 . 0.1 5.9 300
    i 9 29.1 2.1 0.1 5.013 . 0.2 4.2 390
    i 99 32 6.2 0.28 ; Comments are aligned
    i 9 32 9.1 0.34 5.051 2300 0.5 3.8 420
    
    
    i "foo" 0 $macro 0 3 ; Strings and macros work
    i $bar 0 1 2 3  ; See.

After::
    
    i 1    0    4    6.04 15000 2    100  81   50   56   20   1  ; No alignment
    i 1    +    .    .    .     .    101  .    .    .    .    .
    i 1    +    .    5.04 .     .    100  .    .    .    .    .
    i 1    +    .    .    .     .    101  .    .    .    .    .
    i 1    +    .    6.04 .     2    100  .    .    .    .    .
    i 1    +    .    .    .     .    101  .    .    .    .    .
    i 1    +    .    5.04 .     .    100  .    .    .    .    .
    i 1    +    .    .    .     .    101  .    .    .    .    .
    
    
    i 1    0    1      0.1             8.00 0.5  0.333333  ; Begin new section
    i 1    +    .      .               .    .    .         ; Comment
    i 1    +    .      .               .    .    .         ; Another comment
    i 1    +    .      .               .    0.75 .         ; And one more
    i 1    10   0.44   0.99            5.05 0    1         ; Swap mix-rates of last 2 pfields
    i 1    +    0.44   0.99            5.02 <    <
    i 1    +    0.44   [~ * 0.5 + 0.5] 5.01 <    <         ; Expressions work
    i 1    +    0.44   [~ * 0.8 + 0.2] 5.00 <    <
    i 1    +    0.44   .               5.00 <    <
    i 1    +    0.6333 0.88            6.04 1    0
    
    
    i 7    16.4 3.5  8000       5.019 0.2  0.7  0.5  2    3    0.1  ; Mangled snippet from Trapped
    i 7    19.3 6.4  8000       5.041 .    0.9  1    3    2    0.1
    i 9    26.7 1.9  "file.wav" 4.114 .    0.1  5.9  300
    i 9    29.1 2.1  0.1        5.013 .    0.2  4.2  390
    i 99   32   6.2  0.28                                           ; Comments are aligned
    i 9    32   9.1  0.34       5.051 2300 0.5  3.8  420
    
    
    i "foo" 0    $macro 0    3  ; Strings and macros work
    i $bar  0    1      2    3  ; See.
'''

import re
import sys
#sys.path.append('../')  # Fix this.
#import score
from optparse import OptionParser

class AlignScore(object):    
    def __init__(self, block):
        self.__block = block
        self.__matrix = []
        self.__comments = {}
        self.__field_lengths = []

        #isValidInput()
        self.__clean_input()
        self.__create_matrix()
        self.__disjoin_comments()
        self.__create_field_lengths()
        
    def get_refactored_score(self, i_pad=1, field_pad=1, comment_pad=2,
            min_field_width=1, write_field_guide=False, field_delimit=" "):

        score_list = []

        # Add field guide
        if write_field_guide:
            fg = []
            fg.append(';')
            fg.append(field_delimit * i_pad)
            
            for i, field_width in enumerate(self.__field_lengths):
                field_width = max(field_width, min_field_width)
    
                fg.append(str(i).ljust(field_width, field_delimit),)                    
                fg.append(field_delimit * field_pad)
                
            score_list.append(''.join(fg))

        # Process each score row
        for row in self.__matrix:
            row_list = []
            
            # Add i
            row_list.append('i')
            row_list.append(' ' * i_pad)
            
            # Add fields
            for i, field in enumerate(row):
                field_width = max(self.__field_lengths[i], min_field_width)

                row_list.append(field.ljust(field_width, ' '),)                 
                row_list.append(' ' * field_pad)

            row_string = ''.join(row_list)
            row_string = row_string.rstrip();
            score_list.append(row_string)

        # Get longest row value, in characters
        longest_row_value = max(len(row) for row in score_list)
            
        # Add comments
        for key, comment in self.__comments.items():
            row_list = []

            row_list.append(score_list[key])
            row_list.append(' ' * (longest_row_value - len(score_list[key])))
            row_list.append(' ' * comment_pad)
            row_list.append(comment)
            score_list[key] = ''.join(row_list)

        return '\n'.join(score_list)
        
    def __create_field_lengths(self):
        # Pre-fill field_lengths with zeros
        self.__field_lengths = [0] * self.get_number_of_fields()

        for row in self.__matrix:
            for i, field in enumerate(row):
                self.__field_lengths[i] = max(len(field),
                        self.__field_lengths[i])

    def get_number_of_fields(self):
        return max(len(row) for row in self.__matrix)

    def get_number_of_lines(self):
        return len(self.__matrix)

    def __disjoin_comments(self):
        # Place comments into __comments and remove from __matrix
        
        for i, row in enumerate(self.__matrix):
            if row[-1].startswith(';'):
                self.__comments[i] = row[-1]
                row.pop()
                
    def __create_matrix(self):
        this_matrix = []

        # Pattern for pfields and a trailing comment
        p = re.compile('(\".+\"|\[.+\]|\;.+|\S+)')

        for line in self.__block:
            this_matrix.append(p.findall(line))

        self.__matrix = this_matrix

    def __clean_input(self):
        this_block = []

        # Convert string to list if necessary
        if isinstance(self.__block, basestring):
            self.__block = self.__block.splitlines()
            
        # Strip input
        for line in self.__block:
            line = line.strip()
            line = line.lstrip('i')
            line = line.lstrip()
            this_block.append(line)

        self.__block = this_block;

        
if __name__ == '__main__':
    # Get stdin
    stdin = sys.stdin.readlines()  # stdin
    block = []                     # Stores sequential i-events
    
    # Get command-line flags
    usage = "usage: <stdout> | %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-i", "--ipad", dest="ipad", default=1,
            help="amount of whitespace between i and instr number/name")
    parser.add_option("-p", "--pfieldpad", dest="pfieldpad", default=1,
            help="amount of whitespace between pfields")
    parser.add_option("-c", "--commentpad", dest="commentpad", default=2,
            help="amount of whitespace between last pfield and comment")
    parser.add_option("-m", "--min-pfield-width", dest="minpfieldwidth",
            default=1, help="minimum pfield width")
            
    (options, args) = parser.parse_args()
    
    # Limit range of flags
    ipad = max(0, int(options.ipad))
    pfieldpad = max(1, int(options.pfieldpad))
    commentpad = max(0, int(options.commentpad))
    min_pfield_width = max(1, int(options.minpfieldwidth))
    
    # Process each line
    for line in stdin:
        if line.startswith('i'):
            # Collect i-events
            block.append(line)
                
        else:   
            # Refactor block of i-events
            if block:
                score_block = AlignScore(block)
                print score_block.get_refactored_score(ipad, pfieldpad,
                                                       commentpad,
                                                       min_pfield_width)
    
                # Clean for next block
                block = []
                
            print line,
    
    # Refactor block of i-events
    if block:
        score_block = AlignScore(block)
        print score_block.get_refactored_score(ipad, pfieldpad, commentpad,
                                               min_pfield_width)




