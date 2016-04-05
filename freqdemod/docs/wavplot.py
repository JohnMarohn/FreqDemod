#! /usr/bin/env python
# http://people.csail.mit.edu/hubert/pyaudio/
#
# jam99
# 2014/07/23
# install pyaudio using the Canopy/Enthought package manager
# pyaudio 0.2.4
#
# Adapted from 
# http://stackoverflow.com/questions/18625085/how-to-plot-a-wav-file

import matplotlib.pyplot as plt
import numpy as np
import wave
import sys

if len(sys.argv) < 2:
    print("Plots a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)
    
spf = wave.open(sys.argv[1],'r')

#Extract Raw Audio from Wav File

signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

#If Stereo

if spf.getnchannels() == 2:
    print('Just mono files please')
    sys.exit(0)

t = np.linspace(0, len(signal)/fs, num=len(signal))

plt.figure(facecolor='w')
plt.title('Signal Wave...')
plt.plot(t,signal)
plt.ylabel('amplitude [a.u.]')
plt.xlabel('times [s]')
plt.show()