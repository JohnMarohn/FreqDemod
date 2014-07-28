* Rewrite `__init__` to be an empty constructor, e.g., taking zero arguments

* Write a function, `.load()`, which populates the data structure, e.g., plays the role of `__init__` now.  Write an associated function `.save()`, which saves the signal, and any worked-up data, as an `hdf5` file.  The save function should save whatever data is in the Signal object.  

* Write another function, `.load_hd5(filename="my_signal.h5",dataset="x")`, that populates the data structure from an hdf5 array.  

* Mask