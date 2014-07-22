Microcantilever Frequency Noise
-------------------------------

**Detection of Instantaneous Phase**.  The cantilever signal is

.. math:: 
    :label: Eq:x

    \boxed{x(t) = \sqrt{2} \: x_{\text{rms}} \cos{(\omega_0 t + \phi)} +
     \delta x(t)}

where :math:`x_{\text{rms}}` is the cantilever root mean square amplitude, :math:`\omega_0` is the cantilever frequency, and :math:`\phi` is the cantilever phase. Here :math:`\delta x(t)` is random noise which includes contributions from cantilever thermomechanical fluctuations as well as detector noise.

In order to detect the cantilever frequency we create a quadrature
signal by taking the Hilbert transform of the cantilever signal. This
procedure gives

.. math:: 
    :label: Eq:y
    
    y(t) = \sqrt{2} \: x_{\text{rms}} \sin{(\omega_0 t + \phi)} 
    + \delta y(t)

where :math:`\delta y(t)` is the Hilbert transform of
:math:`\delta x(t)`. An expression for :math:`\delta y(t)` can be
written down, but it is not instructive. There is a simple relation,
however, between :math:`y` and :math:`x` in the Fourier domain:

.. math:: 

    \widehat{\delta y}(f) = H(f) \: \widehat{\delta x}(f)

where :math:`\widehat{\delta x}(f)` indicates the Fourier transform of
:math:`\delta x(t)`. The function :math:`H` implements the Hilbert
transform in Fourier space:

.. math::

   H(f) = \begin{cases}
   +j & \text{if } f < 0 \\
   0 & \text{if } f = 0 \\
   -j & \text{if} f > 0
   \end{cases}

Since :math:`H(f) H^{*}(f) = 1` (except for the single point at
:math:`f=0`), it follows that :math:`\delta y(t)` has essentially the
same power spectrum as :math:`\delta x(t)`.

In our frequency-detection algorithm we measure the instantaneous phase
of the cantilever using

.. math:: 
    :label: Eq:phidef

    \phi(t) = \arctan{(\frac{y(t)}{x(t)})}

Substituting equations :eq:`Eq:x` and :eq:`Eq:y` into equation :eq:`Eq:phidef`,

.. math::

   \phi(t) = \arctan{(\frac{\sqrt{2} \: x_{\text{rms}} \sin{(\omega_0 t + \phi)} + \delta y(t)}{\sqrt{2} \: x_{\text{rms}} \cos{(\omega_0 t + \phi)} + \delta x(t)})}

Let us now, with the help of Mathematica, expand :math:`\phi(t)` in a
Taylor series to first order in *both* :math:`\delta y(t)` and
:math:`\delta x(t)`. The result is

.. math::

   \phi(t) \approx \phi + \omega_0 t
    - \frac{\delta x(t)}{\sqrt{2} \: x_{\text{rms}}} \sin{(\omega_0 t + \phi)}
    + \frac{\delta y(t)}{\sqrt{2} \: x_{\text{rms}}} \cos{(\omega_0 t + \phi)}

We can extract the instantaneous frequency as the slope of the
:math:`\phi(t)` versus :math:`t` line. After subtracting away the
best-fit line, we are left with phase noise

.. math:: \delta \phi(t) = \phi(t) - \omega_0 t - \phi

given by

.. math:: 
    :label: Eq:dphi
    
    \delta \phi(t) = 
    - \frac{\delta x(t)}{\sqrt{2} \: x_{\text{rms}}} \sin{(\omega_0 t + \phi)}
    + \frac{\delta y(t)}{\sqrt{2} \: x_{\text{rms}}} \cos{(\omega_0 t + \phi)}

Phase Noise Power Spectrum
--------------------------

Taking the Fourier transform of :math:`\delta \phi(t)`, and switching
frequency units

.. math::

    \begin{gathered}
    \widehat{\delta \phi}(f) = \frac{1}{\sqrt{2} \: x_{\text{rms}}}
    \int_{-\infty}^{+\infty} dt \: e^{j \: 2 \pi f t} (- \delta x(t))
    \frac{1}{2 j} \left( e^{j \: 2 \pi f_0 t} e^{j \: \phi} 
                        - e^{-j \: 2 \pi f_0 t} e^{-j \: \phi} \right)
    \\
    + \frac{1}{\sqrt{2} \: x_{\text{rms}}}
    \int_{-\infty}^{+\infty} dt \: e^{j \: 2 \pi f t} (\delta y(t))
    \frac{1}{2} \left( e^{j \: 2 \pi f_0 t} e^{j \: \phi} 
                    + e^{-j \: 2 \pi f_0 t} e^{-j \: \phi} \right)
    \end{gathered}

