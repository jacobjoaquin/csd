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
* Need to make auto-installation happen.  Eggs?
* Tutorials on how to build custom scripts using this package.
* Spell check docs.
* Elements become atoms?
* Design decision?  Should selection operations be done internally? Or
  by leaving them exposed, let coders have a wider variety of choice
  when they themselves are creating their own custom function?
  
  As it is now::
      
      def add(x, y): return x + y
      selection = sco.select(score, {0: 'i', 1: '1'})
      selection = sco.operate_numeric(selection, 5, add, 1000)
      score = sco.merge(score, selection)
      
  As it could be::
      
      def add(x, y): return x + y
      score = sco.operate_numeric(score, {0: 'i', 1: '1'}, 5, add, 1000)
      
  Not that speed would probably ever be an issue, but I'm guessing case
  1 is more efficient.  Perhaps I can keep merge and select operations
  available, and then keep processing type functions, like
  operate_numeric, in a reduced form.
  
* Need a better name than pf_function.
* Need to use better names for pfield and pfield_list, as some of the
  terms currently trip over each other. pfield, pfield_index,
  pfield_index_list, etc...

