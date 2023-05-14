#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# util.py
# John A. Marohn
# 2014/06/28, 2023/05/11

import math
import datetime
import uuid
import numpy as np
import errno
import os

# Modified from http://code.activestate.com/recipes/578238-engineering-notation/

def powerise10(x):
    """ Return x as a * 10 ^ b with 1 <= a <10"""
    if x == 0: return 0 , 0
    Neg = x <0
    if Neg : x = -x
    a = 1.0 * x / 10**(math.floor(math.log10(x)))
    b = int(math.floor(math.log10(x)))
    if Neg : a = -a
    return a ,b

def eng(x):
    """Return a string representing x in an engineer-friendly notation"""
    a , b = powerise10(x)
    if -3<b<3: return "%.4g" % x
    a = a * 10**(b%3)
    b = b - b%3
    return "%.4gE%s" %(a,b)

def silent_remove(filename):
    """If ``filename`` exists, delete it. Otherwise, return nothing.
       See http://stackoverflow.com/q/10840533/2823213."""
    try:
        os.remove(filename)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occured


def timestamp_temp_filename(suffix, random_length=6):
    """Intented as a random, temporary filename"""
    time_prefix = datetime.datetime.now().strftime("%H%M%S")
    random_sequence = str(uuid.uuid4())[:random_length]
    return time_prefix + '-' +  random_sequence + suffix


def infer_timestep(x):
    dt_array = np.diff(x)
    dt_range = dt_array.max() / dt_array.min()
    if dt_range > 1.01 or dt_range < 0:
        raise ValueError("Time data points must be evenly spaced.")
    else:
        return dt_array.mean()

def nearest2power(x):
    """Nearest power of 2 to x, rounded down."""
    return int(math.pow(2,int(math.floor(math.log(x, 2)))))
