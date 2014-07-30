"""
A set of utility functions for HDF5 files
"""


def update_attrs(h5_attrs, attrs):
    """Update the attributes in ``h5_attrs``, an ``h5py`` group or dataset,
    by adding attributes in the dictionary ``attrs``.

    This will overwrite existing attributes; it is functionally equivalent to
    a python dictionary's update method.
    """
    for key, val in attrs.viewitems():
        h5_attrs[key] = val
