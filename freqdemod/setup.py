#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# John A. Marohn (jam99@cornell.edu)
# 2014/06/28 -- untested

from setuptools import setup

# A custom plist for letting it associate with all files.

Plist = \
    dict(CFBundleDocumentTypes=\
        [dict(CFBundleTypeExtensions=["*"],
              CFBundleTypeRole="Editor"),
        ]
    )

APP = ['freqdemod.py']
DATA_FILES = []
OPTIONS = dict(
            argv_emulation = True,
            plist=Plist)
 
setup(
    app=APP,
    data_files=DATA_FILES,
        )
