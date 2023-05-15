#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# thermomechanical.py
# John A. Marohn
# 2023/05/10

"""

Fit cantilever thermomechanical fluctuation power spectrum to theory.  
Obtain the cantilever spring constant from the area under the power
spectrum.

"""
from __future__ import division, print_function, absolute_import
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
from freqdemod.demodulate import Signal
from collections import OrderedDict
from freqdemod.hdf5 import update_attrs
import h5py
from pint import UnitRegistry
from freqdemod.util import nearest2power
from freqdemod.util import find_nearest
from lmfit import Model
from lmfit import Parameters

ureg = UnitRegistry()

def harmosc(X, Q, F):
    """
    Damped harmonic oscillator with random driving force.
    """
    x, p = X
    dotx = p
    dotp = - x - (1 / Q) * p + F
    return np.array([dotx, dotp])

def solve(X0, dtau, Q, F):
    X = np.zeros([len(F), 2])
    X[0] = X0
    for n, f in enumerate(F[:-1]):
        X[n+1, :] =  X[n, :] + dtau * harmosc(X[n], Q, f)
    return X

def thermconstants(T, k, f0, Q, dtau, verbose=False):

    kb = ureg.Quantity(1.380649e-23, 'J/K')
    xth = np.sqrt((4 * kb * T)/(k * Q * dtau)).to_base_units()
    w0 = 2 * np.pi * f0
    pth = ((k / w0) * xth).to_base_units()

    if verbose:
        print('x thermal = {:6.3f} pm = {:0.3e} m'.format(
            xth.to('pm').magnitude, 
            xth.to_base_units().magnitude))
        print('p thermal = {:6.3f} ug pm / us = {:0.3e} kg m/s'.format(
            pth.to('ug pm / us').magnitude,
            pth.to_base_units().magnitude))
        
    return xth, pth

def brownian(f, A, tau0, f0, B):

    """
    Compute the power spectrum of position fluctuations as a function of frequency f for a harmonic oscillator. We fit the power spectrum of cantilever thermal fluctuations to the following function

    .. math::
    
    \\begin{equation}
    P_{\\delta x}(f) = A \\, 
    \\frac{(\\pi \\tau_0 f_0)^2}
        { (\\pi \\tau_0)^4 ((f_0^2 - f^2)^2) - (\\pi \\tau_0)^2 f^2}
    + B
    \\end{equation}

    The parameter :math:`\\tau_0` is the cantilever ringdown time and :math:`f_0` is the resonance frequency.  The product :math:`\\tau_0 f_0`` is unitless, so :math:`\\tau_0`'s units are reciprocal to :math:`f` and :math:`f_0`'s units; that is, if the unit of :math:`f` and :math:`f_0` is kHz, then the unit of :math:`\\tau_0` is ms.  The parameters :math:`A` and :math:`B` are, respectively, the peak height and  interferometer baseline in the vicinity of resonance.  These parameters take the units of :math:`P_{\delta x}(f)`, either nm :math:`^2` / Hz or, preferably, pm :math:`^2` / sHz. 
    
    """
    
    F = np.pi*tau0*f   # unitless frequency
    F0 = np.pi*tau0*f0 # unitless resonance frequency
    
    return (A*F0**2)/((F**2-F0**2)**2 + F**2) + B

