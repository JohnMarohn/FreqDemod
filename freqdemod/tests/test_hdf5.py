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
import unittest
import h5py
import numpy as np
import datetime
from collections import OrderedDict

from freqdemod.util import silentremove
from freqdemod.hdf5 import (update_attrs)

class Test_update_attrs(unittest.TestCase):
    
    filename = '.temp_update_h5_attrs.h5'

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
        # silentremove(self.filename)
        
class Test_memory_data(unittest.TestCase):
    """Write to memory, read, close; Write to memory, read, close; etc""" 
    
    filename = '.temp_update_h5_data.h5'
    
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
        silentremove(self.filename)

class Test_disk_data(unittest.TestCase):
    """Write to disk, open, read, close; Write to disk, open, read, close; etc"""     
         
    filename = '.temp_update_h5_data.h5'
    
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
        silentremove(self.filename)               

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
    Read and write an x and y dataset representing a cantielver oscillation.
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

    def setUpClass(cls):
        """"
        Record the date and time for use by the functions below. 
        Delete the output file if it exists so we can make it anew.
        """

        try:
            silentremove(cls.filename)
        except:
            pass  
            
        # today = datetime.datetime.today()
        today = datetime.datetime(2014, 7, 31, 18, 29, 12, 137998)    
            
        cls.date = today.strftime("%Y-%m-%d")
        cls.time = today.strftime("%H:%M:%S")

    setUpClass = classmethod(setUpClass)    
            
    def test_01_write(self):
        """Write the representative dataset to a file."""
        
        f = h5py.File(self.filename, 'w')
        
        f.attrs['date'] = self.date
        f.attrs['time'] = self.time
        f.attrs['h5py_version'] = h5py.__version__
        f.attrs['source'] = 'test_hdf5.py'
        f.attrs['help'] = 'This is a test file created during unit testing'
               
        dt = 10.0E-6       
        t = dt*np.arange(32*1024)       
               
        # set the attributes by brute force       
        dset = f.create_dataset('x',data=t)
        dset.attrs['name'] = 't'
        dset.attrs['unit'] = 's'
        dset.attrs['label'] = 't [s]'
        dset.attrs['label_latex'] = '$t \: [\mathrm{s}]$'
        dset.attrs['help'] = 'time axis'
        dset.attrs['initial'] = t[0]
        dset.attrs['step'] = t[1] - t[0]
        
        f0 = 0.013/(2*dt)
        x = np.sin(2*np.pi*f0*t)
        
        # set the attributes more succinctly using an OrderedDict
        # we need an OrderedDict here so that the keys will add in the
        #  given order; neccessary so that the string comparison in 
        #  the assertEqual test of test_02_read () will succeed
        
        dset = f.create_dataset('y',data=x)        
        attrs = OrderedDict([ \
            ('name','x'),
            ('unit','nm'),
            ('label','x [nm]'),
            ('label_latex','$x \: [\mathrm{nm}]$'),
            ('help', 'cantilever amplitude'),
            ('n_avg', 1)
            ])
        update_attrs(dset.attrs,attrs)
             
        f.close()

    def test_02_read(self):
        """
        Read the representative dataset, print out the elements, and compare
        the printout with the expected string.
        """
        
        f = h5py.File(self.filename, 'r')
        
        report = []
        
        for key, val in f.attrs.items():
            report.append("{0}: {1}".format(key, val))
        
        for item in f:
            
            report.append("{}".format(f[item].name))
            for key, val in f[item].attrs.items():
                report.append("    {0}: {1}".format(key, val))
        
        report_string = "\n".join(report)

        f.close()        
                        
        print "\nObjects in file {0}".format(self.filename)
        print report_string               
        print ""                                                
        print "Try:"
        print "{0}".format("h5ls -rv {}".format(self.filename))                
                        
        self.assertEqual(report_string,Test_update_attrs_extended__contents)


Test_update_attrs_extended__contents = r"""date: 2014-07-31
time: 18:29:12
h5py_version: 2.2.1
source: test_hdf5.py
help: This is a test file created during unit testing
/x
    name: t
    unit: s
    label: t [s]
    label_latex: $t \: [\mathrm{s}]$
    help: time axis
    initial: 0.0
    step: 1e-05
/y
    name: x
    unit: nm
    label: x [nm]
    label_latex: $x \: [\mathrm{nm}]$
    help: cantilever amplitude
    n_avg: 1"""        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
if __name__ == '__main__':
    
    unittest.main(verbosity=2)
