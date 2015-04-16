#from distutils.core import setup
from setuptools import find_packages, setup
setup(name='csd',
      version='0.0.4',
      description='Csound csd Python Package',
      author='Jacob Joaquin',
      author_email='jacobjoaquin@gmail.com',
      url='http://jacobjoaquin.github.io/csd/pysco.html',
      packages=['csd', 'csd.orc', 'csd.sco', 'csd.sco.element',
                'csd.sco.event', 'csd.sco.selection', 'csd.pysco'],
      )

