#!/usr/bin/env python
# -*- coding: utf-8 -*-
# #
# freqdemod.py John A. Marohn 2014/06/28
# 
# For formatting fields, see 
# http://sphinx-doc.org/domains.html#info-field-lists

"""

We demodulate the signal in the following steps:

1. Apply a window to the signal :math:`S(t)` in order to make it
   smoothly ramp up from zero and ramp down to zero.

2. Fast Fourier Transform the windowed signal to obtain
   :math:`\\hat{S}(f)`.

3. Identify the primary oscillation frequency :math:`f_0`.  Apply a
   bandpass filter centered at :math:`f_0` to reject signals at other
   frequencies.

4. Apply a second filter which zeros out the negative-frequency
   components of :math:`\\hat{S}(f)`.

5. Apply an Inverse Fast Fourier Transform to the resulting data to
   obtain a complex signal :math:`z(t) = x(t) + i \: y(t)`.

6. Compute the instantaneous phase :math:`\\phi` and amplitude
   :math:`a(t)` using the following equations. Unwrap the phase.

.. math::
    :label: Eq;phi
    
    \\begin{equation}
    \\phi(t) = \\arctan{[\\frac{y(t)}{x(t)}]}
    \\end{equation}

.. math::
    :label: Eq:a
    
    \\begin{equation}
    a(t) = \\sqrt{x(t)^2 + y(t)^2}
    \\end{equation}

7. Calculate the "instantaneous" frequency :math:`f(t)` by dividing the
   instantaneous phase data into equal-time segments and fitting each
   segment to a line.  The average frequency :math:`f(t)` during each time
   segment is the slope of the respective line.

"""

import numpy as np 
import scipy as sp 
import math
import copy 
from util import eng

