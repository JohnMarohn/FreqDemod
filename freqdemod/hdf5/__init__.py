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
                 'hdf5_version': 'v0.1',  # Version of the format specification
                 'source': 'PSB-B19-AFM',
                 'help': 'What is this data?'
                 'extra_dimensions': 'x2'
                 'comment': 'This is an example HDF5 file with multiple dimensions, and several averages for each data point.'}
        x
        attributes: {'name': 'Frequency',
                     'unit': 'Hz',
                     'label': 'f [Hz]'
                     'label_latex': r'$f \\: [\\mathrm{Hz}]$',
                     'initial': 0.0,
                     'step': 0.5,
                     'help': 'Frequency array for PSD.'}
            [0, 0.5, 1.0, 1.5]

        x2
        attributes: {'name': 'Laser Power',
                     'unit': 'mW',
                     'label': 'P [mW]',
                     'label_latex': r'$P \\: [\\mathrm{mW}]$',
                     'help': 'Interferometer Output Laser Power'
                    }
            [2.0]

        y/
        attributes: {'name': 'Power Spectral Density of position fluctuations',
                     'unit': 'nm^2/Hz',
                     'label': 'PSD [nm^2 / Hz]',
                     'label_latex': r'$P_{\\delta x} \: [\\mathrm{nm}^2 / \\mathrm{Hz}]',
                     'n_avg': 4,  # If n_avg is not equal to one, there should be a dataset y_std containing standard deviations
                     'help': 'Power spectral density of position fluctuations.'}
            [1, 2.1, 2.9, 4]

        y_std/
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
    
    for key, val in attrs.items():
        h5_attrs[key] = val
