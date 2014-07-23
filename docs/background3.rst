Practical Details
=================

**Fourier Transform and Units**.   We will analyze our signal using the discrete Fourier Transform (DFT) ``numpy.fft`` summarized in :ref:`Conventions`.  We will display the Fourier transformed data, however, as if it had been obtained by a continuous Fourier Transform (FT).  The outputs of the FT integral and the DFT sum are proportional but not equal.  We can see this immediately by units analysis:  for data :math:`a_n` (and :math:`a(t)`) having units of meters, the discrete Fourier transform :math:`A_k` has units of :math:`\text{m}` while the continuous Fourier transform :math:`\hat{a}(f)` has units of :math:`\text{m} \: \text{Hz}^{-1}`.  The FT is obtained from the DFT as follows.

Consider the continuous Fourier transform

.. math::
    
    \hat{a}(f) = \int_{-\infty}^{+\infty} dt \: 
        a(t) \: e^{-2 \pi \imath f t } 

We can convert this integral to a sum using the following correspondences.  With :math:`\Delta t` the time per point and :math:`N` the total number of points,

.. math::

    \begin{align}
    t & \rightarrow t_n = n \: \Delta t \\
    f & \rightarrow f_k = k /(N \: \Delta t) \\
    a(t) & \rightarrow a(n \: \Delta t) = a_n \\
    \hat{a}(f) & \rightarrow \hat{a}(f_k)
    \end{align}

and 

.. math::

        \int_{-\infty}^{+\infty} \cdots dt 
            \rightarrow \Delta t \: \sum_{n = 0}^{N-1} \cdots

Substituting, we find

.. math::

    \hat{a}(f_k) = \Delta t \:  \underbrace{\sum_{n = 0}^{N-1} A_k 
        \: e^{-2 \pi \imath \, n k / N}}_{A_k}

We conclude that the continuous Fourier transform is obtained from the discrete Fourier transform using

.. math::
    :label: eq:hatak

    \boxed{
        \hat{a}(f_k) = \Delta t \: A_k \: 
            \sim \: [\dfrac{\text{m}}{\text{Hz}}]   
    }

where in writing the units we have assumed that :math:`a` has units of :math:`\text{m}`.

**Power Spectrum and Units**.  To connect the continuous-frequency power spectrum to the discrete-frequency power spectrum let us, for simplicity's sake,  consider the *two-sided* power spectrum.  In the continuous FT, the two-sided power spectrum is defined as

.. math::

    P_{a}^{\text{two}}(f) 
    = \lim_{T \rightarrow \infty} \dfrac{1}{T} | {\hat{a}}_{T}(f) |^2

where, as before, :math:`{\hat{a}}_{T}` is the Fourier transform of a segment of :math:`a(t)` data recorded for a total time :math:`T`.  Substituting :math:`P_{a}(f) \rightarrow  P_{a}(f_k)`, :math:`T  \rightarrow N \: \Delta t`, and :math:`{\hat{a}}_{T} \rightarrow \Delta t \: A_k` we have that

.. math::
    :label: eq:Patwo

    \boxed{
        P_{a}^{\text{two}}(f_k) = \dfrac{\Delta t}{N}| A_k |^2 \:
            \sim \: [\dfrac{\text{m}^2}{\text{Hz}}]
    }

Let us confirm that this is the right definition of the power spectrum by showing that the area under this power spectrum is indeed equal to the mean-square value of :math:`a(t)`.  In the continuous FT case, we have Parseval's theorem:

.. math::
    :label: eq:Par

    a_{\text{rms}}^2 
    = \lim_{T \rightarrow \infty} \frac{1}{T} \int_{0}^{T} a(t)^2 dt
    = \int_{-\infty}^{+\infty} P_{a}^{\text{two}}(f) \: df   

The discrete FT version of this equality is obtained as follows:  

.. math::

     a_{\text{rms}}^2
     = \frac{1}{N \: \Delta t} \Delta t \sum_{n = 0}^{N-1} a_n^{*} a_n 
     = \frac{1}{N} \sum_{n = 0}^{N-1} a_n^{*} a_n,  
     
where we have substituted :math:`a_n = a_n^{*}`; this substitution is valid since :math:`a(t)` is real.  Expanding :math:`a_n` and :math:`a_n^{*}` in terms of their Fourier series, we obtain an expression for the mean-square value in terms of a sum over the Fourier coefficients:

