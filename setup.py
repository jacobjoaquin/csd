from distutils.core import setup

setup(name='csd',
      version='0.0.3.1',
      description='Csound csd Tools',
      author='Jacob Joaquin',
      author_email='jacobjoaquin@gmail.com',
      url='http://www.thumbuki.com/',
      packages=['csd', 'csd.orc', 'csd.sco', 'csd.sco.element',
                'csd.sco.event', 'csd.sco.selection'],
      )

