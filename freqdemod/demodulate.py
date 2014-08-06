#!/usr/bin/env python
# -*- coding: utf-8 -*-
# #
# demodulate.py John A. Marohn 2014/06/28
# 
# For formatting fields, see 
# http://sphinx-doc.org/domains.html#info-field-lists
#
# From http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb
# import matplotlib
# matplotlib.rcParams.update({'font.size': 18, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})


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
   obtain a complex signal :math:`z(t) = x(t) + \imath \: y(t)`.

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

import h5py
import numpy as np 
import scipy as sp 
import math
import copy
import time
import datetime
from freqdemod.hdf5 import (update_attrs)
from collections import OrderedDict

import matplotlib.pyplot as plt 

class Signal(object):

    # =======================================================================

    def __init__(self, filename=None):
        
        """
        Initialize the *Signal* object. Inputs:
        
        :param str filename: the signal's (future) filename 
        
        Add the following objects to the *Signal* object
        
        :param h5py.File f: an h5py object stored in core memory 
        :param str report: a string summarizing in words what has
            been done to the signal (e.g., "Empty signal object created")
            
        """
        
        if filename != None:
        
            self.f = h5py.File(filename, 'w', driver = 'core')
            
            today = datetime.datetime.today()
            
            attrs = OrderedDict([ \
                ('date',today.strftime("%Y-%m-%d")),
                ('time',today.strftime("%H:%M:%S")),
                ('h5py_version',h5py.__version__),
                ('source','demodulate.py'),
                ('help','Sinusoidally oscillating signal and workkup')
                ])
            
            update_attrs(self.f.attrs,attrs)
            
            self.report = []
            new_report = []
            new_report.append("HDF5 file {0} created in core memory".format(filename))
            self.report.append(" ".join(new_report))

    def load_nparray(self, s, s_name, s_unit, dt):

        """ 
        Create a *Signal* object from the following inputs.
        
        :param s: the signal *vs* time 
        :type s: np.array  or list
        :param str s_name: the signal's name
        :param str s_name: the signal's units
        :param float dt: the time per point [s]
        
        Add the following objects to the *Signal* object
        
        :param h5py.File f: an h5py object stored in core memory 
        :param str report: a string summarizing in words what has
            been done to the signal 
        
        """

        dset = self.f.create_dataset('x',data=dt*np.arange(0,len(np.array(s))))
        attrs = OrderedDict([
            ('name','t'),
            ('unit','s'),
            ('label','t [s]'),
            ('label_latex','$t \: [\mathrm{s}]$'),
            ('help','time'),
            ('initial',0.0),
            ('step',dt)
            ])          
        update_attrs(dset.attrs,attrs)        

        dset = self.f.create_dataset('y',data=s)
        attrs = OrderedDict([
            ('name',s_name),
            ('unit',s_unit),
            ('label','{0} [{1}]'.format(s_name,s_unit)),
            ('label_latex','${0} \: [\mathrm{{{1}}}]$'.format(s_name,s_unit)),
            ('help','cantilever displacement'),
            ('abscissa','x'),
            ('n_avg',1)
            ])
        update_attrs(dset.attrs,attrs)    
        
        new_report = []
        new_report.append("Add a signal {0}[{1}]".format(s_name,s_unit))
        new_report.append("of length {0},".format(np.array(s).size))
        new_report.append("time step {0:.3f} us,".format(1E6*dt))
        new_report.append("and duration {0:.3f} s".format(np.array(s).size*dt))
        
        self.report.append(" ".join(new_report))

    def close(self):
        
        self.f.close()
        
    def open(self, filename):
        
        self.f = h5py.File(filename, 'r')

    # =======================================================================

    def plot(self, ordinate, LaTeX=False):
        
        """ 
        Plot a component of the *Signal* object.  
        
            :param str ordinate: the name the y-axis data key 
            :param boolean LaTeX: use LaTeX axis labels; ``True`` or ``False``
            (default)
            
        Plot ``self.f[ordinate]`` versus self.f[y.attrs['abscissa']].
        
        """
        
        y = self.f[ordinate]
        x = self.f[y.attrs['abscissa']]
        
        # posslby use tex-formatted axes labels temporarily for this plot
        # compute plot labels
        
        old_param = plt.rcParams['text.usetex']        
                        
        if LaTeX == True:
        
            plt.rcParams['text.usetex'] = True
            x_label_string = x.attrs['label_latex']
            y_label_string = y.attrs['label_latex']
            
        elif LaTeX == False:
            
            plt.rcParams['text.usetex'] = False
            x_label_string = x.attrs['label']
            y_label_string = y.attrs['label']

        title_string = "{0} vs. {1}".format(y.attrs['help'],x.attrs['help'])

        # create the plot
        
        fig=plt.figure(facecolor='w')
        plt.plot(x,y)
                        
        # axes limits and labels
        
        plt.xlabel(x_label_string)
        plt.ylabel(y_label_string)
        plt.title(title_string)
                
        # set text spacing so that the plot is pleasing to the eye

        plt.locator_params(axis = 'x', nbins = 4)
        plt.locator_params(axis = 'y', nbins = 4)
        fig.subplots_adjust(bottom=0.15,left=0.12)  

        # clean up label spacings, show the plot, and reset the tex option
          
        fig.subplots_adjust(bottom=0.15,left=0.12)   
        plt.show()
        plt.rcParams['text.usetex'] = old_param  
        
    # =======================================================================


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

        n = self.signal['s'].size 
        n2 = int(math.pow(2,int(math.floor(math.log(n, 2)))))

        n_start = 0
        n_stop = n
        n_msg = "N/A"

        if mode == "middle":

            n_start = int(math.floor((n - n2)/2))
            n_stop = int(n_start + n2)
            n_msg = "beginning and end"

        elif mode == "start":
            
            n_start = 0
            n_stop = n2
            n_msg = "end"           

        elif mode == "end":

            n_start = n-n2
            n_stop = n
            n_msg = "beginning"

        array_indices = list(np.arange(n_start,n_stop))

        self.signal['s'] = self.signal['s'][array_indices]
        self.signal['t'] = self.signal['t'][array_indices]

        new_report = []
        new_report.append("Truncate the signal to be {0}".format(n2))
        new_report.append("points long, a power of two.")
        new_report.append("This was done by chopping points off the")
        new_report.append("{0} of the signal array,".format(n_msg))
        new_report.append("that is, by using points")
        new_report.append("{0} up to {1}.".format(n_start,n_stop))
        
        self.report.append(" ".join(new_report))

    def window(self,tw):

        """
        Create a windowing function and apply it to the signal array
        **signal['s']**.
        
        :param float tw: the window's target rise/fall time [s] 
        
        The windowing function is a concatenation of
        
        1. the rising half of a Blackman filter;
        
        2. a constant 1.0; and
        
        3. the falling half of a Blackman filter.
        
        Add the following objects to the *Signal* object
        
        :param np.array signal['w']: the windowing function
        :param np.array signal['sw']: the signal multiplied by the 
            windowing function
        :param np.array signal[tw_actual]: the actual rise/fall file [s]

        The actual rise/fall time may not exactly equal the target rise/fall
        time if the requested time is not an integer multiple of the signal's
        time per point.
                
        """

        ww = int(math.ceil((1.0*tw)/(1.0*self.signal['dt']))) 
        n = len(self.signal['s'])
        tw_actual = ww*self.signal['dt'] 

        w = np.concatenate([sp.blackman(2*ww)[0:ww],
                            np.ones(n-2*ww),
                            sp.blackman(2*ww)[-ww:]])

        self.signal['w'] = w
        self.signal['sw'] = w*self.signal['s']
        self.signal['tw_actual'] = tw_actual
        
        
        new_report = []
        new_report.append("Window the signal with a rising/falling")
        new_report.append("blackman filter having a rise/fall time of")
        new_report.append("{0:.3f} us".format(1E6*tw_actual))
        new_report.append("({0} points).".format(ww))
        
        self.report.append(" ".join(new_report))

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
         
        start = time.time() 
         
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

        stop = time.time()
        t_calc = stop - start

        new_report = []
        new_report.append("Fourier transform the windowed signal.")
        new_report.append("It took {0:.1f} ms".format(1E3*t_calc))
        new_report.append("to compute the FFT.")
        
        self.report.append(" ".join(new_report))

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
        
        # an improved estimate of the center frequency
        #  using the method of moments -- this only gives the right answer
        #  because we have applied the nice bandpass filter first
        
        a = self.signal['f']
        b = abs(self.signal['swFTfilt'])
        
        self.signal['f00'] = (a*b).sum()/b.sum()
    
        # the estimated delay time
        
        self.signal['td'] = 1.25/bw
        
        # report
        
        new_report = []
        new_report.append("Reject negative frequencies;")
        new_report.append("apply a bandpass filter (center frequency")
        new_report.append("{0:.3f} Hz,".format(self.signal['f0']))
        new_report.append("bandwidth {0:.1f} Hz, ".format(bw))
        new_report.append("& order {0});".format(order))
        new_report.append("and set the delay time to")
        new_report.append("{0} us.".format(1E6*self.signal['td']))
        new_report.append("Make an improved estimate of the center")
        new_report.append("frequency: {0:.3f} Hz.".format(self.signal['f00']))
        
        self.report.append(" ".join(new_report))

    def ifft(self):

        """
        Apply an Inverse Fast Fourier Transform to the filtered FT'ed data
        **signal['swFTfilt']**.
        
        Add the following objects to the *Signal* object
        
        :param np.array signal['z']: complex-valued signal; 
            **z.real** is a filtered copy of the original signal, while
            **z.imag** is a phase-shifted (quadrature) copy of the original
            signal
        :param np.array signal['theta']: the signal phase [cycles, not radians]
        :param np.array signal['a']: the signal amplitude
        
        """

        self.signal['z'] = \
            np.fft.ifft(
                np.fft.fftshift(
                    self.signal['swFTfilt']))

        self.signal['theta'] = np.unwrap(np.angle(self.signal['z']))/(2*np.pi)
        self.signal['a'] = abs(self.signal['z'])
        
        new_report = []
        new_report.append("Apply an inverse Fourier transform.")
        
        self.report.append(" ".join(new_report))
        
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
        
        id = int(self.signal['td']/self.signal['dt'])
        
        self.signal['z'] = self.signal['z'][id:-id]
        self.signal['theta'] = self.signal['theta'][id:-id]
        self.signal['a'] = self.signal['a'][id:-id]
        self.signal['t'] = self.signal['t'][id:-id]
 
        new_report = []
        new_report.append("Remove the leading and trailing ripple")
        new_report.append("({0} points) from the complex signal.".format(id))
        new_report.append("Compute the signal phase and amplitude.")
        
        self.report.append(" ".join(new_report))
        
    def fit(self,dt_chunk_target):
        
        """
        Fit the phase *vs* time data to a line.  The slope of the line is the
        (instantaneous) frequency. The phase data is broken into "chunks", with  
        
        :param float dt_chunk_target: the target chunk duration [s]
        
        If the chosen duration is not an integer multiple of the digitization
        time, then find the nearest chunk duration which is.  Create the 
        following objects in the *Signal* object
        
        :param np.array signal['fit_time']: the time at the start of each chunk
        :param np.array signal['fit_freq']: the best-fit frequency during each chunk
        
        Calculate the slope :math:`m` of the phase *vs* time line using
        the linear-least squares formula
        
        .. math::
            
            \\begin{equation}
            m = \\frac{n \\: S_{xy} - S_x S_y}{n \\: S_{xx} - (S_x)^2}
            \\end{equation}
        
        with :math:`x` representing time, :math:`y` representing
        phase, and :math:`n` the number of data points contributing to the 
        fit.  The sums involving the :math:`x` (e.g., time) data can be computed
        analytically because the time data here are equally spaced.  With the 
        time per point :math:`\\Delta t`, 
        
        .. math::
            
            \\begin{equation}
            S_x = \\sum_{k = 0}^{n-1} x_k = \\sum_{k = 0}^{n-1} k \\: \\Delta t
             = \\frac{1}{2} \\Delta t \\: n (n-1)
            \\end{equation}
            
            \\begin{equation}
            S_{xx} = \\sum_{k = 0}^{n-1} x_k^2 = \\sum_{k = 0}^{n-1} k^2 \\: {\\Delta t}^2
             = \\frac{1}{6} \\Delta t \\: n (n-1) (2n -1)
            \\end{equation}
        
        The sums involving :math:`y` (e.g., phase) can not be similarly
        precomputed. These sums are

        .. math:: 
                       
             \\begin{equation}
             S_y =  \\sum_{k = 0}^{n-1} y_k = \\sum_{k = 0}^{n-1} \\phi_k
             \\end{equation} 

             \\begin{equation}
             S_{xy} =  \\sum_{k = 0}^{n-1} x_k y_k = \\sum_{k = 0}^{n-1} (k \\Delta t) \\: \\phi_k
             \\end{equation}         
        
        To avoid problems with round-off error, a constant is subtracted from 
        the time and phase arrays in each chuck so that the time array
        and phase array passed to the least-square formula each start at
        zero.  
                                                                                                                
        """

        # work out the chunking details

        n_per_chunk = int(round(dt_chunk_target/self.signal['dt']))
        dt_chunk = self.signal['dt']*n_per_chunk
        n_tot_chunk = int(round(self.signal['theta'].size/n_per_chunk))
        n_total = n_per_chunk*n_tot_chunk
        
        # report the chunking details
        
        new_report = []
        new_report.append("Curve fit the phase data.")
        new_report.append("The target chunk duration is")
        new_report.append("{0:.3f} us;".format(1E6*dt_chunk_target))
        new_report.append("the actual chunk duration is")
        new_report.append("{0:.3f} us".format(1E6*dt_chunk))
        new_report.append("({0} points).".format(n_per_chunk))
        new_report.append("{0} chunks will be curve fit;".format(n_tot_chunk))
        new_report.append("{0:.3f} ms of data.".\
            format(1E3*self.signal['dt']*n_total))
        
        start = time.time() 
        
        # reshape the phase data
        #  zero the phase at start of each chunk
        
        s_sub = self.signal['theta'][0:n_total].reshape((n_tot_chunk,n_per_chunk))
        s_sub_reset = s_sub - s_sub[:,:,np.newaxis][:,0,:]*np.ones(n_per_chunk)

        # reshape the time data
        #  zero the time at start of each chunk

        t_sub = self.signal['t'][0:n_total].reshape((n_tot_chunk,n_per_chunk))
        t_sub_reset = t_sub - t_sub[:,:,np.newaxis][:,0,:]*np.ones(n_per_chunk)

        # use linear least-squares fitting formulas
        #  to calculate the best-fit slope

        SX = (self.signal['dt'])*0.50*(n_per_chunk-1)*(n_per_chunk)
        SXX = (self.signal['dt'])**2*(1/6.0)*\
            (n_per_chunk)*(n_per_chunk-1)*(2*n_per_chunk-1)

        SY = np.sum(s_sub_reset,axis=1)
        SXY = np.sum(t_sub_reset*s_sub_reset,axis=1)

        slope = (n_per_chunk*SXY-SX*SY)/(n_per_chunk*SXX-SX*SX)

        stop = time.time()
        t_calc = stop - start
                                
        # save the slope and the associated time axis
        
        self.signal['fit_freq'] = slope
        self.signal['fit_time'] = t_sub[:,0]
        
        # report the curve-fitting details
        #  and prepare the report
        
        new_report.append("It took {0:.1f} ms".format(1E3*t_calc))
        new_report.append("to perform the curve fit and obtain the frequency.")
                 
        self.report.append(" ".join(new_report))       
                       
    def plot_phase_fit(self, delta=False, baseline=0, LaTeX=False):
       
        """
        Plot the frequency [Hz] *vs* time [s].   
        
        :param str delta: plot the frequency shift :math:`\\Delta f` (``False``) 
            or the absolute frequency :math:`f` (``False``; default).
        :param float baseline: the duration of time used to compute the
            baseline frequency
        :param boolean LaTeX: use LaTeX axis labels; ``True`` or ``False``
            (default) 
           
        In the ``True`` case, the frequency shift is calculated by subtracting
        the peak frequency **.signal['f00']** determined by the *filter()* 
        function.  If a non-zero number is given for ``baseline``, then the
        first ``baseline`` seconds of frequency shift is used as the reference
        from which the frequency shift is computed.  Display the baseline
        frequency used to compute the frequency shift in the plot title.  
        If ``delta=False`` then plot the frequency shift in units of kHz; if
        ``delta=True``, then plot the frequency shift in Hz.
        
        """
        
        # plotting using tex is nice, but slow
        #  so only use it temporarily for this plot
        
        old_param = plt.rcParams['text.usetex']
        
        if LaTeX == True:
            
            plt.rcParams['text.usetex'] = True
            x_labelstr = r"$t \: \mathrm{[s]}$"
            
        elif LaTeX == False:
            
            plt.rcParams['text.usetex'] = False
            x_labelstr = "t [s]"
        
        # decide what data to plot
        
        x = self.signal['fit_time']
        
        if delta == False: 
            
            y = self.signal['fit_freq']/1E3
            y_lim = [0,1.5*self.signal['fit_freq'].max()/1E3]
                            
            if LaTeX == True:
                
                y_labelstr = r"$f \: \mathrm{[kHz]}$"
                titlestr = ""
                
            elif LaTeX == False:
                
                y_labelstr = "f [kHz]"
                titlestr = ""
                
        elif delta == True:
            
            y = self.signal['fit_freq']
            
            if baseline == 0:
            
                self.signal['f_baseline'] = self.signal['f00']
                
            elif baseline != 0:
                
                # a = array([True, True, ... False,  False,  ...], dtype=bool)
                # ~a = array([False, False, ... True,  True,  ...], dtype=bool)
                # 
                # np.arange(0,len(a))[~a].min() is then the index of the first
                #  element in the array a at which time S.signal['fit_time'] is 
                #  baseline seconds larger than S.signal['fit_time'][0]
                #
                
                a = self.signal['fit_time'] - \
                    self.signal['fit_time'][0] < baseline
                    
                a_first = np.arange(0,len(a))[~a].min()
                
                self.signal['f_baseline'] = y[0:a_first].mean()
                
            y = y - self.signal['f_baseline']
            y_value = max(abs(y.min()),abs(y.max()))
            y_lim = [-1.5*y_value,1.5*y_value] 
            
            if LaTeX == True:
            
                y_labelstr = r"$\Delta f \: \mathrm{[Hz]}$"                          
                titlestr = r"$f_0 = " + \
                        "{0:.3f}".format(self.signal['f_baseline']) + \
                        r" \: \mathrm{Hz}$"
                        
            elif LaTeX == False:
                
                y_labelstr = "Delta f [Hz]"
                titlestr = "f_0 = {0:.3f} [Hz]".format(self.signal['f_baseline'])
                                                
        else:
            
            print r"delta option not understood -- should be False or True "
        
        
        # create the plot
        
        fig=plt.figure(facecolor='w')
        plt.plot(x,y)
        
        # axes limits and labels
        
        plt.xlim([self.signal['t_original'][0],self.signal['t_original'][-1]])
        plt.ylim(y_lim)
        plt.xlabel(x_labelstr)
        plt.ylabel(y_labelstr)
        plt.title(titlestr)
        
        # set text spacing so that the plot is pleasing to the eye

        plt.locator_params(axis = 'x', nbins = 4)
        plt.locator_params(axis = 'y', nbins = 4)
        fig.subplots_adjust(bottom=0.15,left=0.12) 
        
        # don't forget to show the plot abd reset the tex option
        
        plt.show()
        plt.rcParams['text.usetex'] = old_param

    def plot_phase(self, delta=False, LaTeX=False):
        
        """
        Plot the phase *vs* time.
        
        :param str delta: plot the phase shift :math:`\\Delta\\phi/2\\pi`
            (``True``) [cycles] or the absolute phase :math:`\\phi/2\\pi` 
            [kilocycles] (``False``; default).
            
        :param boolean LaTeX: use LaTeX axis labels; ``True`` or ``False``
            (default) 
           
        The phase shift :math:`\\Delta\\phi/2\\pi` is calculated by fitting
        the phase *vs* time data to a line and subtracting off the best-fit
        line as follows:
            
        .. math::
        
            \\begin{equation}
            \\Delta\\phi/2 \\pi = \\phi/2 \\pi - (c_0 \\: t + c_1)
            \\end{equation}
            
        where :math:`c_0` is the best-fit phase at :math:`t=0` and :math:`c_1` 
        is the best-fit frequency [Hz].  If ``delta=True``, then report the 
        best-fit line in the plot title.    
           
        """ 
 
        # use tex-formatted axes labels temporarily for this plot
        
        old_param = plt.rcParams['text.usetex']
        
        if LaTeX == True:
        
            plt.rcParams['text.usetex'] = True
            x_label = r"$t \: \mathrm{[s]}$"
            
        elif LaTeX == False:
            
            plt.rcParams['text.usetex'] = False
            x_label = "t [s]"
 
        # decide what to plot
        
        x = self.signal['t']
 
        if delta == False: 
            
            y = self.signal['theta']/1E3
            y_lim = [0,self.signal['theta'].max()/1E3]
            
            if LaTeX == True:                        
                                                
                y_labelstr = r"$\phi /2 \pi \: \mathrm{[kilocycles]}$"
                titlestr = ""  
       
            elif LaTeX == False:
                
                 y_labelstr = "phase/(2*pi) [kilocycles]"
                 titlestr = ""    
                  
        elif delta == True:
       
            coeff = np.polyfit(self.signal['t'], self.signal['theta'], 1)
            y_calc = coeff[0]*self.signal['t'] + coeff[1]
            y = self.signal['theta'] - y_calc
            y_value = max(abs(y.min()),abs(y.max()))
            y_lim = [-1.5*y_value,1.5*y_value]
            
            if LaTeX == True:
                
                y_labelstr = r"$\Delta\phi /2 \pi \: \mathrm{[cycles]}$"
                titlestr = r"$\phi_0 = " + \
                        "{0:.3f} t  {1:+.3f}".format(coeff[0],coeff[1]) + \
                        r" \: \mathrm{cycles}$"
                        
            elif LaTeX == False:
                
                y_labelstr = "Delta phase/(2*pi) [cycles]"
                titlestr = "phase(0) = {0:.3f} t + " \
                    "{1:+.3f} [cycles]".format(coeff[0],coeff[1])
        
        # create the plot
        
        fig=plt.figure(facecolor='w')
        plt.plot(x,y)
                        
        # axes limits and labels
        
        plt.xlim([self.signal['t_original'][0],self.signal['t_original'][-1]])
        plt.ylim(y_lim)
        plt.xlabel(x_label)
        plt.ylabel(y_labelstr)
        plt.title(titlestr)
                
        # set text spacing so that the plot is pleasing to the eye

        plt.locator_params(axis = 'x', nbins = 4)
        plt.locator_params(axis = 'y', nbins = 4)
        fig.subplots_adjust(bottom=0.15,left=0.12)         
                        
        # don't forget to show the plot abd reset the tex option
        
        plt.show()
        plt.rcParams['text.usetex'] = old_param
        
    def plot_signal(self, LaTeX=False):
        
        """Plot the windowed signal *vs* time.  
        
        :param boolean LaTeX: use LaTeX axis labels; ``True`` or ``False``
            (default) 
            
        Before you call this function, you must have run the ``.window()`` 
        function first.  Because the signal is likely to have many oscillations
        that would be too difficult to see if we plotted all the signal, instead
        draw subplots that zoom in to the beginning, middle, and end of the data. 
        
        Decide what duration of data to plot as follows: 
        
        * beginning and end: use twice the window rise/fall time, 
          **.signal['tw_actual']**
          
        * middle: use 10 times the period of the primary oscillation. Determine 
          this period by taking a Fourier transform of a short, 1024-point, 
          initial segment of the signal.  Identify the primary oscillation 
          frequency as the peak in the Fourier tranform.  Determine the
          oscillation period as the inverse of this oscillation frequency.
            
        The x-axis of each plot is the *relative* time in milliseconds; 
        display in the plot title the relevant time offsets used to create
        each subplot.  The y-axis is the signal, plotted using the variable name
        and units given at initialization time. 
        
        *Programming notes*: We use the relative time as the x-axis because it
        results in much nicer axis labels.  If instead we use the absolute time 
        in seconds as the x-axis, then matplotlib will create x-axis plot labels
        for the middle and end plots like "0.000", "0.001", and put a
        "+4.567831" below -- very ugly. So instead we plot the relative time in
        milliseconds, which yields x-axis plot labels like "0", "1", etc.  It is 
        a small chore for us to now report the relevant time offset ("4.5673" in 
        this example) in the plot title.
        
        """

        # at the beginning and end
        #  look at a stretch of data which is 2x the rise/fall time
        #  determined by the .window() function
        
        i0_del = int(math.floor(2*self.signal['tw_actual']/self.signal['dt']))
        i_end = self.signal['t'].size
          
        # For the middle section, we want to display approximately 
        #  10 cycles of the signal.  We may not have taken the FT of the
        #  data yet.  So here we take an FT of the leading 1024 points 
        #  of the signal and use it to determine the peak frequency
        #  (which may be negative)                              
        
        sFT = np.fft.fftshift(np.fft.fft(self.signal['s'][0:1024]))
        f = np.fft.fftshift(np.fft.fftfreq(1024,d=self.signal['dt']))        
        f0_est = f[np.argmax(abs(sFT))]
        t_delta = 10/abs(f0_est)
        i1_del = int(math.floor(t_delta/self.signal['dt']))
                
        # posslby use tex-formatted axes labels temporarily for this plot
        # compute plot labels
        
        old_param = plt.rcParams['text.usetex']
        
        if LaTeX == True:
        
            plt.rcParams['text.usetex'] = True

            x_label = r"$\Delta t \: \mathrm{[ms]}$"
            y_label = r"$" + "{}".format(self.signal['s_name']) + \
                "\: \mathrm{[" + "{}".format(self.signal['s_unit']) + "]}$"            
                                    
        elif LaTeX == False:
            
            plt.rcParams['text.usetex'] = False                
        
            x_label = "Delta t [ms]"
            y_label = "{0} [{1}]".format(self.signal['s_name'],
                self.signal['s_unit'])
        
        # create the plot
        
        fig=plt.figure(facecolor='w')
        
        plt.subplot(131)    
        i1 = list(np.arange(0,i0_del))
        t1 = 1E3*(self.signal['t'][i1])
        plt.plot(t1-t1[0],self.signal['sw'][i1])
        plt.xlim(0,max(t1-t1[0]))
        plt.xlabel(x_label,labelpad=20)
        plt.ylabel(y_label)
        plt.locator_params(axis = 'x', nbins = 4)
        
        ax2=plt.subplot(132)
        i2 = list(np.arange(i_end/2-i1_del/2,i_end/2+i1_del/2))
        t2 = 1E3*(self.signal['t'][i2])
        plt.plot(t2-t2[0],self.signal['sw'][i2])
        plt.xlim(0,max(t2-t2[0]))
        plt.xlabel(x_label,labelpad=20)
        plt.setp(ax2.get_yticklabels(), visible=False)
        plt.locator_params(axis = 'x', nbins = 4)
        
        ax3=plt.subplot(133)
        i3 = list(np.arange(i_end-i0_del,i_end))
        t3 = 1E3*(self.signal['t'][i3])
        plt.plot(t3-t3[0],self.signal['sw'][i3])
        plt.xlim(0,max(t3-t3[0]))
        plt.xlabel(x_label,labelpad=20)
        plt.setp(ax3.get_yticklabels(), visible=False)
        plt.locator_params(axis = 'x', nbins = 4)        
        
        title_str = "signal at time offsets " + \
            "{0:.4f}, ".format(t1[0]/1E3) + \
            "{0:.4f}, and ".format(t2[0]/1E3) + \
            "{0:.4f} s".format(t3[0]/1E3)
        
        plt.title(title_str, size=14, horizontalalignment='right') 
        
        # clean up label spacings, show the plot, and reset the tex option
        
        fig.subplots_adjust(bottom=0.15,left=0.12)    
        plt.show()
        plt.rcParams['text.usetex'] = old_param  

    def plot_fft(self, autozoom=True, LaTeX=False):
        
        """
        Plot on a logarithmic scale the absolute value of the FT-ed signal, 
        the bandpass-filtered FT-ed signal, and the band-pass filter function
        *vs* frequency in kilohertz. Before you call this function, you must
        have run the ``.fft()`` and ``.filter()`` functions first.  
        
        :param str autozoom: zoom into a region of interest near the primary 
            peak in the FT-ed signal (``True`` default) or display the FT-ed signal
            over the full range of positive frequencies (``False``).
            
        :param boolean LaTeX: use LaTeX axis labels; ``True`` or ``False``
            (default) 
            
        If ``autozoom=True``, then determine the region of interest using 
        **.signal['bw']** and **.self.signal['f0']**.  For purposes of display,
        the filter is scaled to the maximum of the FT-ed signal.
        
        Only plot data at positive frequencies, because (1) we are plotting
        using a logarithmic y scale, (2) the filter function sets to zero the
        data at negative frequencies, and (3) the log of zero is minus infinity.
        For these reasons the negative-frequency data will not show up on a
        semilog plot. 
                
        """

        # possibly use tex-formatted axes labels temporarily for this plot
        
        old_param = plt.rcParams['text.usetex']
        
        if LaTeX == True:
            
            plt.rcParams['text.usetex'] = True
            x_label = r"$f \: \mathrm{[kHz]}$"
            y_label = r"$\hat{" + "{}".format(self.signal['s_name']) + \
                "}(f) \: \mathrm{[" + "{}".format(self.signal['s_unit']) + \
                "/\mathrm{Hz}]}$"
                
        elif LaTeX == False:
            
            plt.rcParams['text.usetex'] = False
            x_label = "f [kHz]"
            y_label = "FT{{{0}}} [{1}/Hz]".format(self.signal['s_name'],
                self.signal['s_unit'])       
             
        # set the plotting range (e.g., zoomed or not)              
                                        
        f = self.signal['f']
        f_lower = self.signal['f0'] - 1.50*self.signal['bw']
        f_upper = self.signal['f0'] + 1.50*self.signal['bw']
                        
        if autozoom == True:
            
            test = (f >= 0) & (f <= f_upper) & (f >= f_lower)
        
        elif autozoom == False:
            
            test = (f >= 0)
            
        sub_indices = np.arange(0,self.signal['f'].size)[test]
        
        # normalization constant
        
        nc = self.signal['dt']
        
        # create the appropriate data subsets --
        #  since we only want to plot the band-pass filtered data, 
        #  scale signal['swFTfilt'] by a factor of 0.5 to "undo"
        #  the rh filter.      
                    
        x = 1E-3*self.signal['f'][sub_indices]
        y1 = abs(nc*self.signal['swFT'])[sub_indices]
        y1_max = y1.max()
        
        y2 = (y1_max*self.signal['bp'])[sub_indices]        
        y3 = abs(nc*0.5*self.signal['swFTfilt'])[sub_indices] 

        # create the plot
        
        fig=plt.figure(facecolor='w')

        if LaTeX == True:        
                        
            plt.plot(x,y1, label=r"$\mathrm{fft}$")
            plt.plot(x,y2, label=r"$\mathrm{filter}$")
            plt.plot(x,y3, label=r"$\mathrm{fft, filtered}$")
            
        elif LaTeX == False:
            
            plt.plot(x,y1, label="fft")
            plt.plot(x,y2, label="filter")
            plt.plot(x,y3, label="fft, filtered")            
        
        # add legend, labels, and y-axis limits
        
        plt.legend(loc='upper right')
        plt.xlabel(x_label, labelpad=20)
        plt.ylabel(y_label)
        plt.yscale('log')
        plt.ylim([1E-6*y1_max,10*y1_max])
        
        # clean up label spacings, show the plot, and reset the tex option
          
        fig.subplots_adjust(bottom=0.15,left=0.12)   
        plt.show()
        plt.rcParams['text.usetex'] = old_param  
                                                      
    
    def __repr__(self):

        """
        Make a report of the (original) signal's properties including its name,
        unit, time step, rms, max, and min.
        
        """

        #s_rms = np.sqrt(np.mean(self.signal['s']**2))
        #s_min = np.min(self.signal['s'])
        #s_max = np.max(self.signal['s'])

        temp = []
        
        #temp.append("Signal")
        #temp.append("======")
        #temp.append("signal name: {0}".format(self.signal['s_name']))
        #temp.append("signal unit: {0}".format(self.signal['s_unit']))
        #temp.append("signal lenth = {}".format(len(self.signal['s'])))
        #temp.append("time step = {0:.3f} us".format(self.signal['dt']*1E6))
        #temp.append("rms = {}".format(eng(s_rms)))
        #temp.append("max = {}".format(eng(s_max)))
        #temp.append("min = {}".format(eng(s_min)))
        #temp.append(" ")
        temp.append("Signal Report")
        temp.append("=============")
        temp.append("\n\n".join(["* " + msg for msg in self.report]))

        return '\n'.join(temp)


