"""
Summary
-------

Tests for the hdf5 module. In writing units tests, it is crucially important
too remember that the unittest object is recreated *every function call* 
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

Additional Resources
--------------------

* HDF5 Command-line Tools [`link <http://www.hdfgroup.org/products/hdf5_tools/>`__]

Unit Tests
----------

"""
import unittest
import h5py
import numpy as np

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
        silentremove(self.filename)
        
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
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
if __name__ == '__main__':
    
    unittest.main(verbosity=2)
