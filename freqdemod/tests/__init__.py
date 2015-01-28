"""
This module will collect tools for unit testing the functions in the 
``FreqDemod`` package. Unit tests were developed using the ``unittest`` package.  
To run the unit tests, open up a terminal in the ``FreqDemod`` directory and 
run either::

    python -m unittest discover 
    (or python -m unittest discover --verbose)

or::

    nosetests
    (or nosetests -v
     or notetests -sv)

In some of the unit tests, we compare two ``numpy`` arrays.  In developing this 
comparison we found the stackoverflow discussion "Comparing numpy float arrays
in unit tests" helpful [`link <http://stackoverflow.com/questions/14920837/comparing-numpy-float-arrays-in-unit-tests>`__].

"""

import os
import unittest


def testsuite():
    """Automatically discover all tests in this folder."""
    return unittest.TestLoader().discover(os.path.dirname(__file__))


def test():
    """Run all tests.

    :return: a :class:`unittest.TestResult` object
    """
    test_runner = unittest.TextTestRunner()
    return test_runner.run(testsuite())
