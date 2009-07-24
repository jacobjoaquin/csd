.. _glossary:

Glossary
========

.. glossary::

    csd
        #. A Csound unified file format that combines a Csound orc file
           and a Csound sco file into a single document.
          
        #. This package.
        
        #. In context of a function parameter, csd is a string that
           contains the contents of a Csound unified file.
          
        #. The top level module in the csd package.
        
    element
        Any :term:`event` data.  Can be numeric, an expression, macro,
        string, comment, a continuous block of space, carry, etc.
    
    event
        A single :term:`score` event. e.g. ``i 1 0 4 1.0 440  ; A440``.
    
    expression
        A Csound score expression, which is containted within brackets.
        e.g. ``[~ * 440 + 440]``
                
    identifier
        The unique name of index that indicates a specific instrument or
        f-table, and immediately proceeds a :term:`statement`. For example,
        ``33`` is the identifier in ``i 33 0 11``.
    
    literal
        A literal is any valid :term:`pfield data type`, such as:
        :term:`numeric`, :term:`expression`, macro, string, or
        preprocessor symbol.
    
    numeric
        A number.  Csound does not distinguish between ints and
        floats.  The term numeric refers to both.
        
    pattern
        A pattern is a python dict that has been repurposed to describe
        the conditions for matching against an :term:`event`.

        Pattern syntax::
            
            {pfield_index: ((string | numeric) | [(string | numeric), *]), *}

        The format is very precise, and must follow strict rules. The
        key is an integer that refers to the index of a pfield. The
        value is either a string, :term:`numeric`, or a list of strings
        and numbers. The values are used to compare against a
        :term:`pfield data type` from within an event.
        
        This system only works with pfield data types.  Whitespace and
        comments are not recognized.  If matching against a numeric
        type, the pattern matcher does distinguish between an integer
        and a floating point number.  i.e. 440 is not 440.0.
        
        Pattern examples::
            
            {0: 'i'}                   # All i-events
            {0: 'f'}                   # All f-tables
            {0: ['i', 'f']}            # All i-events and f-tables
            {0: 'i', 1: 33}            # All i-events for instr 33
            {0: 'i', 1: range(5, 11))  # All i-events for instrs 5 through 10
            {5: 440}                   # Events that contains 440 in pfield 5
        
    pfunction
        A function for operating on pfield values used in conjuction
        with csd.sco.operate_numeric. or csd.sco.map_().
        
        The first argument ``x`` is required, and is used as the pfield
        value in the function.  A pfunction supports any number of
        additional optional arguments.
        
        Example::
            
            def multiply(x, y):
                return x * y
            
            print csd.sco.map_(score, {0: 'i'}, 5, multiply, 3.0)
    
    pfield        
        A pfield, or parameter field, refers to a value as part of a
        :term:`event`.
            
    pfield data type
        Includes: :term:`statement`, :term:`numeric`, macro,
        :term:`expression`, string, and preprocessor symbols.

    pfield_index
        An integer that specifies a specific pfield in an event.

    pfield_index_list
        A pfield_index_list is either a single pfield index or a list
        of pfield indexes.  A pfield index is always an integer, and
        refers to a specific pfield. i.e. [6] refers to pfield 6 in the
        same way p6 does in a Csound orchestra.
        
    pfield_list
        A pfield_list is either a single pfield value or a list of
        pfield values.
        
        i.e. value, [value], or [value, value, ...].
        
        A pfield_list does not support a recursive list structure, i.e
        as [value, [value]].
        
    pgenerator
        DEFINE ME PLEASE
    
    selection
        A selection is a :term:`score` reformatted into a repurposed
        python dict that stores collected :term:`event` strings with
        their respective indexes.
       
        Selection syntax::
            
            {event_index: (event | [event, *]), *}
            
        The purpose of a selection is to be able to pull specific events
        from a :term:`score` and for processing.
        
        Selections are created with the select functions in csd.sco.
        Once they are processed, they must be recombined with the
        original score with the merge function.
            
    score
        #. The part of a Csound program that controls and plays a
           Csound orchestra.
        
        #. In context of a function, a score is a string of Csound
           score events.
               
    statement
        A statement is Csound score command that begins an active score
        :term:`event`.
        
        Statements include: (from the `Csound manual <http://www.csounds.com/manual/html/ScoreStatements.html>`_)
        
            * a - Advance score time by a specified amount
            * b - Resets the clock
            * e - Marks the end of the last section of the score
            * f - Causes a GEN subroutine to place values in a stored
              function table
            * i - Makes an instrument active at a specific time and for
              a certain duration
            * m - Sets a named mark in the score
            * n - Repeats a section
            * q - Used to quiet an instrument
            * r - Starts a repeated section
            * s - Marks the end of a section
            * t - Sets the tempo
            * v - Provides for locally variable time warping of score
              events
            * x - Skip the rest of the current section


