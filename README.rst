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

This package requires the following packages.  See the ``requirements.txt`` file.  If you do not install these packages first, then ``pip`` will install them for you.

* numpy 1.19.2

* scipy 1.5.2

* matplotlib 3.3.4

* h5py 3.8

* six 1.16

* lmfit 1.0.3

It is recommended that you create a virtual enviroment to run the package in.  Using the conda package manager to create a new virtual environment called "freqdemod" running python version 3.10 ::

    conda create -n freqdemod python=3.10
    conda activate freqdemod

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
    
If you are working on an update to freqdemod, and want to install it, run ::

    pip install -e .
    
The `-e` is short for `--editable`.  Passing the `-e` flag to pip will force pip to reinstall the package every time the package contents are updated.  This way, the installation will remain current as you continue to modify freqdemod.  Then you are done with modifications and want to install the package " for good", you can instead run ::

    pip install .

If you plan on running the example jupyter notebooks locally, you will need to install jupyter and a matching ipython kernel in the freqdemod virtual enviroment ::
 
    conda activate freqdemod 
    conda install notebook
    conda install ipykernel
    python -m ipykernel install --user --name=freqdemod

Verify the kernel using ::

    jupyter kernelspec list

Your modified code should now load when you ``import freqdemod`` in your code.  To recreate the documentation, switch to the docs subdirectory, and run ::

    fab html
    fab open
    

If successful, you should see the documentation appear in your webbrowser.  The documentation is created in the directory ``FreqDemod/docs/_build/html``.

There is an example ipython notebook in the ``FreqDemod/freqdemod/docs`` directory.  Running the following command will convert the notebook to html and copy it to the documentation directory ::

    fab html_full
