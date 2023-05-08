To do
-----

* **PSD and fitting**: Define another object (``PSD`` perhaps) and make methods that computes a power spectrum, saves the power spectum as an hdf5 file, and fits the power spectrum to one of two models.  You should also just be able to read in power-spectrum data from an hdf5 files and fit it. 

* **Documentation**. (1) With the total review, the quickstart files are brokwn.  Rewrite them!  Split the files into a few true ``quickstart`` files and longer ``development`` files.  (2) The documentation for the new, HDF5-based code is pretty rough; update it.  (3) Update the ``report`` string in all the functions.  The report could be even more informative.  (4) Rewrite /docs/fabfile.py since the fabric package is totally different now.

Done
----

* Fitting a decay: Harrell 2014/07/30 suggets that it would be handy to have a method to extract oscillator Q from an object of type Signal that contained a trace from a ping experiment.  Idea: curve fit the decay to an exponential.

* Rename the internal variables in the **Signal** object so that the original data is stored in a dictionary called **signal** while the derived, worked-up data is stored in a separate dictionary called **workup**.  This arrangement will correspond more closely to how the data will be stored in the hdf5 file.  

* Store the worked-up data in an hdf5 data structure*!  With attributes, each signal can store its own plot labels and messages!  If you handle the worked-up arrays this way, then saving them to disk will be *very* easy I think. SUMMARY: Use the in-memory HDF5 "file" object as a generalized numpy array, carrying along its own units, axis labels, and messages. Some references:
 
 - h5py Quickstart Quide: http://docs.h5py.org/en/latest/quick.html

 - In-memory HDF5 files: http://pytables.github.io/cookbook/inmemory_hdf5_files.html; see also http://docs.h5py.org/en/latest/high/file.html and search for core.
 
 - HDF5 tutorial: http://blog.tremily.us/posts/HDF5/

* Write a function that saves the signal *and* worked-up data as an hdf5 file.  Could call the function, for example, ``.save_hd5(filename="my_worked_up_signal.h5")``.  Add an analogous function ``.load_hd5(filename="my_signal.h5")``, that populates the data structure from an hdf5 array.  This function should load not only any signal data, but also any worked-up data as well.

* Work in natural units: seconds for time (and ringdown) and kHz for frequency.  This way we won't have to convert Hz to kHz for plotting.  Using this units conventions and storing the worked-up data in hdf5 format, it should be possible to write a very general plotting function that uses ascii or LaTeX axis labels. 

* In ``.trim()`` we now overwrite the ``signal[‘z’]``, ``signal[‘theta’]``, ``signal[‘a’]``, and ``signal[‘t’]`` arrays.  Instead, define a *masking* array that is used by later functions to select a subsection of the data for analysis and plotting.  Think about modifying ``.binarate()`` to also simply generate a masking array.

* Added many more units tests. As of 2014/08/07, have 27 units tests.

* Rewrite ``__init__`` to be an empty constructor, e.g., taking zero arguments.  Replace it with ``.load_nparray(s,s_name,s_unit,dt)``.  Add units tests.

* Modify ``demodulate.py`` so that it takes command-line arguments allowing you to choose a test signal.

* Get the units right on the FT y axis (e.g., nm/Hz).

* Change all the ``yes`` or ``no`` inputs to ``True`` and ``False``.  

* Modify all the plotting functions so that using LaTeX to typeset the plot labels is optional.  This is because some people have trouble getting the LaTeX plot labels to work in matplotlib; for them, the plotting functions don't work presently.  This took quite a bit of work!

* Add command-line demodulate.py which takes options for LaTeX plotting.