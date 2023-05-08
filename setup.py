#!/usr/bin/env python
# Enables the package to be used in develop mode
# See http://pythonhosted.org/setuptools/setuptools.html#development-mode
# See https://github.com/scikit-learn/scikit-learn/issues/1016
# setuptools is included with pip; basically python standard at this point
import io
import os

from setuptools import setup, find_packages

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# On readthedocs, we can't install packages with compiled code
if on_rtd:
    install_requires = ['six >= 1.16.0']
else:
    install_requires = ['numpy >= 1.22.4', 'scipy >= 1.10.1', 'matplotlib >= 3.7.1', 'h5py >= 3.8.0', 'six >= 1.16.0', 'lmfit >= 1.2.1']

description = """Extract the time-dependent frequency of a sinusoidally oscillating signal."""

readme = io.open('README.rst', mode='r', encoding='utf-8').read()

doclink = """
Documentation
-------------

The full documentation is at https://freqdemod.rtfd.org."""

history = io.open('HISTORY.rst', mode='r',
                  encoding='utf-8').read().replace('.. :changelog:', '')

setup(name='FreqDemod',
      version='0.3.1',
      description=description,
      long_description=readme + '\n\n' + doclink + '\n\n' + history,
      author='John Marohn',
      license='GPLv3',
      author_email='jam99@cornell.edu',
      url='https://github.com/JohnMarohn/FreqDemod',
      packages=find_packages(),
      install_requires=install_requires,
      setup_requires=["setuptools_git >= 0.3"],
      tests_require=[],
      zip_safe=False,
      include_package_data=True,
      test_suite='freqdemod.tests.discover',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
      )
