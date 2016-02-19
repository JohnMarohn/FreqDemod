#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# John A. Marohn (jam99@cornell.edu)
# 2014/06/28

"""

Tests for the hdf5 module. In writing units tests, it is crucially important
to remember that the unittest object is recreated *every function call* 
[`see here <http://stackoverflow.com/questions/10570307/self-attr-resets-between-tests-in-unittest-testcase>`__].
You thus cannot expect, say, ``self.f`` to retain a value if it is passed
between functions.  You cannot pass a value between functions this way if
your object is a ``unittest`` object.  

You *can* pass values from the ``setUp`` function to other functions, because
the ``setUp`` function is called once before every other function in the class.
Likewise the ``tearDown`` function.  

There *is* a way to pass data between functions in a ``unittest`` onject.
This requires use of the special ``setUpClass``, illustrated below in the 
object ``Test_disk_data2``.  This test mimics how we would like to use 
HDF5 data: open file on disk, pass the data between object methods, reading
and writing the data as needed.

**Additional Resources**


* HDF5 Command-line Tools [`link <http://www.hdfgroup.org/products/hdf5_tools/>`__]

* h5ls command line tool [`link <http://www.hdfgroup.org/HDF5/doc/RM/Tools.html#Tools-Ls>`__]

"""
from __future__ import division, print_function, absolute_import
import unittest
import h5py
import numpy as np
from numpy.testing import assert_array_equal
import datetime

from freqdemod.util import silent_remove
from freqdemod.hdf5 import (update_attrs)

class Test_update_attrs(unittest.TestCase):
    """Test the helper function update_attrs"""
    filename = '.Test_update_h5_attrs.h5'

    def setUp(self):
        self.f = h5py.File(self.filename, 'w')
        self.f.attrs['to-be-overwritten'] = 'initial'

    def test_overwrite(self):
        """The function *should* overwrite existing attributes"""
        attrs = {'to-be-overwritten': 0}
        update_attrs(self.f.attrs, attrs)
        assert self.f.attrs['to-be-overwritten'] == 0

    def test_normal_write(self):
        """Writing a non-empty dictionary should do something"""
        attrs = {'one': 1}
        update_attrs(self.f.attrs, attrs)
        assert self.f.attrs['one'] == 1

    def test_empty_write(self):
        """Writing an empty dictionary should do nothing."""
        empty_attrs = {}
        update_attrs(self.f.attrs, empty_attrs)
        assert self.f.attrs['to-be-overwritten'] == 'initial'

    def tearDown(self):
        """Close the h5 file, and remove the file for the next iteration."""
        self.f.close()
        silent_remove(self.filename)

class Test_memory_data(unittest.TestCase):
    """Write to memory, read, close; Write to memory, read, close; etc""" 
    
    filename = '.Test_update_h5_data.h5'
    
    def setUp(self):
        self.f = h5py.File(self.filename, 'w', driver = 'core')
        dset = self.f.create_dataset('x',np.arange(2))
        dset.attrs['unit'] = 'nm'      
                
    def test_array_read(self):
        """Open in memory, write, read array, close"""
        self.assertTrue(np.allclose(self.f['x'],np.array([0, 1])))
        
    def test_attr_read(self):
        """Open in memory, write, read attribute, close"""
        self.assertEqual(self.f['x'].attrs['unit'],'nm')
        
    def tearDown(self):
        """Close the h5 file, and remove the file for the next iteration."""
        self.f.close()
        silent_remove(self.filename)

class Test_disk_data(unittest.TestCase):
    """Write to disk, open, read, close; Write to disk, open, read, close; etc"""     
         
    filename = '.Test_update_h5_data.h5'
    
    def setUp(self):
        self.f = h5py.File(self.filename, 'w')
        dset = self.f.create_dataset('x',np.arange(2))
        dset.attrs['unit'] = 'nm'
        self.f.close()      
        
    def test_01_read(self):
        """Open file from disk, read array, close"""
        self.g =  h5py.File(self.filename, 'r')
        self.assertTrue(np.allclose(self.g['x'],np.array([0, 1])))
        self.g.close()
          
    def test_02_read(self):
        """Open file from disk, read attribute, close"""
        self.g =  h5py.File(self.filename, 'r')
        self.assertEqual(self.g['x'].attrs['unit'],'nm')
        self.g.close()     

    def tearDown(self):
        """Remove the file for the next iteration."""
        silent_remove(self.filename)               

