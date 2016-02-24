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

def h5ls_str(g, offset='', print_types=True):
    """Prints the input file/group/dataset (g) name and begin iterations on its
    content.
    
    See goo.gl/2JiUQK."""
    string = []
    if isinstance(g, h5py.File):
        string.append(offset+repr(g.file))
    elif isinstance(g, h5py.Dataset):
        if print_types:
            string.append(offset+g.name+'  '+repr(g.shape)+'  '+(g.dtype.str))
        else:
            string.append(offset+g.name+'  '+repr(g.shape))
    elif isinstance(g, h5py.Group):
        string.append(offset+g.name)
    else:
        raise ValueError('WARNING: UNKNOWN ITEM IN HDF5 FILE'+g.name)
    if isinstance(g, h5py.File) or isinstance(g, h5py.Group):
        for key, subg in dict(g).iteritems():
            string.append(h5ls_str(subg, offset + '    ',
                                   print_types=print_types))
    return "\n".join(string)


def h5ls(*args):
    """List the contents of an HDF5 file object or group.
    Accepts a file / group handle, or a string interpreted as the hdf5
    file path."""
    for arg in args:
        if isinstance(arg, six.string_types):
            fh = h5py.File(arg, mode='r')
            print(h5ls_str(fh))
            fh.close()
        else:
            print(h5ls_str(arg))
