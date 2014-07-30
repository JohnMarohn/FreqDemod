"""
Tests for the hdf5 module.
"""
import unittest

import h5py

from freqdemod.util import silentremove
from freqdemod.hdf5 import (update_attrs)


class Test_update_attrs(unittest.TestCase):
    filename = 'temp_update_h5_attrs.h5'

    def setUp(self):
        self.f = h5py.File(self.filename, 'w')
        self.f.attrs['to-be-overwritten'] = 'initial'

    def test_overwrite(self):
        """The function *should* overwrite existing attributes"""
        attrs = {'to-be-overwritten': 0}
        update_attrs(self.f.attrs, attrs)
        assert self.f.attrs['to-be-overwritten'] == 0

    def test_normal_write(self):
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