.. math::
    :label: eq:ams1

    a_{\text{rms}}^2 
    = \frac{1}{N^3} \sum_{k = 0}^{N-1} \sum_{k^\prime = 0}^{N-1}
        A_k A_{k^\prime}^{*} 
    \underbrace{\sum_{n = 0}^{N-1} e^{\, 2 \pi \imath (k - k^\prime) n/N}}_{N \, \delta_{k,k^\prime}}
    = \frac{1}{N^2} \sum_{k = 0}^{N-1} | A_k |^2

Converting the integral in equation :eq:`eq:Par` into a sum, we obtain an equivalent expression for the mean-square value 

.. math::
    :label: eq:ams2

    a_{\text{rms}}^2 = \int_{-\infty}^{+\infty} P_{a}(f) \: df
     = \underbrace{\sum_{k = 0}^{N-1} \frac{1}{N \: \Delta t}}_{\int \cdots df} 
      \underbrace{\frac{\Delta t}{N}| A_k |^2}_{P_{a}^{\text{two}}(f)}
     = \frac{1}{N^2} \sum_{k = 0}^{N-1} | A_k |^2

That equations :eq:`eq:ams1` and  :eq:`eq:ams2` are equal gives us confidence that :eq:`eq:Patwo` is indeed the correct expression for obtaining the continuous-FT power spectrum from the DFT coefficients.  

**Hilbert Transform**.  In :ref:`FreqNoise`, we defined a function :math:`H` that implemented the Hilbert transform in Fourier space:

.. math::

    H(f)\: \widehat{\delta x}(f) = \widehat{\delta y}(f).
    
The function was given as

.. math::

   H(f) = \begin{cases}
   +\imath & \text{if } f < 0 \\
   0 & \text{if } f = 0 \\
   -\imath & \text{if} f > 0
   \end{cases}

In the following code, we compute the Hilbert transform by a different route.  
Consider the function

.. math::

    {\delta z}(t) = {\delta x}(t) + \imath \: {\delta y}(t).

The measured data is the real part of :math:`{\delta z}` while the Hilbert transform of the data is contained in the imaginary part of :math:`{\delta z}`.  
How can we obtain :math:`\delta z` from :math:`\delta x}`?  The required function can be inferred by considering

.. math::

    \widehat{\delta z}(f) 
    = \widehat{\delta x}(f) + \imath \: \widehat{\delta y}(f)     
    = \underbrace{(1 + \imath \: H(f))}_{\equiv Hc(f)} \: \widehat{\delta x}(f)

The function we want is thus

.. math::

   Hc(f) = \begin{cases}
   0 & \text{if } f < 0 \\
   1 & \text{if } f = 0 \\
   2 & \text{if} f > 0
   \end{cases}

So defined,

.. math::

    Hc(f)\: \widehat{\delta x}(f) = \widehat{\delta z}(f).

For lack of a better term, we'll call :math:`Hc` the complex Hilbert transform.

**Analysis of Thermomechanical Motion**.  We will fit the power spectrum of cantilever position fluctuation to the function

.. math::
    :label: Pdzfit1

    P_{\delta z}^{\text{therm}}(f) 
    =  \dfrac{k_b T \tau_0^2}{\Gamma} 
        \dfrac{1}{(\pi \tau_0)^4(f_0^2 - f^2)^2 + (\pi \tau_0)^2 f^2}

To avoid numerical-precision problems in the curve-fitting algorithm, it is important that the dependent variable :math:`P_{\delta z}^{\text{therm}}`, the independent variable :math:`f`, and the fit parameters :math:`\Gamma`, :math:`f_0`, and :math:`\tau_0` all be of order unity.  In non-linear least-squares fitting, this order-unity condition is usually achieved by carefully choosing units for the quantities of interest.

We can easily arrange for the independent variable to be of order unity by working with frequency in units of kilohertz, :math:`f \sim [\text{kHz}]`.  The last term in equation :eq:`Pdzfit1` is unitless as long as :math:`\tau_0` and :math:`f_0`, and :math:`f` have complimentary units. This suggests working with the resonance frequency in units of kilohertz, :math:`f_0 \sim [\text{kHz}]`, and the ringdown time in units of milliseconds, :math:`\tau_0 \sim [\text{ms}]`.   We can arrange for the dependent variable to be of order unity by working with the cantilever position :math:`x(t)` in units of nanometers; this will give the dependent variable units of :math:`P_{\delta z}^{\text{therm}} \sim [\text{nm}^2 \: \text{Hz}^{-1}]`.  It remains to discuss :math:`\Gamma`, the dissipation constant.
 
.. cross referencing: http://sphinx-doc.org/markup/inline.html