def testsignal_sine():
        
    fd = 50.0E3    # digitization frequency
    f0 = 5.00E3    # signal frequency
    nt = 60E3      # number of signal points    
    sn = 1.0       # signal zero-to-peak amplitude
    sn_rms = 0.20  # noise rms amplitude
    
    dt = 1/fd
    t = dt*np.arange(nt)
    s = sn*np.sin(2*np.pi*f0*t) + np.random.normal(0,sn_rms,t.size)
    
    S = Signal('temp.h5')
    S.load_nparray(s,"x","nm",dt)
    S.close()
    
    S.open('temp.h5')
    S.plot('y', LaTeX=latex)
    
    return S
    
#    S.binarate("middle")   
#    S.window(3E-3)
#    S.plot_signal(LaTeX=latex)
#    S.fft()
#    S.filter(1E3)
#    S.plot_fft(autozoom=True,LaTeX=latex)
#    S.ifft()
#    S.trim()
#    S.plot_phase(delta=True,LaTeX=latex)
#    S.fit(201.34E-6)
#    S.plot_phase_fit(delta=True,LaTeX=latex) 
#         
#    print(S)
#    return(S)
#


if __name__ == "__main__":
    
    # Parge command-line arguments
    # https://docs.python.org/2/library/argparse.html#module-argparse
    
    import argparse
    from argparse import RawTextHelpFormatter
    
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
        description="Determine a signal's frequency vs time.\n"
        "Example usage:\n"
        "    python demodulate.py --testsignal=sine --LaTeX\n\n")
    parser.add_argument('--testsignal',
        default='sine',
        choices = ['sine', 'sineexp'],
        help='analyze one of the available test signals')
    parser.add_argument('--LaTeX',
        dest='latex',
        action='store_true',
        help = 'use LaTeX plot labels')
    parser.add_argument('--no-LaTeX',
        dest='latex',
        action='store_false',
        help = 'do not use LaTeX plot labels (default)')
    parser.set_defaults(latex=False)    
    args = parser.parse_args()
    
    # Set the default font and size for the figure
    
    font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : 18}

    plt.rc('font', **font)
    plt.rcParams['figure.figsize'] =  8.31,5.32
    
    latex = args.latex
    
    # Do one of the tests
    
    if args.testsignal == 'sine':
        
        S = testsignal_sine()
        
    else:
        
        print "**warning **"
        print "--testsignal={} not implimented yet".format(args.testsignal)