class PSD(object):

    def __init__(self, filename=None, mode='w-', driver='core', backing_store=False):

        """
        Copy the initialization routine from the Signal object.  Set the initial
        number of averages and signal mean and standard deviation to zero.

        """

        Signal.__init__(self, filename, mode, driver, backing_store)
        self.Navg = 0
        self.mean = 0
        self.std = 0
        self.fitted = False
    
    def close(self):
        Signal.close(self)

    def plot(self, ordinate, LaTeX=False, component='abs'):
        Signal.plot(self, ordinate, LaTeX, component)
        """Copy the generic plotting function from the Signal object."""

    def plot_psd(self, LaTeX=False, x_scale='linear', y_scale='log'):
        """Plot the power spectrum in `self.f['psd']`. """
        
        # The x and y datasets

        y = self.f['psd']
        x = self.f[y.attrs['abscissa']]

        # Possibly use tex-formatted axes labels temporarily for this plot
        # and compute plot labels
        
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

        # The x and y numpy arrays

        y = y[()]
        x = x[()]

        if self.fitted:

            yfit = self.f['fit'][()]
            yerr = y/np.sqrt(self.Navg)
            resid = (yfit - y) / yerr

            fig, axs = plt.subplots(nrows=2, ncols=2, 
                figsize=(8, 6), 
                sharex='col',
                sharey='row',
                height_ratios = [2, 5],
                width_ratios = [3,1],
                tight_layout=True)

            axs[0][0].plot(x, resid)
            axs[0][0].set_ylabel('norm. resid.')

            counts, edges = np.histogram(resid, bins=50)
            axs[0][1].stairs(counts, edges, fill=True, orientation="horizontal")
            axs[0][1].set_xlabel('counts')

            msg1 = '{:0.3f}'.format(resid.mean())
            msg2 = '{:0.3f}'.format(resid.std())

            axs[0][1].text(counts.max(), resid.max(),
                msg1 + '\n $\pm$ ' + msg2, 
                fontsize=12, 
                horizontalalignment='right',
                verticalalignment='top')

            axs[1][0].loglog(x, y) 
            axs[1][0].loglog(x, yfit, 'k-') 
            axs[1][0].set_xlabel(x_label_string)
            axs[1][0].set_ylabel(y_label_string)

            fig.delaxes(axs[1][1])
            fig.align_ylabels()
            plt.show()

        else:

            plt.subplots(1, 1, figsize=(8, 5), tight_layout=True)
            plt.plot(x[()], y[()])
            plt.xscale(x_scale)
            plt.yscale(y_scale)
            plt.title(title_string)
            plt.xlabel(x_label_string)
            plt.ylabel(y_label_string)
            plt.show()

       # show the plot, and reset the tex option

        plt.show()
        plt.rcParams['text.usetex'] = old_param

    def fitPx(self, Temp=300):
        """Fit thermal position fluctuations to theory to obtain the cantilever parameters."""

        gmodel = Model(brownian)
        params = Parameters()

        y = self.f['psd'][()]
        x = self.f['freq'][()]

        # The initial guess for the amplitude is max in the spectrum.

        params.add('A', value=y.max(), min=0)

        # The initial guess for the resonance frequency is the frequency 
        # at which that max occurs.

        params.add('f0', value=x[np.argmax(y)], min=0)

        # Estimate the baseline from the values of the spectrum at the
        # start and end of the spectrum -- take whichever is smaller.

        Bguess = min(y[0], y[-1])
        params.add('B', value=Bguess, min=0)

        # Find the location of the peak in the spectrum, `index1`.  
        # Find the location where the spectrum is half the max height, `index2`.  
        # Determine the difference in the frequencies at the two indices.  
        # Twice this value is the linewidth, and the ringdown time is 
        # the inverse of this linewidth.

        index1, _ = find_nearest(y, y.max())
        index2, _ = find_nearest(y, y.max()/2)
        tau0guess = 1/(2 * abs(x[index2] - x[index1]))
        params.add('tau0', value=tau0guess, min=0)

        result = gmodel.fit(data=y[()], 
            params=params, 
            f=x[()], 
            weights=np.sqrt(self.Navg)/y[()])

        self.f['fit'] = result.best_fit
        self.fitted = True # for plotting
        
        # Save the fitted parameter values and error bars in a dictionary

        self.valueU = {'A': ureg.Quantity(result.params['A'].value, 'pm**2/Hz'),
           'f0': ureg.Quantity(result.params['f0'].value, 'kHz'),
           'B': ureg.Quantity(result.params['B'].value, 'pm**2/Hz'),
           'tau0': ureg.Quantity(result.params['tau0'].value, 'ms')}

        self.stderrU = {'A': ureg.Quantity(result.params['A'].stderr, 'pm**2/Hz'),
                'f0': ureg.Quantity(result.params['f0'].stderr, 'kHz'),
                'B': ureg.Quantity(result.params['B'].stderr, 'pm**2/Hz'),
                'tau0': ureg.Quantity(result.params['tau0'].stderr, 'ms')}
        
        # Derive the dissipation constant and spring constant, 
        # propagating error bars

        self.valueU['Q'] = (np.pi * self.valueU['f0'] * self.valueU['tau0']).to('dimensionless')
        self.stderrU['Q'] = (self.valueU['Q'] * np.sqrt( 
            np.power(self.stderrU['f0'] / self.valueU['f0'], 2.0) 
            + np.power(self.stderrU['tau0'] / self.valueU['tau0'], 2.0))).to('dimensionless')

        kb = ureg.Quantity(1.380649e-23, 'J/K')
        T = ureg.Quantity(Temp, 'K')

        self.valueU['Gamma'] = ((kb * T)/((
            np.pi**2) * (self.valueU['f0']**2) * self.valueU['A'])).to('pN s/m')
        self.stderrU['Gamma'] = (self.valueU['Gamma'] * np.sqrt( 
            np.power(2 * self.stderrU['f0'] / self.valueU['f0'], 2.0) 
            + np.power(self.stderrU['A'] / self.valueU['A'], 2.0))).to('pN s/m')       

        self.valueU['k'] = ((2*self.valueU['tau0'] * kb * T)/self.valueU['A']).to('N/m')
        self.stderrU['k'] = (self.valueU['k'] * np.sqrt( 
            np.power(self.stderrU['tau0'] / self.valueU['tau0'], 2.0) 
            + np.power(self.stderrU['A'] / self.valueU['A'], 2.0))).to('N/m')

        for key in  self.valueU.keys():
            print('{:<10} = {:0.4e} +/- {:0.4e}'.format(
                key, self.valueU[key].magnitude,  # just the number
                self.stderrU[key]))               # the number with unit

        return result

    def load_signal(self, s, psd_help='power spectrum'):
       
        """
        Create a *PSD* object from the following inputs. 
        
        :param s: Signal object
        
        Add the following objects to the *PSD* object
        
        :param h5py.File f: an h5py object stored in core memory 
        :param str report: a string summarizing in words what has
            been done to the signal 
        
        It is assumed that `s.f['/workup/freq/freq']` and 
        `s.f['/workup/freq/FT']` exist.  These dataset and their associated
        attributes are copied to `self.f['freq']` and `self.s['FT']` respectively.
        If you try to load another signal into an already existing PSD object,
        it is assumed you want to signal-average the power spectrum.

        """
   
        if self.Navg == 0:

            # copy everything over from the Signal object

            freq =  s.f['/workup/freq/freq']            
            self.f['freq'] = freq[()]
            update_attrs(self.f['freq'].attrs, OrderedDict(freq.attrs.items()))

            psd = s.f['/workup/freq/FT']
            self.f['psd'] = psd[()]
            update_attrs(self.f['psd'].attrs, OrderedDict(psd.attrs.items()))
            self.f['psd'].attrs['abscissa'] = 'freq' # overwrite

            new_report = []
            new_report.append("Add a psd signal of length {}".format(len(self.f['freq'])))
            self.report.append(" ".join(new_report))

            self.Navg += 1

        else:

            # running average, stored in place

            psd_old = self.f['psd'][()]
            psd_current = s.f['/workup/freq/FT'][()]

            n = self.Navg
            psd_new = (n / (n + 1)) * psd_old + (1 / (n + 1)) * psd_current
            self.f['psd'][...] = psd_new

            self.f['psd'].attrs['n_avg'] += 1
            self.Navg += 1

        self.mean =  self.f['psd'][()].mean()
        self.std = self.f['psd'][()].std()   