class Test_disk_data2(unittest.TestCase):
    """Write once to disk, open once from disk, read, write, read, close.
    Leave the file intact to we can examine it by calling::
    
        h5ls -v .Test_disk_data2.h5

    """

    def setUpClass(cls):

        cls.filename = '.Test_disk_data2.h5'
    
        f = h5py.File(cls.filename, 'w')
        dset = f.create_dataset('x',np.arange(2))
        dset.attrs['unit'] = 's'
        f.close()  
    
        cls.g = h5py.File(cls.filename, 'r+')

    setUpClass = classmethod(setUpClass)
        
    def test_01_read(self):
        """Read array"""
        self.assertTrue(np.allclose(self.g['x'],np.array([0, 1])))
          
    def test_02_read(self):
        """Read attribute"""
        self.assertEqual(self.g['x'].attrs['unit'],'s')
        
    def test_03_write(self):
        """Write new attribute"""
        dset = self.g.create_dataset('y',0.5*np.arange(2))
        dset.attrs['unit'] = 'nm'
        
    def test_04_read(self):
        """Read new attribute"""
        self.assertEqual(self.g['y'].attrs['unit'],'nm')
                              
    def tearDownClass(cls): 
    
        cls.g.close()                                                                                                                                                                                                                   
            
    tearDownClass = classmethod(tearDownClass)

class Test_update_attrs_extended(unittest.TestCase):
    """
    Read and write an x and y dataset representing a cantilever oscillation.
    Use an HDF5 file format that Dwyer, Marohn, and Harrell have agreed upon (with
    minor modifications).  This class's unit tests create a hidden HDF5 whose 
    contents can be examined using the command-line call:: 
    
            h5ls -v .Test_update_attrs_extended.h5
            
    The function ``test_02_read`` reads the h5 file and prints out its contents.
    The outputs of print statements are usually swallowed during the unit test.
    To display the informative print statements, you can initiate unit testing
    using the following command::
    
            nosetests -sv
    """


    filename = '.Test_update_attrs_extended.h5'

    def setUp(self):
        """"Record the date and time for use by the functions below. 
        Delete the output file if it exists so we can make it anew.
        """

        silent_remove(self.filename)

        today = datetime.datetime(2014, 7, 31, 18, 29, 12, 137998)

        self.date = today.strftime("%Y-%m-%d")
        self.time = today.strftime("%H:%M:%S")

        self.dt = 10.0E-6
        self.t = self.dt * np.arange(32*1024)

        self.x_attrs = {'name': 't',
                        'unit': 's',
                        'label': 't [s]',
                        'label_latex': '$t \\: [\\mathrm{s}]$',
                        'help': 'time axis',
                        'initial': self.t[0],
                        'step': self.t[1] - self.t[0]}

        self.y_attrs = {'name': 'x',
                        'unit': 'nm',
                        'label': 'x [nm]',
                        'label_latex': '$x \: [\mathrm{nm}]$',
                        'help': 'cantilever amplitude',
                        'abscissa': 'x',
                        'n_avg': 1}

        self.f_attrs = {'date': self.date,
                        'time': self.time,
                        'h5py_version': h5py.version.version,
                        'source': 'test_hdf5.py',
                        'help': 'This is a test file created during unit testing'}

        self.write_h5file()

    def write_h5file(self):
        """Write the representative dataset to a file."""

        f = h5py.File(self.filename, 'w')

        update_attrs(f.attrs, self.f_attrs)

        f['x'] = self.t

        update_attrs(f['x'].attrs, self.x_attrs)

        f0 = 0.013/(2*self.dt)
        self.y = np.sin(2*np.pi*f0*self.t)

        f['y'] = self.y

        update_attrs(f['y'].attrs, self.y_attrs)

        f.close()

    def test_read(self):
        """
        Read the representative dataset from disk, and compare with the data / attributes written.
        """

        f = h5py.File(self.filename, 'r')

        assert_array_equal(f['x'][:], self.t)
        assert_array_equal(f['y'][:], self.y)

        self.assertEqual(dict(f['x'].attrs), self.x_attrs)
        self.assertEqual(dict(f['y'].attrs), self.y_attrs)
        self.assertEqual(dict(f.attrs), self.f_attrs)

        f.close()

    def tearDown(self):
        silent_remove(self.filename)


if __name__ == '__main__':

    unittest.main(verbosity=2)
