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

Download
--------

`Download as Zip <https://github.com/jacobjoaquin/csd/zipball/master>`_

`Download as TAR ball <https://github.com/jacobjoaquin/csd/tarball/master>`_

Clone from Github::

    git clone git://github.com/jacobjoaquin/csd.git

Install
-------

In a terminal window, cd to the csd folder and type::

	python setup.py install

On Linux, Unix, and OS X, you may need to sudo it::

	sudo python setup.py install

Test
----

You can test to see if installation was successful running the script
test.py, found in the demo folder::
    
    ./test.py
    
If this runs without throwing any errors, then you should be good to
go.

Supported Systems
-----------------

The only system in which csd is tested on is OS X 10.8 running
Python 2.7.  At this time, compatibility among the various platforms
is unknown. This includes installation issues.  Whether you manage
to install successfully, or if you run into issues, please email
me your results so I can make improvements in future releases:
jacobjoaquin@gmail.com



