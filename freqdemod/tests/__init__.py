"""
This module collects tools for unit testing the functions in the
``FreqDemod`` package. Unit tests were developed using the ``unittest``
package. To run the unit tests, open a terminal in the ``FreqDemod`` directory
and run either::

    python -m unittest discover
    (or python -m unittest discover --verbose)

or::

    python setup.py test

In some of the unit tests, we compare two ``numpy`` arrays.  In developing this
comparison we found the stackoverflow discussion "Comparing numpy float arrays
in unit tests" helpful [`link <http://stackoverflow.com/questions/14920837/comparing-numpy-float-arrays-in-unit-tests>`__].

"""

import os
import unittest


def discover():
    """Automatically collect all tests in this folder."""
    return unittest.TestLoader().discover(os.path.dirname(__file__))


def main():
    """Run all tests.

    :return: a :class:`unittest.TestResult` object
    """
    test_runner = unittest.TextTestRunner()
    return test_runner.run(discover())
