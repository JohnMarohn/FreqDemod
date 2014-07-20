Introduction
============

**Summary**.  This package provides functions for analyzing and plotting the time-dependent frequency and amplitude of a sinusoidally oscillating signal.  Additional functions are provided for analyzing fluctuations in oscillator amplitude, phase, or frequency.  The provided functions should work equally well for any oscillating signal, although thee data-fitting and -plotting functions have been written with an oscillating atomic force microscope (AFM) cantilever in mind.  

**Motivation**: The microcantilevers uses in an AFM experiment oscillate with an amplitude between 0.1 to 100 nm and at a frequency in the kilohertz range.  
A number of microcantilever-based experiments rely on meauring the time-dependent oscillation frequency of a cantilever.  These experiments include

* frequency-modulation scanning Kelvin probe force microscopy (FM-SKPM) [#Kikukawa1995jun]_, used to measure a thin film's local capacitance and electrostatic potential;   

* frequency-modulated magnetic resonance force microscopy (FM-MRFM), used to sensitively detect and image electron-spin or nuclear-spin magnetic resonance as a slow [#Garner2004jun]_ [#Alexson2012jul]_ or rapidly-modulated [#Rugar2004jul]_ [#Mamin2007may]_ [#Moore2009dec]_ shift in the resonance frequency of a cantilever; 

* experiments studying the frequency fluctuations experienced by a charged microcantilever near a sample surface.  This apparent frequency noise can be used to probe dielectric fluations arising from thermally-driven atomic motions in the sample below [#Yazdanian2008jun]_ [#Yazdanian2009jun]_ [#Hoepker2011oct]_, light-induced charge detrapping of charges in inorganic [#Cockins2009mar]_ and organic semiconductor films [#Luria2012nov]_, and voltage fluctuations arising from correlated charge motion in an organic field effect transistor [#Lekkala2012sep]_ [#Lekkala2013nov]_.

This package represents a detailed description of the frequency-demodulation algorithm outlined in the Supplementary Information of Reference [#Yazdanian2009jun]_ and in the Ph.D. thesis of Reference [#Moore2011sep]_.

**Algorithm**.  Let 

.. math::

    x(t) = a(t) \cos{(2 \pi f(t) \: t)}
    
be the oscillating cantilever signal, with :math:`a(t)` the cantilever amplitude and :math:`f(t)` the cantilever frequency.  We want to extract :math:`a(t)` and :math:`f(t)` from :math:`x(t)`.  We do this by generating phase-shifted copy of the signal,

.. math::

    y(t) = a(t) \sin{(2 \pi f(t) \: t)}
    
using a Hilbert transform.  Using the original signal and the phase-shifted signal, we compute the instantaneous amplitude as

.. math::

    a(t) = \sqrt{x(t)^2 + y(t)^2}
    
and the instantaneous phase as 

.. math::

    \phi(t) = \arctan{(y(t)/x(t))}  

The instantanous frequency is equal to the slope of the :math:`\phi(t)` *vs* :math:`t` line.

**References**

.. [#Kikukawa1995jun] [**Kikukawa1995jun**] Kikukawa, A.; Hosaka, S. & Imura, R. Silicon :math:`pn` Junction Imaging and Characterization Using Sensitivity Enhanced Kelvin Probe Microscopy. *Appl. Phys. Lett.*,  **1995**, *66*: 3510 - 3512 [http://dx.doi.org/10.1063/1.113780].

.. [#Garner2004jun] [**Garner2004jun**] Garner, S. R.; Kuehn, S.; Dawlaty, J. M.; Jenkins, N. E. & Marohn, J. A. Force-Gradient Detected Nuclear Magnetic Resonance. *Appl. Phys. Lett.*,  **2004**, *84*: 5091 - 5093 [http://dx.doi.org/10.1063/1.1762700].

.. [#Alexson2012jul] [**Alexson2012jul**] Alexson, D. A.; Hickman, S. A.; Marohn, J. A. & Smith, D. D. Single-shot nuclear magnetization recovery curves with force-gradient detection. *Appl. Phys. Lett.*,  **2012**, *101*: 022103 [http://dx.doi.org/10.1063/1.4730610].

.. [#Rugar2004jul] [**Rugar2004jul**] Rugar, D.; Budakian, R.; Mamin, H. J. & Chui, B. W. Single Spin Detection by Magnetic Resonance Force Microscopy. *Nature*,  **2004**, *430*: 329 - 332 [http://dx.doi.org/10.1038/nature02658].

.. [#Mamin2007may] [**Mamin2007may**] Mamin, H. J.; Poggio, M.; Degen, C. L. & Rugar, D. Nuclear Magnetic Resonance Imaging with 90-nm Resolution. *Nat. Nanotechnol.*,  **2007**, *2*: 301 - 306 [http://dx.doi.org/10.1038/nnano.2007.105].

.. [#Moore2009dec] [**Moore2009dec**] Moore, E. W.; Lee, S.-G.; Hickman, S. A.; Wright, S. J.; Harrell, L. E.; Borbat, P. P.; Freed, J. H. & Marohn, J. A. Scanned-Probe Detection of Electron Spin Resonance from a Nitroxide Spin Probe. *Proc. Natl. Acad. Sci. U.S.A.*,  **2009**, *106*: 22251 - 22256 [http://dx.doi.org/10.1073/pnas.0908120106].

.. [#Yazdanian2008jun] [**Yazdanian2008jun**] Yazdanian, S. M.; Marohn, J. A. & Loring, R. F. Dielectric Fluctuations in Force Microscopy: Noncontact Friction and Frequency Jitter. *J. Chem. Phys.*,  **2008**, *128*: 224706 [http://dx.doi.org/10.1063/1.2932254].

.. [#Yazdanian2009jun] [**Yazdanian2009jun**] Yazdanian, S. M.; Hoepker, N.; Kuehn, S.; Loring, R. F. & Marohn, J. A. Quantifying Electric Field Gradient Fluctuations over Polymers Using Ultrasensitive Cantilevers. *Nano Lett.*,  **2009**, *9*: 2273 - 2279 [http://dx.doi.org/10.1021/nl9004332].

.. [#Hoepker2011oct] [**Hoepker2011oct**] Hoepker, N.; Lekkala, S.; Loring, R. F. & Marohn, J. A. Dielectric Fluctuations Over Polymer Films Detected Using an Atomic Force Microscope. *J. Phys. Chem. B*,  **2011**, *115*: 14493 - 14500 [http://dx.doi.org/10.1021/jp207387d].

.. [#Cockins2009mar] [**Cockins2009mar**] Cockins, L.; Miyahara, Y. & Grütter, P. Spatially Resolved Low-Frequency Noise Measured by Atomic Force Microscopy. *Phys. Rev. B*,  **2009**, *79*: 121309 [http://dx.doi.org/10.1103/PhysRevB.79.121309].

.. [#Luria2012nov] [**Luria2012nov**] Luria, J. L.; Hoepker, N.; Bruce, R.; Jacobs, A. R.; Groves, C. & Marohn, J. A. Spectroscopic Imaging of Photopotentials and Photoinduced Potential Fluctuations in a Bulk Heterojunction Solar Cell Film. *ACS Nano*,  **2012**, *6*: 9392 - 9401 [http://dx.doi.org/10.1021/nn300941f].

.. [#Lekkala2012sep] [**Lekkala2012sep**] Lekkala, S.; Hoepker, N.; Marohn, J. A. & Loring, R. F. Charge carrier dynamics and interactions in electric force microscopy. *J. Chem. Phys.*,  **2012**, *137*: 124701 [http://dx.doi.org/10.1063/1.4754602].

.. [#Lekkala2013nov] [**Lekkala2013nov**] Lekkala, S.; Marohn, J. A. & Loring, R. F. Electric force microscopy of semiconductors: Cantilever frequency fluctuations and noncontact friction. *J. Chem. Phys.*,  **2013**, *139*: 184702 [http://dx.doi.org/10.1063/1.4828862].

.. [#Moore2011sep] [**Moore2011sep**] Moore, E. W. 1. Mechanical Detection of Electron Spin Resonance from Nitroxide Spin Probes, 2. Ultrasensitive Cantilever Torque Magnetometry of Magnetization Switching in Individual Nickel Nanorods. Ph.D. Thesis, Cornell University, **2011**.