Which can be simplified to

.. math:: 
    :label: Eq:deltaphiintermediate
    
    \begin{gathered}
    \widehat{\delta \phi}(f) = \frac{1}{\sqrt{2} \: x_{\text{rms}}}
    \left( -\frac{e^{j \: \phi}}{2 j} \: \widehat{\delta x}(f+f_0) + \frac{e^{-j \: \phi}}{2 j} \: \widehat{\delta x}(f-f_0) \right. \\
    \left. + \frac{e^{j \: \phi}}{2} \: \widehat{\delta y}(f+f_0) + \frac{e^{-j \: \phi}}{2} \: \widehat{\delta y}(f-f_0) \right)
    \end{gathered}

We can eliminate :math:`\widehat{\delta y}` from equation 
:eq:`Eq:deltaphiintermediate` by recognizing

.. math::
    :label: Eq:deltaysimp1

    \widehat{\delta y}(f+f_0)
        = \widehat{H}(f+f_0) \: \widehat{\delta x}(f+f_0) 
        = -\frac{1}{j} \: \widehat{\delta x}(f+f_0)
        
.. math::
    :label: Eq:deltaysimp2        
        
    \widehat{\delta y}(f-f_0) 
        = \widehat{H}(f-f_0) \: \widehat{\delta x}(f-f_0) 
        = \frac{1}{j} \: \widehat{\delta x}(f-f_0)

which holds for frequencies :math:`f \leq f_0`, which is the case here.
Substituting equations :eq:`Eq:deltaysimp1` and :eq:`Eq:deltaysimp2` into 
equation :eq:`Eq:deltaphiintermediate` gives

.. math::
    :label: Eq:FTdeltaphi
    
    \widehat{\delta \phi}(f) = 
        - \frac{1}{j} \frac{1}{\sqrt{2} \: x_{\text{rms}}} 
        \left( e^{j \: \phi} \: \widehat{\delta x}(f+f_0) + e^{-j \: \phi} \:
            \widehat{\delta x}(f-f_0) \right)

Passing to the power spectrum requires a limiting procedure, as follows.
We should consider that :math:`x(t)` is only sampled for a finite amount
of time :math:`T`, which we can indicate with a subscript:
:math:`x(t) \rightarrow x_{T}(t)` where

.. math::
    :label: Eq:xT
    
    x_{T}(t) = \begin{cases}
    0 & \text{for } t < 0 \\
    x(t) & \text{for } 0 \leq t \leq T \\
    0 & \text{for } T < t
    \end{cases}

Equation :eq:`Eq:dphi` holds with
:math:`\delta x \rightarrow \delta x_T`,
:math:`\delta x \rightarrow \delta y_T`, and
:math:`\delta \phi \rightarrow \delta \phi_T`. Time correlation
functions are defined in terms of :math:`x_T(t)`, not :math:`x(t)`,

.. math::

   \begin{split}
   C_x(\tau) 
   & = \lim_{T \rightarrow \infty} \frac{1}{T}
   \int_{0}^{T} \langle x(t) \: x(t + \tau) \rangle \: dt \\
   & = \lim_{T \rightarrow \infty} \frac{1}{T}
   \int_{-\infty}^{+\infty} \langle x_{T}(t) \: x_{T}(t + \tau) \rangle \: dt
   \end{split}

where :math:`\langle \cdots \rangle` indicates a statistical average.
The manipulations leading to equation :eq:`Eq:FTdeltaphi` are still valid with
the :math:`T`-subscripted variables, with the result that

.. math:: 
    :label: Eq:FTdeltaphiT
    
    \widehat{\delta \phi_{T}}(f) = 
    - \frac{1}{j} \frac{1}{\sqrt{2} \: x_{\text{rms}}} 
        \left( e^{j \: \phi} \: \widehat{\delta x_{T}}(f+f_0) + e^{-j \: \phi} 
            \: \widehat{\delta x_{T}}(f-f_0) \right)

The next step to computing the power spectrum is to calculate

.. math::
    :label: Eq:PdeltaphiTintermediate

    \widehat{\delta \phi_{T}}(f) \: \widehat{\delta \phi_{T}}^{*}\!\!(f) =
    \frac{1}{2 \: x_{\text{rms}}} 
    \left( e^{j \: \phi} \: \widehat{\delta x_{T}}(f+f_0)
     + e^{-j \: \phi} \: \widehat{\delta x_{T}}(f-f_0) \right)
     
    \left( e^{-j \: \phi} \: \widehat{\delta x_{T}}^{*}\!\!(f+f_0)
     + e^{j \: \phi} \: \widehat{\delta x_{T}}^{*}\!\!(f-f_0) \right)

