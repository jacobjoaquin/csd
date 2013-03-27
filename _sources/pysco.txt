#####
Pysco
#####

*"All composers should be as lazy as possible when writing scores."* - Max V. Mathews

What is Pysco?
==============

Pysco is a modular Csound score environment for event generation, event processing, and the fashioning musical structures in time.

..
    Pysco is non-imposing and does not force composers into any one particular compositional model; Composers design their own score frameworks by importing from existing Python libraries, or fabricate their mechanisms own as needed. It is 100% compatible with the classical Csound score, and runs inside a unified CSD file.

    Pysco is designed to be a giant leap forward from the classical Csound score by leveraging Python, a highly extensible general-purpose scripting language. While the classical Csound score does feature a small handful of score tricks, it lacks common computer programming paradigms, offering little in terms of alleviating the tedious process of writing scores by hand. Python plus the Pysco interface transforms the limited classical score into highly flexible and modular text-based compositional environment.

The details documentation is still being worked out. In the meantime, check out this algorithmic Amen loop generator:

.. raw:: html

    <iframe width="100%" height="166" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=http%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F42750779"></iframe>

.. literalinclude:: ../../demo/pysco/drum3.csd

