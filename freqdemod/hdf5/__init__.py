"""
This module will collect tools for reading, writing and testing structured
HDF5_ files.

HDF5 Format Specification
-------------------------

Here is a sample of the HDF5 file format.

::

    /
    attributes: {'date': '2014-07-22',
                 'time': '13:00:00',
                 'hdf5_version': 'v0.1',
                 'source': 'PSB-B19-AFM',
                 'help': 'What is this data?'
                 'extra_dimensions': 'x2'}
        x
        attributes: {'name': 'Frequency',
                     'initial': 0.0,
                     'step': 0.5,
                     'unit': 'Hz',
                     'help': 'Frequency array for PSD.'}
            [0, 0.5, 1.0, 1.5]

        x2
        attributes: {'name': 'Laser Power'}
                     'unit': 'mW'
                     'help': 'Interferometer Output Laser Power'
                    }
            [2.0]

        y/
        attributes: {'name': 'PSD_{\delta x}'
                     'n_avg': 4,
                     'unit': 'nm^2/Hz',
                     'help': 'Power spectral density of position fluctuations.'}
            mean
                [1, 2.1, 2.9, 4]
            stdev
                [0.2, 0.3, 0.4, 0.5]


        workup/
            FFT
             [1, 2, 3]
            FTTunit
             'nm'



Note: If ``x`` is an empty array, we can determine the array from
the initial and step attributes.

Note: If ``y['n_avg'] == 1``, then ``y`` is a dataset rather than a group,
with ``y`` data stored directly, as shown below.

::

        y
        attributes: {'name': 'PSD_{\delta x}'
                     'n_avg': 1,
                     'unit': 'nm^2/Hz',
                     'help': 'Power spectral density of position fluctuations.'}
            [1, 2.1, 2.9, 4]

After the data has been processed, you can output any fitting or workup
parameters to a group called ``workup``.

.. _HDF5: http://www.hdfgroup.org/HDF5/
        
"""


def update_attrs(h5_attrs, attrs):
    """Update the attributes in ``h5_attrs``, an ``h5py`` group or dataset,
    by adding attributes in the dictionary attrs.

    This will overwrite existing attributes.
    """
    for key, val in attrs.viewitems():
        h5_attrs[key] = val
