%%%%%%%%%%%%%%
Installing csd
%%%%%%%%%%%%%%

The csd installer is built using the Python Distribution Utilities
("Distutils").  This source distribution will install only the python
modules within the csd package heirarchy.  Demo examples, test scripts
and documentation are not installed.

For complete instructions on installing python packages, refer to
`Installing Python Modules <http://docs.python.org/install/>`_ in the
Python on-line docs.

Quick Instructions
------------------

After downloading the csd tar file, you can install csd in using the
following command-lines in a terminal window::

    gunzip -c csd-x.x.x.tar | tar xf -
    cd csd-x.x.x
    python setup.py install

.. note:: Some systems, including OS X, allow you to unpack the contents
    of the tar files by double clicking on the file in the Finder.

Test
----

You can test to see if installation was successful running the script
test.py, found in the demo folder::
    
    ./test.py
    
If this runs without throwing any errors, then you should be good to
go.

Supported Systems
-----------------

The only system in which csd is tested on is OS X Leopard running
Python 2.5.1.  At this time, compatibility among the various
platforms is unknown. This includes installation issues.  Whether
you manage to install successfully, or if you run into issues,
please email me your results so I can make improvements in future
releases: jacobjoaquin@gmail.com