We may now pass to the power spectrum by taking the limit

.. math::

    P_{\delta x}(f) = \lim_{T \rightarrow \infty} \frac{1}{T} \:
    \widehat{\delta x_{T}}(f) \: \widehat{\delta x_{T}}^{*}\!\!(f)

with the power spectrum :math:`P_{\delta \phi}(f)` analogously defined.
Carrying out this limiting procedure on both sides of
equation :eq:`Eq:PdeltaphiTintermediate` yields

.. math::

    P_{\delta \phi}(f) 
    = \frac{1}{2 x_{\text{rms}}^2} 
        \left( P_{\delta x}(f+f_0) + P_{\delta x}(f-f_0) \right)
    - \frac{1}{2 x_{\text{rms}}^2} \lim_{T \rightarrow \infty} \frac{1}{T}
      \text{Re} \! \left( \widehat{\delta x_{T}}^{*}\!\!(f-f_0) \:
                        \widehat{\delta x_{T}}(f+f_0) \: e^{j \: 2 \phi} \right)

where :math:`\text{Re} \! \left( \cdots \right)` indicates taking the
real part. The last term will not survive statistical averaging over the
phase :math:`\phi` since

.. math:: \frac{1}{2 \pi} \int_{0}^{2 \pi} e^{j \: 2 \phi} \: d\phi = 0

Implicit in this average is the assumption that :math:`\phi` is randomly
distributed, that is, there is no correlation between the phase of the
cantilever and the cantilever noise. After statistical averaging over
:math:`\phi`, the power spectrum of cantilever phase noise becomes

.. math::
    :label: Eq:Pdeltaphi

    \boxed{P_{\delta \phi}(f) = 
    \dfrac{1}{2 x_{\text{rms}}^2} 
        \left( P_{\delta x}(f+f_0) + P_{\delta x}(f-f_0) \right)}

Frequency Shift Power Spectrum
------------------------------

Let us define the instantaneous frequency shift as

.. math:: \delta f(t)= \frac{1}{2 \pi} \frac{d}{d t} \: \delta \phi(t) = \frac{1}{2 \pi} \delta \dot{\phi}

and the compute the power spectrum of the instantaneous frequency shift.
Let us define :math:`\delta f_{T}(t)` as in equation :eq:`Eq:xT`. The
time-correlation function of the frequency shift is then

.. math::

   C_{\delta f}(\tau) = \lim_{T \rightarrow \infty} \: \frac{1}{T}
   \int_{-\infty}^{+\infty} \langle \delta f_{T}(t) \: \delta f_{T}(t+\tau) \rangle \: dt

with :math:`C_{\delta \phi}` defined likewise. Substituting, and
dropping :math:`\langle \cdots \rangle` for notational convenience,

.. math::
    :label: Eq:Cdeltaf

    C_{\delta f}(\tau) = 
    \frac{1}{4 \pi^2} \lim_{T \rightarrow \infty} \: \frac{1}{T}
    \int_{-\infty}^{+\infty} \langle \delta \dot{\phi}_{T}(t) 
    \: \delta \dot{\phi}_{T}(t+\tau) \rangle \: dt

The time derivative :math:`\delta \dot{\phi}` may be computing using its
Fourier transform. With

.. math:: \delta \phi_T(t) = \int_{-\infty}^{+\infty} \widehat{\delta \phi_T}(f) \: e^{-j \: 2 \pi f \: t} \: df

we can compute the time derivative of the instantaneous phase shift as

.. math::
    :label: Eq:deltadotphiT

    \delta \dot{\phi}_T(t) = \int_{-\infty}^{+\infty} \widehat{\delta \phi_T}(f) \: (-j \: 2 \pi f) \: e^{-j \: 2 \pi f \: t} \: df

If we substitute equation :eq:`Eq:deltadotphiT` into equation :eq:`Eq:Cdeltaf` 
and use

.. math:: \int_{-\infty}^{+\infty} e^{-j \: 2 \pi (f^{\prime}+f^{\prime\prime}) t } dt = \delta(f^{\prime}+f^{\prime\prime}),

where :math:`\delta(t)` is the Kroenecker delta function, then

.. math::

    C_{\delta f}(\tau) = \int_{-\infty}^{+\infty}
    f^2 \: e^{j \: 2 \pi f \tau} 
    \left\{
        \lim_{T \rightarrow \infty} 
        \: \frac{1}{2 T} \: \widehat{\delta \phi_T}(f) 
        \: \widehat{\delta \phi_T}(-f) 
    \right\} \: df

