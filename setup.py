#!/usr/bin/env python
from distribute_setup import use_setuptools
use_setuptools()

#python setup.py sdist upload

from setuptools import setup
from stratum import version

setup(name='stratum',
      version=version.VERSION,
      description='Stratum server implementation based on Twisted',
      author='MERP Solutions',
      author_email='info@merp.nl',
      url='http://www.merp.nl/stratum',
      packages=['stratum',],
      py_modules=['distribute_setup',],
      zip_safe=False,
      install_requires=['twisted', 'ecdsa', 'autobahn',]
     )