def test_signal_detector_noise(plotme):
    """Obtain a target detector noise floor starting with noisy time-series data."""

    Pdet = 1.0e-5   # detector noise in pm^2/Hz
    Npts = 128      # number of time points; a power of two
    Na = 64         # number of averages; a power of two
    dt = 10.0E-6    # time step, determines the Nyquist frequency
    
    t  = np.linspace(start=0., stop=dt*(Npts-1), num=Npts)
    unit_noise = np.random.normal(0., 1., Npts)

    psd = PSD()
    for k in np.arange(Na):
    
        s = Signal()
        s.load_nparray(np.sqrt(Pdet/dt) * unit_noise, "x", "pm", dt)
        s.fft(psd=True)
        psd.load_signal(s)
        s.close()

    if plotme:
        psd.plot_psd()

    print('-'*50)
    print('detector noise test report')
    print('-'*50)
    print('unit normal std = {:0.4f}'.format(unit_noise.std()))
    print('target psd = {:0.4e} +/- {:0.4e} pm^2/Hz'.format(Pdet, Pdet/np.sqrt(Na)))
    print('actual psd = {:0.4e} +/- {:0.4e} pm^2/Hz'.format(psd.mean, psd.std))
    print('3-sigma relative error = {:0.4f}'.format(3.0/np.sqrt(Na)))
    print(' actual relative error = {:0.4f}'.format((Pdet - psd.mean)/Pdet))
    print('-'*50)

    return(s)

