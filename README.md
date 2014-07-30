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

To create the html documentation, you will need the sphinx and fabric packages.  Then,

```bash
    cd docs
    fab html_full
    fab open
```
