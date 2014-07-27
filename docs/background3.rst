.. notes: cross referencing: http://sphinx-doc.org/markup/inline.html

Practical Details
=================

**Fourier Transform and Units**.   We will analyze our signal using the discrete Fourier Transform (DFT).  We will display the Fourier transformed data, however, as if it had been obtained by a continuous Fourier Transform (FT).  The outputs of the FT integral and the DFT sum are proportional but not equal.  We can see this immediately by units analysis:  for data :math:`a_n` (and :math:`a(t)`) having units of meters, the discrete Fourier transform :math:`A_k` has units of :math:`\text{m}` while the continuous Fourier transform :math:`\hat{a}(f)` has units of :math:`\text{m} \: \text{Hz}^{-1}`.  

The FT data is obtained from the DFT data as follows.  Consider the continuous Fourier transform

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

where in writing the units we have assumed that :math:`a` has units of :math:`\text{m}`.  If :math:`a` has units of :math:`\text{nm}`, then :math:`\hat{a}(f_k)` will have units of :math:`\text{nm} \: \text{Hz}^{-1}`.

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

That equations :eq:`eq:ams1` and  :eq:`eq:ams2` are equal gives us confidence that :eq:`eq:Patwo` is indeed the correct expression for obtaining the continuous-FT power spectrum from the DFT array elements.  

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
How can we obtain :math:`\delta z` from :math:`\delta x`?  The required function can be inferred by considering

.. math::

    \widehat{\delta z}(f) 
    = \widehat{\delta x}(f) + \imath \: \widehat{\delta y}(f)     
    = \underbrace{(1 + \imath \: H(f))}_{\equiv \text{Hc}(f)} \: 
        \widehat{\delta x}(f)

The function we want is thus

.. math::

   \text{Hc}(f) = \begin{cases}
   0 & \text{if } f < 0 \\
   1 & \text{if } f = 0 \\
   2 & \text{if} f > 0
   \end{cases}

So defined,

.. math::

    \text{Hc}(f)\: \widehat{\delta x}(f) = \widehat{\delta z}(f).

For lack of a better term, we'll call :math:`\text{Hc}` the complex Hilbert transform.

**Analysis of Thermomechanical Position Fluctuations**.  We will fit the power spectrum of cantilever position fluctuations to the function

.. math::
    :label: Pdzfit1

    P_{\delta z}^{\text{therm}}(f) 
    =  \dfrac{k_b T \tau_0^2}{\Gamma} 
        \dfrac{1}{(\pi \tau_0)^4(f_0^2 - f^2)^2 + (\pi \tau_0)^2 f^2}

using non-linear least-squares fitting.  To avoid numerical-precision problems in the  curve fitting algorithm, it is important for the fit's :math:`y` axis (:math:`P_{\delta z}^{\text{therm}}`), :math:`x` axis (:math:`f`), and parameters (:math:`\Gamma`, :math:`\tau_0`, and :math:`f_0`) to be within a few orders of magnitude of 1.  There are two ways to achieve this condition: (1) apply a scale factor to the :math:`x` and :math:`y` axis data so the scaled data ranges from 0 to 1, or (2) carefully choose units for all the quantities of interest.  We will take the second approach.

Working with frequency in units of kilohertz will make the fit's :math:`x` axis data be order unity: :math:`f \sim [\text{kHz}]`.  To make the :math:`y` axis data of order unity, we will work with the cantilever position :math:`x(t)` in units of nanometers, so that :math:`P_{\delta z}^{\text{therm}} \sim [\text{nm}^2 \: \text{Hz}^{-1}]`. 

Now for the fit parameters. The second term in equation :eq:`Pdzfit1` is unitless as long as :math:`\tau_0`, :math:`f_0`, and :math:`f` have complimentary units.  We will therefore work with the resonance frequency in units of kilohertz and the ringdown time in units of milliseconds: :math:`f_0 \sim [\text{kHz}]` and :math:`\tau_0 \sim [\text{ms}]`.  Most microcantilevers have a dissipation constant within a few orders of magnitude of :math:`1 \times 10^{-12} \: \text{N} \: \text{s} \: \text{m}^{-1}`.  We will therefore choose this as the unit of dissipation constant, :math:`\Gamma \sim [\text{pN} \: \text{s} \: \text{m}^{-1}]`:

For purposes of curve fitting, let us define unitless, barred versions of the variables of interest:

.. math::

    \begin{align}
    \overline{f} & = f / \text{kHz} \\
    {\overline{P}}_{\! \delta z}^{\, \text{therm}} & 
        = P_{\delta z}^{\text{therm}} / (\text{nm}^2 \: \text{Hz}^{-1}) \\
    \overline{\Gamma} & = \Gamma /(\text{pN} \: \text{s} \: \text{m}^{-1}) \\
    \overline{\tau}_{0} & = \tau / \text{ms} \\
    \overline{f}_0 & = f_0 / \text{kHz}
    \end{align}
   
We will represent the temperature in units of kelvin as :math:`\overline{T} = T / \text{K}`. The prefactor in equation :eq:`Pdzfit1` is in mixed units and needs to be simplified:

.. math::

    \begin{align}
    \dfrac{k_b T \tau_0^2}{\Gamma}
    & = \frac{
            1.3806 \times 10^{-23} \: \text{N} \: \text{m} \: \text{K}^{-1} 
            \overline{T} \: \text{K} \: 
            \overline{\tau}_0^{\, 2} \: \text{ms}^{2} 
        }
        {
            \overline{\Gamma} \: \text{pN} \: \text{s} \: \text{m}^{-1}
        }
    \\
    & = 13.806 \frac{
            \overline{T} \: \overline{\tau}_{0}^{\, 2}}
        {
             \overline{\Gamma} 
        } 
        \: \frac{\text{nm}^2}{\text{Hz}}
    \end{align}
    
We will thus fit to

.. note: with the \overline(f) and \overline{f)_0 variables, the superscripts
.. note: are getting put too high.  Manually adjust them lower.

.. math::

    \boxed{
    {\overline{P}}_{\! \delta z}^{\, \text{therm}}(\overline{f})
    = 13.808 \dfrac{\overline{T} \: \overline{\tau}_0^{\, 2}}{\overline{\Gamma}}
    \dfrac{1}{
            (\pi \overline{\tau}_0)^4
                ((\overline{f}_0)^2 - (\overline{f})^2)^2 
            + (\pi \overline{\tau}_0)^2 (\overline{f})^2
        }
    }
     
with the temperature :math:`\overline{T}` given.  To this equation we will add two terms to account for detector noise.  The first term is a constant, the frequency-indepenendent part of the power spectrum of detector noise.  The second term accounts for the frequency-dependent part of the noise floor; the constant in this term corresponds to the first coefficient in a Taylor expansion of the detector noise power spectrum about :math:`f = f_0`.  Putting both thermomechanical and detector noise terms together, we will fit the observed power spectrum of cantilever position fluctuations to  

.. math::

    \boxed{
    {\overline{P}}_{\! \delta z}(\overline{f})
     = {\overline{P}}_{\! \delta z}^{\, \text{therm}}(\overline{f})
     + {\overline{P}}_{\! \delta z}^{\, \text{det}} 
     + 1000 \: \overline{p}_1 (\overline{f} - \overline{f}_0)
    }

with :math:`{\overline{P}}_{\! \delta z}^{\, \text{det}}` the detector noise power spectrum in units of :math:`\text{nm}^2 \: \text{Hz}^{-1}` and :math:`\overline{p}_1` the Taylor-series coefficient in units of :math:`\text{nm}^2 \: \text{Hz}^{-2}`.  The factor of 1000 in the above equation results from a :math:`\text{kHz}` to :math:`\text{Hz]` units conversion. 

The power spectrum of force fluctuations, which determines cantilever force sensitivity, is easily expressed in terms of the unitless parameters.  In practical units,

.. math::

    \boxed{
        P_{\delta F} 
        = 4 k_b T \: \Gamma 
        = 55.232 \: \overline{T} \: \overline{\Gamma} \:
            \dfrac{\text{aN}^2}{\text{Hz}} 
    }
