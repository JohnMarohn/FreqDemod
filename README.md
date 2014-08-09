UPDATES
=======

2014/08/09 (jam99@cornell.edu): The demodulate.py file has undergone a major rewrite!

* The "quickstart" files are essentially all broken.  You may instead see how the new code works by running, at the command line, from the home directory of the package

```bash
    python freqdemod/demodulate.py --no-LaTeX --testsignal=sine
    python freqdemod/demodulate.py --no-LaTeX --testsignal=sinefm
    python freqdemod/demodulate.py --no-LaTeX --testsignal=sineexp
```    
    
  Running these commands will bring up a number of windows.  You will have to click each window closed before the program will proceed and show you the next window.  Each window should have a pretty self-explanatory title I hope.  You can try the ``--LaTeX`` option to see all the plots in fancy LaTeX typesetting.

* All the data is stored as an HDF5 file.  If you have the h5py package installed correctly, you should have available the ``h5ls`` command line program which is useful for inspecting the contents of HDF5 files.  Each of the above programs saves its data to a hidden HDF5 file.  You can see the files by running at the command line::

```bash
    ls -ha | grep h5
```
  or simply looking for the files that start with a dot, ``.``, and end with ``.h5``.  To examine the contents of the HDF5 files produced by running

```bash  
    h5ls -rv .temp_sine.h5
    h5ls -rv .temp_sine_fm.h5
    h5ls -rv .temp_sine_exp.h5
```
    
* The code is only lightly documented.  To get an idea of how things work, start by looking at the functions

```bash 
    testsignal_sine()
    testsignal_sine_fm()
    testsignal_sine_exp()
```

  in the ``demodulate.py`` program. 

Install the development version
===============================

For working with git, the program SourceTree is helpful.

To install the development version 

```bash
    git clone git@github.com:JohnMarohn/FreqDemod.git
    cd FreqDemod    
    git pull 
    find . -name "*.pyc" -delete
    nosetests
```

You will need a couple of packages:

* sphinx

* fabric

* nose

* numpy

* scipy

* matplotlib

* ipython.

If you have Canopy, you should have numpy, scipy, and matplotlib.  You can install nose and sphinx using the Canopy package manager.

To test whether the local installation worked, try

```bash
    python -c "from freqdemod.demodulate import Signal"
    python -m unittest discover
    python setup.py develop
```

To create a branch, play with it, and merge its code back into the master copy of the code:

```bash
    git checkout -b sandbox
    <do you coding>
    git add .
    git commit -m "This is what I did ..."
    <if you want to keep the changes>
    git checkout master
    git merge sandbox 
    git push
```

If you want to see the commit tree nicely in the terminal, type

```bash
    git config --global alias.tree "log --oneline --decorate --all --graph"
```

and from then on

```bash
    git tree
```

If you find yourself in trouble, want to trash the uncommitted changes in your sandbox, to make your working version the last version of the master copy:

```bash
    <frpm your messed-up sandbox>
    git checkout master
    git reset --hard HEAD
```

Documentation
=============

To create the html documentation, you will need the sphinx and fabric packages.  Then, from the FreqDemod directory

```bash
    cd docs
    fab html_full
    fab open
```
The documentation is created in FreqDemod/docs/_build/html.