class Signal(object):

    def __init__(self, s, s_name, s_unit, dt):

        """ 
        Create a *Signal* object from the following inputs.
        
        :param s: the signal *vs* time 
        :type s: np.array  or list
        :param str s_name: the signal's name
        :param str s_name: the signal's units
        :param float dt: the time per point [s]
        
        Add the following objects to the *Signal* object
        
        :param np.array signal['s']: a copy of the signal
        :param str signal['s_name']: a copy of the signal's name
        :param str signal['s_unit']: a copy of the signal's unit
        :param float signal['dt']: a copy of the time per point [s]
        :param np.array signal['t']: an array of time data [s]
        
        """

        signal = {}

        signal['s'] = np.array(s)
        signal['s_name'] = s_name
        signal['s_unit'] = s_unit

        signal['dt'] = dt
        signal['t'] = dt*np.arange(0,len(np.array(s)))

        self.signal = signal

    def binarate(self,mode):

        """
        Truncate the signal **signal['s']**, if needed, so that it is a
        factor of two in length.
        
        :param str mode: "start", "middle", or "end" 
        
        With "start", the beginning of the signal array is left intact and the 
        end is truncated; with "middle", the signal array is shortened
        symmetically from both ends; and with "end" the end of the signal array
        is left intact while the beginning of the array is chopped away.  The
        time array is truncated analogously.
        
        Add or modify the following objects to the *Signal* object
        
        :param np.array signal['s']: shortened so it is a power of 2 in length
        :param np.array signal['t']: shortened so it is a power of 2 in length
        :param np.array signal['s_original']: a copy of the (unshortened) 
            original signal
        :param np.array signal['t_original']: a copy of the (unshortened) 
            original time array
        
        """

        self.signal['s_original'] = copy.deepcopy(self.signal['s'])
        self.signal['t_original'] = copy.deepcopy(self.signal['t'])

        n = len(self.signal['s']) 
        n2 = int(math.pow(2,int(math.floor(math.log(n, 2)))))

        if mode == "middle":

            n_start = int(math.floor((n - n2)/2))
            n_stop = int(n_start + n2)
            array_indices = list(np.arange(n_start,n_stop))

        elif mode == "start":

            array_indices = list(np.arange(0,n2))

        elif mode == "end":

            array_indices = list(np.arange(n-n2,n))

        self.signal['s'] = self.signal['s'][array_indices]
        self.signal['t'] = self.signal['t'][array_indices]

    def window(self,tw):

        """
        Create a windowing function and apply it to the signal array
        **signal['s']**.
        
        :param float tw: the window's rist/fall time [s] 
        
        The windowing function is a concatenation of
        
        1. the rising half of a Blackman filter;
        
        2. a constant 1.0; and
        
        3. the falling half of a Blackman filter.
        
        Add the following objects to the *Signal* object
        
        :param np.array signal['w']: the windowing function
        :param np.array signal['sw']: the signal multiplied by the 
            windowing function
        
        """

        ww = int(math.ceil((1.0*tw)/(1.0*self.signal['dt']))) 
        n = len(self.signal['s'])

        w = np.concatenate([sp.blackman(2*ww)[0:ww],
                            np.ones(n-2*ww),
                            sp.blackman(2*ww)[-ww:]])

        self.signal['w'] = w
        self.signal['sw'] = w*self.signal['s']

    def fft(self):

        """
        Take a Fast Fourier transform of the windowed signal **signal['sw']**.
        
        Add the following objects to the *Signal* object
        
        :param np.array signal['swFT']: FT of the windowed 
            signal **signal['sw']**
        :param np.array signal['f']: a frequency axis [Hz]
        :param float signal['df']: the spacing points along the 
            frequency axis [Hz]
        
        """

        # Fourier transform the data
         
        self.signal['swFT'] = \
            np.fft.fftshift(
                np.fft.fft(
                    self.signal['sw']))

        # make a frequency axis
         
        self.signal['f'] = \
            np.fft.fftshift(
                np.fft.fftfreq(
                    self.signal['swFT'].size,
                    d=self.signal['dt']))

        self.signal['df'] = self.signal['f'][1] - self.signal['f'][0]

    def filter(self,bw,order=50):

        """
        Apply two filters to the Fourier transformed data.
        
        :param float bw: filter bandwidth. :math:`\\Delta f` [Hz]
        :param int order: filter order, :math:`n` (defaults to 50)
        
        Add the following objects to the *Signal* object
        
        :param np.array signal['swFTfilt']: the filtered signal
        :param np.array signal['rh']: the right-handed filter
        :param np.array signal['bp']: the bandpass filter 
        :param float signal['td']: ripple caused by the filter [s]
        
        The first filter sets the negative-frequency components of the FT'ed
        data to zero, giving a "right handed" spectrum.  The associated
        filtering function is
        
        .. math::
            :label: Eq:rh
             
            \\begin{equation}
            \\mathrm{rh}(f) = 
            \\begin{cases}
            0 & \\text{if $f \\leq 0$} \\\\ 
            2 & \\text{if $f > 0$}
            \\end{cases}
            \\end{equation}
        
        The factor of 2 (instead of 1) results in two quadrature signals --
        obtained by an inverse Fourier transform below -- that are the same
        amplitude as the original signal.  The second filter is a bandpass
        filter centered at the oscillation frequency, :math:`f_0`.  The center
        frequency is automatically estimated as the largest peak in the right
        handed spectrum.  The associated filtering function is
        
        .. math::
            :label: Eq:bp
             
            \\begin{equation}
            \\mathrm{bp}(f) 
            = \\frac{1}{1 + (\\frac{|f - f_0|}{\\Delta f})^n}
            \\end{equation}
        
        The absolute value makes the filter symmetric, even for odd values of 
        :math:`n`.  When we inverse-FFT the filtered signal, the resulting
        time-domain signal will now have a leading- and trailing-edge ripple
        resulting from the filtering.  We therefore compute and save an 
        estimated delay time, **signal['td']** or :math:`t_d`, that it will take
        the new signal to settle.  We use :math:`t_d = 1.25/\\Delta f`.   For a
        high-order filter, :math:`n=50`, this :math:`t_d` value empirically 
        reduces the remaining ripple in the ampltude of a pure sine wave to less
        than approximately 2 percent of the full amplitude.
        
        """

        # save the filter parameters
        
        self.signal['bw'] = bw
        self.signal['order'] = order

        # the right-hand filter
        
        f_shifted = self.signal['f'] - self.signal['df']/2
        self.signal['rh'] = (abs(f_shifted) + f_shifted)/(abs(f_shifted))
        swFTrh = self.signal['rh']*self.signal['swFT']

        # the bandpass filter 
         
        self.signal['f0'] = self.signal['f'][np.argmax(abs(swFTrh))]
        f_scaled = (self.signal['f'] - self.signal['f0'])/bw
        self.signal['bp'] = 1.0/(1.0+np.power(abs(f_scaled),order))
        self.signal['swFTfilt'] = swFTrh*self.signal['bp']
        
        # the estimated delay time
        
        self.signal['td'] = 1.25/bw

    def ifft(self):

        """
        Apply an Inverse Fast Fourier Transform to the filtered FT'ed data
        **signal['swFTfilt']**.
        
        Add the following objects to the *Signal* object
        
        :param np.array signal['z']: complex-valued signal; 
            **z.real** is a filtered copy of the original signal, while
            **z.imag** is a phase-shifted (quadrature) copy of the original
            signal
        :param np.array signal['theta']: the signal phase [Hz, not radians]
        :param np.array signal['a']: the signal amplitude
        
        """

        self.signal['z'] = \
            np.fft.ifft(
                np.fft.fftshift(
                    self.signal['swFTfilt']))

        self.signal['theta'] = np.unwrap(np.angle(self.signal['z']))/(2*np.pi)
        self.signal['a'] = abs(self.signal['z'])
        
    def trim(self):
    
        """
        Remove the leading and trailing ripple from the complex signal, phase,
        and amplitude data.  The amount of leading and trailing data removed is 
        determined by the time delay, **signal['td']**, computed in the 
        *filter()* function.
        
        Modify the following objects in the *Signal* object
        
        :param np.array signal['z']: truncated complex signal
        :param np.array signal['theta']: truncated phase [Hz]
        :param np.array signal['a']: truncated amplitude
        :param np.array signal['t']: truncated time [s]
        
        """
        
        id = self.signal['td']/self.signal['dt']
        self.signal['z'] = self.signal['z'][id:-id]
        self.signal['theta'] = self.signal['theta'][id:-id]
        self.signal['a'] = self.signal['a'][id:-id]
        self.signal['t'] = self.signal['t'][id:-id]
        
    
    def __repr__(self):

        """
        Make a report of the (original) signal's properties including its name,
        unit, time step, rms, max, and min.
        
        """

        s_rms = np.sqrt(np.mean(self.signal['s']**2))
        s_min = np.min(self.signal['s'])
        s_max = np.max(self.signal['s'])

        temp = []
        
        temp.append("Signal")
        temp.append("======")
        temp.append("signal name: {0}".format(self.signal['s_name']))
        temp.append("signal unit: {0}".format(self.signal['s_unit']))
        temp.append("signal lenth = {}".format(len(self.signal['s'])))
        temp.append("time step = {0:.3f} us".format(self.signal['dt']*1E6))
        temp.append("rms = {}".format(eng(s_rms)))
        temp.append("max = {}".format(eng(s_max)))
        temp.append("min = {}".format(eng(s_min)))

        return '\n'.join(temp)

