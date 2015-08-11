"""
A set of utility functions for HDF5 files
"""
import six
import h5py

def update_attrs(h5_attrs, attrs):
    """Update the attributes in ``h5_attrs``, an ``h5py`` group or dataset,
    by adding attributes in the dictionary ``attrs``.

    This will overwrite existing attributes; it is functionally equivalent to
    a python dictionary's update method.
    """

    for key, val in attrs.items():
        h5_attrs[key] = val


def _save_hdf5(f_src, f_dst, datasets, **kwargs):
    """"""
    for dset in datasets:
        f_src.copy(dset, f_dst, name=dset, **kwargs)


def save_hdf5(f_src, f_dst, datasets, overwrite=False, **kwargs):
    if isinstance(f_dst, six.string_types):
        mode = 'w' if overwrite else 'w-'
        with h5py.File(f_dst, mode=mode) as f:
            _save_hdf5(f_src, f, datasets, **kwargs)
    else:
        _save_hdf5(f_src, f_dst, datasets, **kwargs)
