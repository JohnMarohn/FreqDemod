#!/usr/bin/env python
# Enables the package to be used in develop mode
# See http://pythonhosted.org/setuptools/setuptools.html#development-mode
# See https://github.com/scikit-learn/scikit-learn/issues/1016
# setuptools is included with pip; basically python standard at this point
import io

from setuptools import setup, find_packages


description = """This package provides functions for analyzing and plotting the
time-dependent frequency and amplitude of a sinusoidally oscillating signal."""

readme = io.open('README.rst', mode='r', encoding='utf-8').read()

doclink = """
Documentation
-------------

The full documentation is at https://freqdemod.rtfd.org."""

history = io.open('HISTORY.rst', mode='r',
                  encoding='utf-8').read().replace('.. :changelog:', '')

setup(name='FreqDemod',
      version='0.2.1',
      description=description,
      long_description=readme + '\n\n' + doclink + '\n\n' + history,
      author='John Marohn',
      license='GPLv3',
      author_email='jam99@cornell.edu',
      url='https://github.com/JohnMarohn/FreqDemod',
      packages=find_packages(),
      install_requires=['numpy', 'scipy', 'matplotlib', 'h5py',],
      setup_requires=["setuptools_git >= 0.3"],
      tests_require=['nose'],
      zip_safe=False,
      include_package_data=True,
      test_suite='nose.collector',
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
      )