where we have passed the limit into the integral. Because
:math:`\delta \phi_T(t)` is a real function,
:math:`\widehat{\delta \phi_T}(-f) = \widehat{\delta \phi_T}^{*}\!\!(f)`.
The term in braces is thus :math:`P_{\delta \phi}(f)`, the power
spectrum of phase fluctuations. We find

.. math:: C_{\delta f}(\tau) = \int_{-\infty}^{+\infty} f^2 \: P_{\delta \phi}(f) \: e^{j \: 2 \pi f \tau} \: df

Comparing this to the usual relation between the correlation function
and the power spectrum

.. math:: C_{\delta f}(\tau) = \int_{-\infty}^{+\infty} P_{\delta f}(f) \: e^{-j \: 2 \pi f \tau} \: df,

we see that

.. math::
    :label: Eq:PdeltafPdeltaphi
    
    \boxed{P_{\delta f}(f) =  f^2 \: P_{\delta \phi}(-f)}

Substituting equation :eq:`Eq:PdeltafPdeltaphi` into equation :eq:`Eq:Pdeltaphi` 
we conclude

.. math::
    :label: Eq:Pdeltafresult
    
    \boxed{P_{\delta f}(f) =
    \dfrac{f^2}{2 x_{\text{rms}}^2}
    \left( P_{\delta x}(f_0+f) + P_{\delta x}(f_0-f) \right)}

where we have used that
:math:`P_{\delta x}(\Omega) = P_{\delta x}(-\Omega)`.

Instrument Noise
----------------

Equation :eq:`Eq:Pdeltafresult` is a general relation between the
position-fluctuation power spectrum and the frequency-fluctuation power
spectrum. The power spectrum of detector noise is typically flat:

.. math:: P_{\delta x}(f_0+f) = P_{\delta x}(f_0-f) \equiv P_{\delta x}^{\text{det}}

Thus

.. math::
    :label: Eq:PdeltaxDet

    \boxed{P_{\delta f}^{\text{det}}(f) = \dfrac{f^2 \: P_{\delta x}^{\text{det}}}{x_{\text{rms}}^2} }

This relation holds whether the power spectra are defined as one-sided
or two-sided, as long as the power spectrum is computed consistently on
both sides of equation. We typically work up data using one-sided power
spectra.

Cantilever Noise
----------------

We have previously shown that the (one sided) power spectrum of
cantilever position fluctuation is

.. math::

    P_{\delta x}^{\text{one}}(f) 
    = \frac{2 k_B T}{\pi k Q f_0} 
    \frac{f_0^4}{(f_0^2 - f^2)^2 + f^2 f_0^2 / Q^2}

where :math:`T` is temperature, :math:`k_B` is Boltzmann’s constant, and
:math:`f_0`, :math:`k`, and :math:`Q` are cantilever frequency, spring
constant, and mechanical quality factor, respectively. We can see that,
for frequencies :math:`f \gg f_0 / Q`

.. math:: 

    P_{\delta x}^{\text{one}}(f_0 \pm f) 
    \approx  \frac{2 k_B T}{\pi k Q f_0} \times \frac{f_0^2}{4 f^2}

Substituting this result into equation :eq:`Eq:Pdeltafresult` gives

.. math::

    P_{\delta f}^{\text{therm}}(f) 
    = \frac{k_B T f_0}{2 \pi \: x_{\text{rms}}^2 k Q}

Using

.. math:: Q = \pi f_0 \tau_0,

where :math:`\tau_0` is the cantilever ringdown time, we can rewrite the
one-sided power spectrum of cantilever frequency fluctuations as

.. math::
    :label: Eq:PdeltaxTherm
    
    \boxed{P_{\delta f}^{\text{therm}}(f) = \dfrac{k_B T}{2 \pi^2 \: x_{\text{rms}}^2 k \: \tau_0} }

Discussion
----------

Equations :eq:`Eq:PdeltaxDet` and :eq:`Eq:PdeltaxTherm` agree *exactly* with
what Loring and co-workers have derived [#Yazdanian2008jun]_.

References
----------

.. [#Yazdanian2008jun] Yazdanian, S. M.; Marohn, J. A. & Loring, R. F. Dielectric Fluctuations in Force Microscopy: Noncontact Friction and Frequency Jitter. *J. Chem. Phys.*,  **2008**, *128*: 224706 [http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2674627/] [http://dx.doi.org/10.1063/1.2932254] .  See equations 6.7 through 6.9.