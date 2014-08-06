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
# import h5py

class InitLoadSaveTests(unittest.TestCase):
    """
    Make sure the *Signal* object is set up correctly.
    """

    def setUp(self):
        """
        Create an trial *Signal* object
        """
        
        self.s = Signal('.InitLoadSaveTests_1.h5')
        self.s.load_nparray(np.arange(3),"x","nm",10E-6)

    def test_report(self):
        """Initialize Signal object"""

        self.assertEqual(self.s.report[0],'HDF5 file .InitLoadSaveTests_1.h5 created in core memory')

    def test_x(self):
        """Check x-array data."""
              
        self.assertTrue(np.allclose(self.s.f['x'],10E-6*np.array([0, 1, 2]), rtol=1e-05, atol=1e-08))

    def test_y(self):
        """Check y-array data."""
        
        self.assertTrue(np.allclose(self.s.f['y'],np.array([0, 1, 2]), rtol=1e-05, atol=1e-08))
    
    def test_close(self):
        """Verify closed object by testing one of the attributes"""
        
        self.s.close()
        self.snew = Signal()
        self.snew.open('.InitLoadSaveTests_1.h5')
        
        # print out the contents of the file nicely        
                                
        report = []
        
        for key, val in self.snew.f.attrs.items():
            report.append("{0}: {1}".format(key, val))
        
        for item in self.snew.f:
            
            report.append("{}".format(self.snew.f[item].name))
            for key, val in self.snew.f[item].attrs.items():
                report.append("    {0}: {1}".format(key, val))
        
        report_string = "\n".join(report)
        
        print "\nObjects in file .InitLoadSaveTests_1.h5"
        print report_string

        # test one of the attributes

        self.assertTrue(self.snew.f.attrs['source'],'demodulate.py')
    
    def tearDown(self):
        """Close the h5 files before the next iteration."""
        try:
            self.s.f.close()
        except:
            pass
        try:
            self.snew.f.close()
        except:
            pass        
        
class MaskTests(unittest.TestCase):
    
    def setUp(self):
        """
        Create an trial *Signal* object
        """
        
        self.s = Signal('.InitLoadSaveTests_1.h5')
        self.s.load_nparray(np.arange(60000),"x","nm",10E-6)
        
    def test_binarate_1(self):
        """Binarate mask middle; test length is 2^n"""
        
        self.s.binarate("middle")
        m = self.s.f['mask/binarate']

        self.assertEqual(np.count_nonzero(m),32*1024)    
        
    def test_binarate_2(self):
        """Binarate mask start; test length is 2^n"""
        
        self.s.binarate("start")
        m = self.s.f['mask/binarate']

        self.assertEqual(np.count_nonzero(m),32*1024)   
        
    def test_binarate_3(self):
        """Binarate mask end test length is 2^n"""
        
        self.s.binarate("end")
        m = self.s.f['mask/binarate']

        self.assertEqual(np.count_nonzero(m),32*1024)   
 
    def tearDown(self):
        """Close the h5 files before the next iteration."""
        try:
            self.s.f.close()
        except:
            pass       