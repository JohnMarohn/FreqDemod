Conventions and Background
==========================

**Fourier Transform**.  Our frequency-demodulation algorithm implements the Hilbert Transform indirectly, *via* a Discrete Fourier Transform (DFT).  We use the ``numpy.fft`` package [#numpy.fft]_ to carry our the DFT.  This package defines the Fourier transform of the signal :math:`a_n` (having :math:`N` data points, :math:`n = 0, 1, .\ldots, N - 1`) as

.. math::
    :label: eq:DFT  

    A_k = \sum_{n = 0}^{N - 1} a_n \: e^{-2 \pi \imath \, n k / N}

while the inverse Fourier transform is defined as

.. math::
    :label: eq:DIFT  

    a_n = \sum_{k = 0}^{N-1} A_k \: e^{\: 2 \pi \imath \, n k / N}.

In the derivations presented below, we will have need of the continuous Fourier transform.  The continuous analog of the forward transform (equation :eq:`eq:DFT`) is

.. math::
    :label: eq:FT
    
    \hat{a}(f) = \int_{-\infty}^{+\infty} dt \: 
        a(t) \: e^{-2 \pi \imath f t } 

while the continuous analog of the inverse transform (equation :eq:`eq:DIFT`) is
 
.. math::
    :label: eq:IFT
    
    a(t) = \int_{-\infty}^{+\infty} df \: 
        \hat{a}(f) \: e^{\: 2 \pi \imath f t } 

We thus define our Fourier transform in terms of the frequency variable :math:`f \: \sim \: [\text{cycles/s} = \text{Hz}]` and not :math:`\omega = 2 \pi f \: \sim \: [\text{radians/s}]`.  While this transform-variable convention agrees with the convention espoused by *Numerical Recipes* [#Press1986]_, the sign of the exponent in the ``numpy.fft`` DFT (:math:`-2 \pi \imath \, n k / N`) is different from the sign of the exponent in the *Numerical Recipes* DFT (:math:`+2 \pi \imath \, n k / N`).  

In the following tutorials we define a correlation function and power spectrum based on the Fourier transform conventions of equations :eq:`eq:FT` and :eq:`eq:IFT`.  The results of the tutorials can be summarized as follows.


**Cantilever Thermomechanical Fluctuations**.  We characterize a microcantilever by its resonance frequency :math:`f_0 \: [\mathrm{Hz}]`, ringdown time :math:`\tau_0 \: [\mathrm{s}]`, and frictional coefficient :math:`\Gamma \: [\mathrm{N} \mathrm{s} \mathrm{m}^{-1}]`.  The cantilever experiences a stochastic force arising from its interaction with the environment that gives rise to thermal fluctuations in cantilever position.  In the first tutorial we show that, for a microcantilever in thermal equilibrium at temperature :math:`T`, the resulting power spectrum of these thermal fluctuations in cantilever position is given by

.. math::
    :label: Eq:Pdzf
    
    P_{\delta z}(f) =  \frac{k_b T \tau_0^2}{\Gamma}
        \frac{1}{(\pi \tau_0)^4 (f_0^2 - f^2)^2 + (\pi \tau_0)^2 f^2}

with  :math:`k_b` Boltzmann's constant and :math:`T` the temperature.  Assuming that the cantilever's temperature is known, we can fit the observed power spectrum of position fluctuations to equation :eq:`Eq:Pdzf` to obtain :math:`f_0`, :math:`\tau_0`, and :math:`\Gamma`.  In terms of the quantities in equation :eq:`Eq:Pdzf`, the cantilever spring constant and quality factor are computed as :math:`k = 2 \pi^2 f_0^2 \tau_0 \Gamma \: [\mathrm{N} \: \mathrm{m}^{-1}]` and :math:`Q = \pi f_0 \tau_0 \: [\mathrm{unitless}]`, respectively. 

**Cantilever Frequency Noise**.  Both thermomechanical position fluctuations and detector noise contribute to the noise observed in the cantilever frequency determined using the algorithm described in the Introduction.  In the second tutorial we show that these two noise sources give rise to apparent fluctuations in cantilever frequency whose power spectrum is given by 

.. math::
    :label: Eq:Pdff

    P_{\delta f}(f) = \frac{1}{x_{\mathrm{rms}}^2} 
    \left( 
        \frac{1}{4 \pi^2} \frac{k_b T}{\Gamma} \frac{1}{(\pi \tau_0 f_0^2)^2}
        + f^2 P_{\delta x}^{\mathrm{det}}
    \right)

with :math:`x_{\mathrm{rms}}` the root-mean-square amplitude of the driven cantilever, :math:`P_{\delta x}^{\mathrm{det}} \: [\mathrm{m}^2 \: \mathrm{Hz}^{-1}]` the power spectrum of detector noise written as an equivalent position fluctuation.   In writing equation :eq:`Eq:Pdff`, we have assumed for simplicity that :math:`P_{\delta x}^{\mathrm{det}}(f)` is independent of frequency in the vicinity of the cantilever resonance at :math:`f = f_0`.

**References**

.. [#numpy.fft] *Discrete Fourier Transform* (``numpy.fft``).  http://docs.scipy.org/doc/numpy/reference/routines.fft.html

.. [#Press1986] Press, W. H.; Flannery, B. P.; Teukolsky, S. A. & Vetterling, W. T. Numerical Recipes, The Art of Scientific Computing.  Cambridge University Press, New York (1986).  The current edition (3rd edition; 2007) is available online through http://www.nr.com/.


.. NOTES
.. =====
..
.. with  20080223-Marohn-Group_Report-Frequency_Noise_Tutorial-ver1 
..  = fnt.tex 
.. pandoc --output=fnt.rst --from=latex --to=rst fnt.tex
.. the conversion generated no errors
.. copy the contents of fnt.rst below and manually change === to --- etc
.. delete \color{Blue} everywhere
.. add the :label: Eq:xxx role everywhere we want numbered equation
.. can not have underscores in equation labels
.. refer to equations inline using :eq:`Eq:xxx`

.. with 20080223-Marohn-Group_Report-Frequency_Noise_Tutorial-ver1.tex 
..  = hobm.tex
.. pandoc --output=hobm.rst --from=latex --to=rst hobm.tex
.. the conversion generated no errors
.. then hand-edit as indicated above
.. copy the contents of hobm.rst below and hand edit as follows
.. replace all the unit macros: \sec with {\mathrm{s}} and etc
.. add back in the section headings manually
.. add reference labels for the sections manually
.. edit out the macros involving \ensuremath 
.. remove \tiny and \small
.. remove \lefteqn
.. remove as many as possible \begin{aligned} since we have a wider page here
.. grep search for \[eq:(\w+)\]
..  and replace with :eq:`eq:\1`
.. grep search eq.  and replace with equation 

.. upper document uses equation lables eq:xxx, the lower document Eq:xxx
.. look for :eq:`Eq and add the work equation before each reference

.. \begin{align} does not work well, but \begin{split} does.