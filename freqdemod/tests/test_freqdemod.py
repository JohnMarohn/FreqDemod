#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# John A. Marohn (jam99@cornell.edu)
# 2014/06/28

"""

Tests for the demodulate module. 

"""

# if a function is *expected *to fail, then
#
#    @unittest.expectedFailure
#    def test_that_fails():
#

from freqdemod.demodulate import Signal
import unittest
import numpy as np
# import logging
# import os
# import re



class InitLoadSaveTests(unittest.TestCase):
    """
    Make sure the *Signal* object is set up correctly.
    """

    def setUp(self):
        """
        Create an empty *Signal* object
        """
        
        self.s = Signal()

    def test_init(self):
        """Signal object initialized"""

        self.assertEqual(self.s.report[0],'Empty Signal object created')

    def test_load_nparray(self):
        """Signal.load_nparray saves the array"""
        
        self.s.load_nparray(np.arange(3),"x","nm",10E-6)        
        self.assertTrue(np.allclose(self.s.signal['s'],np.array([0, 1, 2]), rtol=1e-05, atol=1e-08))
        
