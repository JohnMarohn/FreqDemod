Introduction to the FreqDemod Package
=====================================

This package provides functions for analyzing and plotting the time-dependent frequency and amplitude of a sinusoidally oscillating signal.  Additional functions are provided for analyzing fluctuations in oscillator amplitude, phase, or frequency.  The provided functions should work equally well for any oscillating signal, although the included data-fitting and -plotting functions have been written with an oscillating atomic force microscope cantilever in mind.  The main frequency-demodulation algorithm's only assumption is that the oscillating signal contains a single frequency component (the carrier, in FM-radio terminology).

Resources
---------

* Download the package via the Python Package Index: https://pypi.python.org/pypi/FreqDemod

* Read the documentation at Read the Docs: http://FreqDemod.rtfd.org

* Obtain the source code at GitHub: https://github.com/JohnMarohn/FreqDemod

Install
-------

This package requires the following packages.  If you use the Enthought Canopy Distribution, then you should install these packages first using Enthought's package manager.  If you do not install them first, then ``pip`` will install them for you

* numpy 1.8.1

* scipy 0.14.1

* matplotlib 1.4.2

* h5py 2.4.0 

To install the package ::

    pip install FreqDemod

To test that the installation worked, run ::

    python -c "import freqdemod; freqdemod.test()"

Install the development version
-------------------------------

To edit the package and compile the documentation, you will need 

* fabric 1.10.1

* Sphinx 1.2.3

* ipython 2.3.1

To install the development version, first clone the package :: 

    git clone git@github.com:JohnMarohn/FreqDemod.git
    cd FreqDemod
    
To confirm that everything is working, in the FreqDemod directory run ::

    python -m unittest discover

or ::

    python -m unittest discover -v

or ::

    python setup.py test
    
If you make modifications to the code, and want to test drive your modifications, run ::

    python setup.py develop
    
Your modified code should now load when you ``import FreqDemod`` in your code.  To recreate the documentation, switch to the docs subdirectory, and run ::

    fab html
    fab open
    

If successful, you should see the documentation appear in your webbrowser.  The documentation is created in the directory ``FreqDemod/docs/_build/html``.

There is an example ipython notebook in the ``FreqDemod/freqdemod/docs`` directory.  Running the following command will convert the notebook to html and copy it to the documentation directory ::

    fab html_full
