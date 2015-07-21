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
from freqdemod.hdf5 import update_attrs
from freqdemod.util import silent_remove
import unittest
import numpy as np
from numpy.testing import assert_allclose, assert_array_equal
import h5py

class InitLoadSaveTests(unittest.TestCase):
    """
    Make sure the *Signal* object is set up correctly.
    """
    filename = '.InitLoadSaveTests_1.h5'
    def setUp(self):
        """
        Create an trial *Signal* object
        """
        
        self.s = Signal(self.filename)
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

    def tearDown(self):
        """Close the h5 files before the next iteration."""
        self.s.f.close()


class TestClose(unittest.TestCase):
    filename = '.TestClose.h5'
    def setUp(self):
        self.s = Signal(self.filename, backing_store=True)
        self.s.load_nparray(np.arange(3),"x","nm",10E-6)
        self.s.close()

    def tearDown(self):
        silent_remove(self.filename)

    def test_close(self):
        """Verify closed object by testing one of the attributes"""
        
        self.snew = Signal()
        self.snew.open(self.filename)
        
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

        
class MaskTests(unittest.TestCase):
    
    def setUp(self):
        """
        Create a trial *Signal* object
        """
        
        self.s = Signal('.InitLoadSaveTests_1.h5')
        self.s.load_nparray(np.arange(60000),"x","nm",10E-6)    
        
    def test_binarate_1(self):
        """Binarate mask middle; test length is 2^n"""
        
        self.s.time_mask_binarate("middle")
        m = self.s.f['workup/time/mask/binarate']

        self.assertEqual(np.count_nonzero(m),32*1024)    
        
    def test_binarate_2(self):
        """Binarate mask start; test length is 2^n"""
        
        self.s.time_mask_binarate("start")
        m = self.s.f['workup/time/mask/binarate']

        self.assertEqual(np.count_nonzero(m),32*1024)   
        
    def test_binarate_3(self):
        """Binarate mask end test length is 2^n"""
        
        self.s.time_mask_binarate("end")
        m = self.s.f['workup/time/mask/binarate']

        self.assertEqual(np.count_nonzero(m),32*1024)   
 
    def test_binarate_4(self):
        """If we have not called binarate, then workup/time/mask/binarate does not exist"""
        
        self.assertEqual(self.s.f.__contains__('workup/time/mask/binarate'),False)

    def test_binarate_5(self):
        """If we have called binarate, then workup/time/mask/binarate does exist"""
        
        self.s.time_mask_binarate("middle")
        self.assertEqual(self.s.f.__contains__('workup/time/mask/binarate'),True)  
   
    def tearDown(self):
        """Close the h5 files before the next iteration."""
        try:
            self.s.f.close()
        except:
            pass       
            
class FFTTests(unittest.TestCase):
    
    def setUp(self):
        """
        Create an trial *Signal* object
        """
        
        fd = 50.0E3    # digitization frequency
        f0 = 5.00E3    # signal frequency
        nt = 512     # number of signal points    

        dt = 1/fd
        t = dt*np.arange(nt)
        s = 1.0*np.sin(2*np.pi*f0*t) 

        self.s = Signal('.FFTTests_1.h5')
        self.s.load_nparray(s,"x","nm",dt)
        self.s.time_mask_binarate("middle")
        self.s.time_window_cyclicize(10*dt)
        self.s.fft()
        self.s.freq_filter_Hilbert_complex()
        
    def testfft_1(self):
        """FFT: test that the resulting data is complex"""
        
        first_point = self.s.f['workup/freq/FT'][0]
        self.assertEqual(isinstance(first_point, complex),True)
        
    def testfft_2(self):
        """FFT: test that the complex Hilbert transform filter is real"""
        
        first_point = self.s.f['workup/freq/filter/Hc'][0]
        self.assertEqual(isinstance(first_point, complex),False)
        
    def testfft_3(self):
        """FFT: test the complex Hilbert transform filter near freq = 0"""
        
        freq = self.s.f['workup/freq/freq'][:]
        index = np.roll(freq == 0,-1) + np.roll(freq == 0,0) + np.roll(freq == 0,1)
        filt = self.s.f['workup/freq/filter/Hc'][index]
        
        self.assertTrue(np.allclose(filt,np.array([0, 1, 2])))
                           
    def tearDown(self):
        """Close the h5 files before the next iteration."""
        try:
            self.s.f.close()
        except:
            pass                


class FFTOddPoints(unittest.TestCase):
    def setUp(self):
        self.x = np.array([0, 1, 0, -1, 0, 1, 0, -1, 0])
        self.s = Signal()
        self.s.load_nparray(self.x, 'x', 'nm', 1)

    def test_ifft_odd_pts(self):
        self.s.fft()
        self.s.ifft()
        x_ifft_fft = self.s.f['workup/time/z'][:]
        x = self.x
        # Should give x back to within numerical rounding errors
        assert_allclose(x.real, x_ifft_fft.real, atol=1e-15)
        assert_allclose(x.imag, x_ifft_fft.imag, atol=1e-15)

    def tearDown(self):
        self.s.close()


