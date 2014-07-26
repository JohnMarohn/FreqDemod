# :title: fabfile.py 
# :author: John A. Marohn (jam99@cornell.edu)
# :date: 2014-07-26 
# :subject: substitute/extend "make html" and "make open"
# :ref: http://docs.fabfile.org/en/1.4.1/tutorial.html
# :ref: http://ipython.org/ipython-doc/1/interactive/nbconvert.html

from fabric.api import *
from fabric.context_managers import lcd
import os
import glob

env.ipython_dir = os.path.join(os.path.join('..','freqdemod'),'docs')
home = os.getcwd()

def clean():

    local('rm -rf _build/*')

def html_full():

    os.chdir(os.path.join('{ipython_dir}'.format(**env)))
    ipynb_files = glob.glob('*.ipynb')
    os.chdir(home)

    with lcd('{ipython_dir}'.format(**env)):
        local('ls -la')
        for file in ipynb_files:
            print '{}'.format(file)
            local('ipython nbconvert --to html --template full {}'.format(file))
        
    with lcd(''):
        local('ls -la')
        local('sphinx-build -b html . _build/html')
    
def html():

    local('ls -la')
    local('sphinx-build -b html . _build/html')
    
def show():

    local('open _build/html/index.html')