def test_signal_thermal_psd(plotme):
    """Simulate cantilever motion in the time domain and compute a power spectrum."""

    T = ureg.Quantity(300, 'K')    # cantilever temperature
    k = ureg.Quantity(1.0, 'N/m')  # cantilever spring constant
    f0 = ureg.Quantity(100, 'kHz') # cantilever resonance frequency
    Q = 50                         # cantilever quality factor; not too big
    Pdet = 1.0E-5                  # detector noise floor in pm^2/Hz
    Ntau = 128                     # no. time steps per cantilever oscillations (64 or 128, >Q)
    Na = 128                       # no. signal averages; a small power of two (i.e., 8 to 128)

    # Run one large simulation, and break it up into smaller sections
    # for signal-averaging later.  We'll run the simulation for 10 Q cycles of
    # burn-in, discarding the burn-in data later.  For each of Na runs, carry the
    # computation out 16 Q cantilever cycles.  This will give at least 16 independent 
    # points across the cantilever resonance.

    dtau = 1/Ntau
    xth, pth = thermconstants(T, k, f0, Q, dtau, verbose=True)
    tstop = 10 * Q + Na * 16 * Q

    # An array of time points with units

    tu = (1 / (2 * np.pi * f0.to('Hz'))) * np.arange(start=0., stop=tstop, step=dtau)
    dtu = tu[1] - tu[0]

    F = np.random.normal(0., 1., len(tu))  # random force time-series
    xi = 0.0/xth.to_base_units().magnitude # initial reduced position
    pi = 0.0/pth.to_base_units().magnitude # initial reduced momentum
    X0 = np.array([xi, pi])                # unitless initial conditions
    xu = xth * solve(X0, dtau, Q, F)[:, 0] # run the simulation, create position time series

    if plotme:
        plt.subplots(1, 1, figsize=(8, 5), tight_layout=True)
        plt.plot(tu.to('ms').magnitude, xu.to('pm').magnitude)
        plt.xlabel('time [ms]')
        plt.ylabel('position [pm]')
        plt.show()

    # Now discard the burn-in data, reshape the position time-series
    # data so we can pretend we did multiple experiments and average
    # the power spectra over the experiments

    Nxu = nearest2power(len(xu))
    Nchunk = int(Nxu/Na)
    xunew = xu[-Nxu:].reshape((Na, Nchunk))

    # Create an array of detector noise we can add to the simulation

    dtsig = dtu.to('s').magnitude
    xn = np.sqrt(Pdet/dtsig) * np.random.normal(0, 1., Na*Nchunk).reshape((Na, Nchunk))

    # Now loop over the experiments and average the power spectra

    psd = PSD()
    for k in np.arange(Na):
    
        s = Signal()
        xsig = xunew[k,:].to('pm').magnitude + xn[k,:]
        s.load_nparray(xsig, "x", "pm", dtsig)
        s.fft(psd=True)
        psd.load_signal(s)
        s.close()
    
    if plotme:
        psd.plot_psd(x_scale='log')

    return psd  

if __name__ == "__main__":

    import argparse
    from argparse import RawTextHelpFormatter

    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
        description="Analyze cantilever thermomechanical fluctuations.\n"
        "Example usage:\n"
        "    python thermomechanical.py\n\n")
    parser.add_argument('--testsignal',
        default='detector-noise',
        choices = ['detector-noise', 'thermal-psd', 'thermal-psd-fit'],
        help='create analyze a test signal') 
    parser.add_argument('--LaTeX',
        dest='latex',
        action='store_true',
        help = 'use LaTeX plot labels')
    parser.add_argument('--plot',
        dest='plot',
        action='store_true',
        help = 'create plots')
    parser.set_defaults(latex=False)  
    parser.set_defaults(plots=False) 
    args = parser.parse_args()
    
    # Set the default font and size for the figure
    
    font = {'family' : 'serif',
            'weight' : 'normal',
            'size'   : 18}

    plt.rc('font', **font)
    plt.rcParams['figure.figsize'] =  8.31,5.32
    
    latex = args.latex

    # Do one of the tests

    if args.testsignal == 'detector-noise': 
        psd = test_signal_detector_noise(args.plot)
        psd.close()

    if args.testsignal == 'thermal-psd': 
        psd = test_signal_thermal_psd(args.plot)
        psd.close()

    if args.testsignal == 'thermal-psd-fit': 
        psd = test_signal_thermal_psd(args.plot)
        psd.fitPx()
        if args.plot:
            psd.plot_psd(x_scale='linear')
        psd.close()