class HDF5LoadGeneral(unittest.TestCase):
    filename = '.general_format_h5_file.h5'

    def setUp(self):
        self.x = np.array([0, 1, 2])
        self.y = np.array([0, 2, 4])
        self.s = Signal()
        self.f = h5py.File(self.filename, driver='core',
                           backing_store=False)
        self.f['time'] = self.x
        self.f['position'] = self.y

    def test_load_general_format_h5_x_y(self):
        self.s._load_hdf5_general(self.f, s_dataset='position',
                                  t_dataset='time', s_name='x', s_unit='nm')

        assert_allclose(self.s.f['x'][:], self.x)
        assert_allclose(self.s.f['y'][:], self.y)

        self.assertEqual(self.s.f['x'].attrs['step'], 1)
        self.assertEqual(self.s.f['y'].attrs['name'], 'x')
        self.assertEqual(self.s.f['y'].attrs['label'], 'x [nm]')

    def test_load_general_format_h5_y_dt(self):
        self.s._load_hdf5_general(self.f, s_dataset='position',
                                  dt=1, s_name='x', s_unit='nm')

        assert_array_equal(self.s.f['x'][:], self.x)
        assert_array_equal(self.s.f['y'][:], self.y)

        self.assertEqual(self.s.f['x'].attrs['step'], 1)
        self.assertEqual(self.s.f['y'].attrs['name'], 'x')
        self.assertEqual(self.s.f['y'].attrs['label'], 'x [nm]')

    def test_load_general_no_x_or_dt_specified(self):
        with self.assertRaises(ValueError):
            self.s._load_hdf5_general(self.f, s_dataset='position', s_name='x',
                                      s_unit='nm')

    def tearDown(self):
        self.f.close()
        self.s.close()


class HDF5LoadDefault(unittest.TestCase):
    filename = '.default_format_h5_file.h5'

    def setUp(self):
        self.f = h5py.File(self.filename, driver='core',
                           backing_store=False)
        self.x = np.array([0, 1, 2])
        self.y = np.array([0, 2, 4])

        self.x_attrs = {'name': 't',
                        'unit': 's',
                        'label': 't [s]',
                        'label_latex': '$t \\: [\\mathrm{s}]$',
                        'help': 'time axis',
                        'initial': 0,
                        'step': 1}

        self.y_attrs = {'name': 'x',
                        'unit': 'nm',
                        'label': 'x [nm]',
                        'label_latex': '$x \: [\mathrm{nm}]$',
                        'help': 'cantilever amplitude',
                        'abscissa': 'x',
                        'n_avg': 1}

        self.f['x'] = self.x
        self.f['y'] = self.y

        update_attrs(self.f['x'].attrs, self.x_attrs)
        update_attrs(self.f['y'].attrs, self.y_attrs)

        self.s = Signal()

    def test_hdf5_general_all_attrs_specified(self):
        self.s._load_hdf5_default(self.f, infer_dt=False,
                                  infer_attrs=False)

        assert_array_equal(self.s.f['x'][:], self.x)
        assert_array_equal(self.f['y'][:], self.y)
        self.assertEqual(dict(self.s.f['x'].attrs), self.x_attrs)
        self.assertEqual(dict(self.s.f['y'].attrs), self.y_attrs)

    def test_hdf5_general_infer_dt(self):
        del self.f['x'].attrs['step']

        self.s._load_hdf5_default(self.f, infer_dt=True,
                                  infer_attrs=False)

        assert_array_equal(self.s.f['x'][:], self.x)
        assert_array_equal(self.f['y'][:], self.y)
        self.assertEqual(dict(self.s.f['x'].attrs), self.x_attrs)
        self.assertEqual(dict(self.s.f['y'].attrs), self.y_attrs)

    def test_hdf5_general_infer_missing_label(self):
        del self.f['x'].attrs['label']

        self.s._load_hdf5_default(self.f, infer_dt=False,
                                  infer_attrs=True)

        assert_array_equal(self.s.f['x'][:], self.x)
        assert_array_equal(self.f['y'][:], self.y)
        self.assertEqual(dict(self.s.f['x'].attrs), self.x_attrs)
        self.assertEqual(dict(self.s.f['y'].attrs), self.y_attrs)

    def test_hdf5_general_infer_missing_abscissa(self):
        del self.f['y'].attrs['abscissa']

        self.s._load_hdf5_default(self.f, infer_dt=False,
                                  infer_attrs=True)

        assert_array_equal(self.s.f['x'][:], self.x)
        assert_array_equal(self.f['y'][:], self.y)
        self.assertEqual(dict(self.s.f['x'].attrs), self.x_attrs)
        self.assertEqual(dict(self.s.f['y'].attrs), self.y_attrs)


    def test_hdf5_general_infer_missing_y_labels(self):
        del self.f['y'].attrs['label']
        del self.f['y'].attrs['label_latex']

        self.s._load_hdf5_default(self.f, infer_dt=False,
                                 infer_attrs=True)

        assert_array_equal(self.s.f['x'][:], self.x)
        assert_array_equal(self.f['y'][:], self.y)
        self.assertEqual(dict(self.s.f['x'].attrs), self.x_attrs)
        self.assertEqual(dict(self.s.f['y'].attrs), self.y_attrs)

    def tearDown(self):
        self.f.close()
        self.s.close()





class MiscTests(unittest.TestCase):
    
    def test_array_middle_1(self):
        """Misc: mean time (n odd)"""
        
        n = 5
        t = np.arange(n) # [0,1,2,3,4] => mean 2 -> t[2]
        self.assertEqual(np.mean(t,axis=0),2.0)
        
                
    def test_array_middle_2(self):
        """Misc: mean time (n even)"""
        
        n = 6
        t = np.arange(n) # [0,1,2,3,4,5] => mean 2.5 => (t[2]+t[3])/2.0
        self.assertEqual(np.mean(t,axis=0),2.5)
