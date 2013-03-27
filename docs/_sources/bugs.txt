Bugs
=====

* In some of the test scores, there are some score string examples using
  single quotes.  Single quotes are not supported by the score.

* Test-cases need to be written for demos.

* Jython 2.5 fails some tests.

* The python interpreter didn't like passing a selection generated with
  csd.sco.select_all() to csd.sco.operate_numeric().

Planned Changes
===============

* Error checking, exceptions, and warnings - *Oh my!!*
* Need to get an online repository.  At least a somewhat official site.
* Look into eggs.
* Tutorials on how to build custom scripts using this package.
* Spell check docs.
* Elements become atoms?
* When dealing with dicts, make sure they are sorted. Had an issue with
  csd.sco.operate_numeric().
* selection functions needs a contractual flow.

    When a function receives a selection, a value in a key_index may
    contain multiple lines, and thus, the receiving function must
    operate on it.
    
    The value should be treated as a value_score.  A string containing
    one or more events.  Thus, it should be split.
    
    After the split, it can be processed.
    
    Before replacing the orignal value_score, the split needs to be
    joined, creating a single string, with newlines as evenet
    delimiters.
    

