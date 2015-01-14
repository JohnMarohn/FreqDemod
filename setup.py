#!/usr/bin/env python
# Enables the package to be used in develop mode
# See http://pythonhosted.org/setuptools/setuptools.html#development-mode
# See https://github.com/scikit-learn/scikit-learn/issues/1016
# setuptools is included with pip; basically python standard at this point
from setuptools import setup

setup(name='FreqDemod',
      version='0.2',
      description='',
      author='John Marohn',
      author_email='jam99@cornell.edu',
      packages=['freqdemod'],
      install_requires=['numpy', 'scipy', 'matplotlib', 'h5py',],
      tests_require=['nose'],
      zip_safe=False,
      include_package_data=True,
      test_suite='nose.collector',
      )
