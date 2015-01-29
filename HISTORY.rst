Development History
===================

2015/01/28
----------

* Typos fixed in documentation.

* Tests can now be easily run on packages installed via pip, using ``freqdemod.test()``.

2015/01/23
----------

* Release the package into the wild.

2014/08/09 
----------

The demodulate.py file has undergone a major rewrite!

* The "quickstart" files are essentially all broken.  You may instead see how the new code works by running, at the command line, from the home directory of the package ::

    python freqdemod/demodulate.py --no-LaTeX --testsignal=sine
    python freqdemod/demodulate.py --no-LaTeX --testsignal=sinefm
    python freqdemod/demodulate.py --no-LaTeX --testsignal=sineexp
    
  Running these commands will bring up a number of windows.  You will have to click each window closed before the program will proceed and show you the next window.  Each window should have a pretty self-explanatory title I hope.  You can try the ``--LaTeX`` option to see all the plots in fancy LaTeX typesetting.

* All the data is stored as an HDF5 file.  If you have the h5py package installed correctly, you should have available the ``h5ls`` command line program which is useful for inspecting the contents of HDF5 files.  Each of the above programs saves its data to a hidden HDF5 file.  You can see the files by running at the command line ::

    ls -ha | grep h5

  or simply looking for the files that start with a dot, ``.``, and end with ``.h5``.  To examine the contents of the HDF5 files produced by running ::

    h5ls -rv .temp_sine.h5
    h5ls -rv .temp_sine_fm.h5
    h5ls -rv .temp_sine_exp.h5
    
* The code is only lightly documented.  To get an idea of how things work, start by looking at the functions ::

    testsignal_sine()
    testsignal_sine_fm()
    testsignal_sine_exp()

  in the ``demodulate.py`` program. 
