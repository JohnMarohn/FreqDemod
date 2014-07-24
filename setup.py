#!/usr/bin/env python
# Enables the package to be used in develop mode
# See http://pythonhosted.org/setuptools/setuptools.html#development-mode
# See https://github.com/scikit-learn/scikit-learn/issues/1016
try:
    import setuptools
except ImportError:
    pass

from distutils.core import setup

setup(name='FreqDemod',
      version='0.2',
      description='',
      author='John Marohn',
      author_email='jam99@cornell.edu',
      packages=['freqdemod']
      )
