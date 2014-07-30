To do
-----

Creation, reading, and writing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Rename the internal variables in the **Signal** object so that the original data is stored in a dictionary called **signal** while the derived, worked-up data is stored in a separate dictionary called **workup**.  This arrangement will correspond more closely to how the data will be stored in the hdf5 file.

* Add a function ``.load_hd5(filename="my_signal.h5")``, that populates the data structure from an hdf5 array.  This function should load not only any signal data, but also any worked-up data as well.

* Write a function that saves the signal *and* worked-up data as an hdf5 file.  Could call the function, for example, ``.save_hd5(filename="my_worked_up_signal.h5")``.  

Workup
^^^^^^

* In ``.trim()`` we now overwrite the ``signal[‘z’]``, ``signal[‘theta’]``, ``signal[‘a’]``, and ``signal[‘t’]`` arrays.  Instead, define a *masking* array that is used by later functions to select a subsection of the data for analysis and plotting.

* Think about modifying ``.binarate()`` to also simply generate a masking array.

* Harrell 2014/07/30: Would be handy to have a method to extract oscillator Q from an object of type Signal that contained a trace from a ping experiment.  Idea: curve fit the decay to an exponential.

* Define another object (``PSD`` perhaps) and make methods that computes a power spectrum, saves the power spectum as an hdf5 file, and fits the power spectrum to one of two models.  You should also just be able to read in power-spectrum data from an hdf5 files and fit it. 

Plotting
^^^^^^^^

* Modify all the plotting functions so that using LaTeX to typeset the plot labels is optional.  This is because some people have trouble getting the LaTeX plot labels to work in matplotlib; for them, the plotting functions don't work presently.

Documentation and Testing
^^^^^^^^^^^^^^^^^^^^^^^^^

* Review the ``quickstart`` files -- split into true ``quickstart`` files and ``development`` files.  

* We need some units tests!


Done
----

* Rewrite ``__init__`` to be an empty constructor, e.g., taking zero arguments.  Replace it with ``.load_nparray(s,s_name,s_unit,dt)``.  Add units tests.

* Modify ``demodulate.py`` so that it takes command-line arguments allowing you to choose a test signal.

* Get the units right on the FT y axis (e.g., nm/Hz).

* Change all the ``yes`` or ``no`` inputs to ``True`` and ``False``.  