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
    """Copy all the elements of datasets from f_src to f_dst. For information
    on kwargs, see the documentation for the h5py copy method."""
    for dset in datasets:
        f_src.copy(dset, f_dst, name=dset, **kwargs)


def save_hdf5(f_src, f_dst, datasets, overwrite=False, **kwargs):
    """Copy all the elements of datasets from f_src to f_dst. For information
    on kwargs, see the documentation for the h5py copy method.

    :param f_src: source h5py file or group object
    :param f_dst: destination filename or h5py file or group object
    :param datasets: list of datasets / groups to copy
    :param overwrite: If True, overwrite an existing file with the filename
        f_dst.
    """
    if isinstance(f_dst, six.string_types):
        mode = 'w' if overwrite else 'w-'
        with h5py.File(f_dst, mode=mode) as f:
            _save_hdf5(f_src, f, datasets, **kwargs)
    else:
        _save_hdf5(f_src, f_dst, datasets, **kwargs)
