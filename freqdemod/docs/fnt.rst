Detection of Instantaneous Phase
================================

The cantilever signal is

.. math:: \boxed{x(t) = \sqrt{2} \: x_{\text{rms}} \cos{(\omega_0 t + \phi)} + \delta x(t)} \label{Eq:x}

where :math:`x_{\text{rms}}` is the cantilever root mean square
amplitude, :math:`\omega_0` is the cantilever frequency, and
:math:`\phi` is the cantilever phase. Here :math:`\delta x(t)` is random
noise which includes contributions from cantilever thermomechanical
fluctuations as well as detector noise.

In order to detect the cantilever frequency we create a quadrature
signal by taking the Hilbert transform of the cantilever signal. This
procedure gives

.. math:: y(t) = \sqrt{2} \: x_{\text{rms}} \sin{(\omega_0 t + \phi)} + \delta y(t) \label{Eq:y}

where :math:`\delta y(t)` is the Hilbert transform of
:math:`\delta x(t)`. An expression for :math:`\delta y(t)` can be
written down, but it is not instructive. There is a simple relation,
however, between :math:`y` and :math:`x` in the Fourier domain:

.. math:: \widehat{\delta y}(f) = H(f) \: \widehat{\delta x}(f)

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

.. math:: \phi(t) = \arctan{(\frac{y(t)}{x(t)})} \label{Eq:phi_def}

Substituting Eqs. [Eq:x] and [Eq:y] into Eq.[Eq:phi\ :sub:`d`\ ef],

.. math::

   \phi(t) = \arctan{(\frac{\sqrt{2} \: x_{\text{rms}} \sin{(\omega_0 t + \phi)} + \delta y(t)}
    {\sqrt{2} \: x_{\text{rms}} \cos{(\omega_0 t + \phi)} + \delta x(t)})}

Let us now, with the help of Mathematica, expand :math:`\phi(t)` in a
Taylor series to first order in *both* :math:`\delta y(t)` and
:math:`\delta x(t)`. The result is

.. math::

   \begin{gathered}
   \phi(t) \approx \phi + \omega_0 t
   - \frac{\delta x(t)}{\sqrt{2} \: x_{\text{rms}}} \sin{(\omega_0 t + \phi)} \\
   + \frac{\delta y(t)}{\sqrt{2} \: x_{\text{rms}}} \cos{(\omega_0 t + \phi)}\end{gathered}

We can extract the instantaneous frequency as the slope of the
:math:`\phi(t)` versus :math:`t` line. After subtracting away the
best-fit line, we are left with phase noise

.. math:: \delta \phi(t) = \phi(t) - \omega_0 t - \phi

given by

.. math::

   \begin{gathered}
   \color{Blue} \delta \phi(t) = - \frac{\delta x(t)}{\sqrt{2} \: x_{\text{rms}}} \sin{(\omega_0 t + \phi)} \\
   \color{Blue} + \frac{\delta y(t)}{\sqrt{2} \: x_{\text{rms}}} \cos{(\omega_0 t + \phi)}
   \label{Eq:deltaphi}\end{gathered}

Phase Noise Power Spectrum
==========================

Taking the Fourier transform of :math:`\delta \phi(t)`, and switching
frequency units

.. math::

   \begin{gathered}
   \widehat{\delta \phi}(f) = \frac{1}{\sqrt{2} \: x_{\text{rms}}}
   \int_{-\infty}^{+\infty} dt \: e^{j \: 2 \pi f t} (- \delta x(t)) \\
   \frac{1}{2 j} \left( e^{j \: 2 \pi f_0 t} e^{j \: \phi} - e^{-j \: 2 \pi f_0 t} e^{-j \: \phi} \right) \\
   + \frac{1}{\sqrt{2} \: x_{\text{rms}}}
   \int_{-\infty}^{+\infty} dt \: e^{j \: 2 \pi f t} (\delta y(t)) \\
   \frac{1}{2} \left( e^{j \: 2 \pi f_0 t} e^{j \: \phi} + e^{-j \: 2 \pi f_0 t} e^{-j \: \phi} \right)\end{gathered}

Which can be simplified to

.. math::

   \begin{gathered}
   \widehat{\delta \phi}(f) = \frac{1}{\sqrt{2} \: x_{\text{rms}}}
   \left( -\frac{e^{j \: \phi}}{2 j} \: \widehat{\delta x}(f+f_0) + \frac{e^{-j \: \phi}}{2 j} \: \widehat{\delta x}(f-f_0) \right. \\
   \left. + \frac{e^{j \: \phi}}{2} \: \widehat{\delta y}(f+f_0) + \frac{e^{-j \: \phi}}{2} \: \widehat{\delta y}(f-f_0) \right) \label{Eq:delta_phi_intermediate}\end{gathered}

We can eliminate :math:`\widehat{\delta y}` from
Eq. [Eq:delta\ :sub:`p`\ hi\ :sub:`i`\ ntermediate] be recognizing

[Eq:delta:sub:`ys`\ imp]

.. math::

   \begin{aligned}
   \widehat{\delta y}(f+f_0) & = \widehat{H}(f+f_0) \: \widehat{\delta x}(f+f_0) \nonumber \\
    & = -\frac{1}{j} \: \widehat{\delta x}(f+f_0) \\
   \widehat{\delta y}(f-f_0) & = \widehat{H}(f-f_0) \: \widehat{\delta x}(f-f_0) \nonumber \\
    & = \frac{1}{j} \: \widehat{\delta x}(f-f_0)\end{aligned}

which holds for frequencies :math:`f \leq f_0`, which is the case here.
Substituting Eqs. [Eq:delta\ :sub:`ys`\ imp] into
Eq. [Eq:delta\ :sub:`p`\ hi\ :sub:`i`\ ntermediate] gives

.. math::

   \begin{gathered}
   \color{Blue} \widehat{\delta \phi}(f) = - \frac{1}{j} \frac{1}{\sqrt{2} \: x_{\text{rms}}} \times \\
   \color{Blue} \left( e^{j \: \phi} \: \widehat{\delta x}(f+f_0) + e^{-j \: \phi} \: \widehat{\delta x}(f-f_0) \right)
   \label{Eq:FTdeltaphi}\end{gathered}

Passing to the power spectrum requires a limiting procedure, as follows.
We should consider that :math:`x(t)` is only sampled for a finite amount
of time :math:`T`, which we can indicate with a subscript:
:math:`x(t) \rightarrow x_{T}(t)` where

.. math::

   x_{T}(t) = \begin{cases}
   0 & \text{for } t > T \\
   x(t) & \text{for } -T \leq t < T \\
   0 & \text{for } t < -T
   \end{cases}
   \label{Eq:xT}

Equation [Eq:deltaphi] holds with
:math:`\delta x \rightarrow \delta x_T`,
:math:`\delta x \rightarrow \delta y_T`, and
:math:`\delta \phi \rightarrow \delta \phi_T`. Time correlation
functions are defined in terms of :math:`x_T(t)`, not :math:`x(t)`,

.. math::

   \begin{gathered}
   C_x(\tau) = \lim_{T \rightarrow \infty} \frac{1}{2 T}
   \int_{-T}^{+T} \langle x(t) \: x(t + \tau) \rangle \: dt \\
   = \lim_{T \rightarrow \infty} \frac{1}{2 T}
   \int_{-\infty}^{+\infty} \langle x_{T}(t) \: x_{T}(t + \tau) \rangle \: dt\end{gathered}

where :math:`\langle \cdots \rangle` indicates a statistical average.
The manipulations leading to Eq. [Eq:FTdeltaphi] are still valid with
the :math:`T`-subscripted variables, with the result that

.. math::

   \begin{gathered}
   \widehat{\delta \phi_{T}}(f) = - \frac{1}{j} \frac{1}{\sqrt{2} \: x_{\text{rms}}} \times \\
   \left( e^{j \: \phi} \: \widehat{\delta x_{T}}(f+f_0) + e^{-j \: \phi} \: \widehat{\delta x_{T}}(f-f_0) \right)
   \label{Eq:FTdeltaphiT}\end{gathered}

The next step to computing the power spectrum is to calculate

.. math::

   \begin{gathered}
   \widehat{\delta \phi_{T}}(f) \: \widehat{\delta \phi_{T}}^{*}\!\!(f) =
    \frac{1}{2 \: x_{\text{rms}}} \times \\
    \left( e^{j \: \phi} \: \widehat{\delta x_{T}}(f+f_0)
     + e^{-j \: \phi} \: \widehat{\delta x_{T}}(f-f_0) \right) \\
    \left( e^{-j \: \phi} \: \widehat{\delta x_{T}}^{*}\!\!(f+f_0)
     + e^{j \: \phi} \: \widehat{\delta x_{T}}^{*}\!\!(f-f_0) \right)
     \label{Eq:PdeltaphiTintermediate}\end{gathered}

We may now pass to the power spectrum by taking the limit

.. math::

   P_{\delta x}(f) = \lim_{T \rightarrow \infty} \frac{1}{2 T} \:
    \widehat{\delta x_{T}}(f) \: \widehat{\delta x_{T}}^{*}\!\!(f)

with the power spectrum :math:`P_{\delta \phi}(f)` analogously defined.
Carrying out this limiting procedure on both sides of
Eq. [Eq:PdeltaphiTintermediate] yields

.. math::

   \begin{gathered}
   P_{\delta \phi}(f) = \frac{1}{2 x_{\text{rms}}^2} \left( P_{\delta x}(f+f_0) + P_{\delta x}(f-f_0) \right) \\
    + \frac{1}{2 x_{\text{rms}}^2} \lim_{T \rightarrow \infty} \frac{1}{2 T} \text{Re} \! \left( \widehat{\delta x_{T}}^{*}\!\!(f-f_0) \: \widehat{\delta x_{T}}(f+f_0) \: e^{j \: 2 \phi} \right)\end{gathered}

where :math:`\text{Re} \! \left( \cdots \right)` indicates taking the
real part. The last term will not survive statistical averaging over the
phase :math:`\phi` since

.. math:: \frac{1}{2 \pi} \int_{0}^{2 \pi} e^{j \: 2 \phi} \: d\phi = 0

Implicit in this average is the assumption that :math:`\phi` is randomly
distributed, that is, there is no correlation between the phase of the
cantilever and the cantilever noise. After statistical averaging over
:math:`\phi`, the power spectrum of cantilever phase noise becomes

.. math::

   \boxed{\color{Blue} P_{\delta \phi}(f) = \frac{1}{2 x_{\text{rms}}^2} \left( P_{\delta x}(f+f_0) + P_{\delta x}(f-f_0) \right)}
   \label{Eq:Pdeltaphi}

Frequency Shift Power Spectrum
==============================

Let us define the instantaneous frequency shift as

.. math:: \delta f(t)= \frac{1}{2 \pi} \frac{d}{d t} \: \delta \phi(t) = \frac{1}{2 \pi} \delta \dot{\phi}

and the compute the power spectrum of the instantaneous frequency shift.
Let us define :math:`\delta f_{T}(t)` as in Eq. [Eq:xT]. The
time-correlation function of the frequency shift is then

.. math::

   C_{\delta f}(\tau) = \lim_{T \rightarrow \infty} \: \frac{1}{2 T}
   \int_{-\infty}^{+\infty} \langle \delta f_{T}(t) \: \delta f_{T}(t+\tau) \rangle \: dt

with :math:`C_{\delta \phi}` defined likewise. Substituting, and
dropping :math:`\langle \cdots \rangle` for notational convenience,

.. math::

   C_{\delta f}(\tau) = \frac{1}{4 \pi^2} \lim_{T \rightarrow \infty} \: \frac{1}{2 T}
   \int_{-\infty}^{+\infty} \langle \delta \dot{\phi}_{T}(t) \: \delta \dot{\phi}_{T}(t+\tau) \rangle \: dt
   \label{Eq:Cdeltaf}

The time derivative :math:`\delta \dot{\phi}` may be computing using its
Fourier transform. With

.. math:: \delta \phi_T(t) = \int_{-\infty}^{+\infty} \widehat{\delta \phi_T}(f) \: e^{-j \: 2 \pi f \: t} \: df

we can compute the time derivative of the instantaneous phase shift as

.. math::

   \delta \dot{\phi}_T(t) = \int_{-\infty}^{+\infty} \widehat{\delta \phi_T}(f) \: (-j \: 2 \pi f) \: e^{-j \: 2 \pi f \: t} \: df
   \label{Eq:deltadotphiT}

If we substitute Eq. [Eq:deltadotphiT] into Eq. [Eq:Cdeltaf] and use

.. math:: \int_{-\infty}^{+\infty} e^{-j \: 2 \pi (f^{\prime}+f^{\prime\prime}) t } dt = \delta(f^{\prime}+f^{\prime\prime}),

where :math:`\delta(t)` is the Kroenecker delta function, then

.. math::

   \begin{gathered}
   C_{\delta f}(\tau) = \int_{-\infty}^{+\infty}
   f^2 \: e^{j \: 2 \pi f \tau} \times \\
   \left\{ \lim_{T \rightarrow \infty} \: \frac{1}{2 T} \: \widehat{\delta \phi_T}(f) \: \widehat{\delta \phi_T}(-f) \right\}
    \: df\end{gathered}

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

   \boxed{\color{Blue} P_{\delta f}(f) =  f^2 \: P_{\delta \phi}(-f)}
   \label{Eq:PdeltafPdeltaphi}

Substituting Eq. [Eq:PdeltafPdeltaphi] into Eq. [Eq:Pdeltaphi] we
conclude

.. math::

   \boxed{\color{Blue} P_{\delta f}(f) =
   \frac{f^2}{2 x_{\text{rms}}^2} \left( P_{\delta x}(f_0+f) + P_{\delta x}(f_0-f) \right)}
   \label{Eq:Pdeltafresult}

where we have used that
:math:`P_{\delta x}(\Omega) = P_{\delta x}(-\Omega)`.

Instrument Noise
================

Equation [Eq:Pdeltafresult] is a general relation between the
position-fluctuation power spectrum and the frequency-fluctuation power
spectrum. The power spectrum of detector noise is typically flat:

.. math:: P_{\delta x}(f_0+f) = P_{\delta x}(f_0-f) \equiv P_{\delta x}^{\text{det}}

Thus

.. math::

   \boxed{\color{Blue} P_{\delta f}^{\text{det}}(f) = \frac{f^2 \: P_{\delta x}^{\text{det}}}{x_{\text{rms}}^2} }
   \label{Eq:PdeltaxDet}

This relation holds whether the power spectra are defined an one-sided
or two-sided, as long as the power spectrum is computed consistently on
both sides of equation. We typically work up data using one-sided power
spectra.

Cantilever Noise
================

We have previously shown that the (one sided) power spectrum of
cantilever position fluctuation is

.. math:: P_{\delta x}^{\text{one}}(f) = \frac{2 k_B T}{\pi k Q f_0} \frac{f_0^4}{(f_0^2 - f^2)^2 + f^2 f_0^2 / Q^2}

where :math:`T` is temperature, :math:`k_B` is Boltzmann’s constant, and
:math:`f_0`, :math:`k`, and :math:`Q` are cantilever frequency, spring
constant, and mechanical quality factor, respectively. We can see that,
for frequencies :math:`f \gg f_0 / Q`

.. math:: P_{\delta x}^{\text{one}}(f_0 \pm f) \approx  \frac{2 k_B T}{\pi k Q f_0} \times \frac{f_0^2}{4 f^2}

Substituting this result into Eq. [Eq:Pdeltafresult] gives

.. math:: P_{\delta x}^{\text{therm}}(f) = \frac{k_B T f_0}{2 \pi \: x_{\text{rms}}^2 k Q}

Using

.. math:: Q = \pi f_0 \tau_0,

where :math:`\tau_0` is the cantilever ringdown time, we can rewrite the
one-sided power spectrum of cantilever frequency fluctuations as

.. math::

   \boxed{\color{Blue} P_{\delta x}^{\text{therm}}(f) = \frac{k_B T}{2 \pi^2 \: x_{\text{rms}}^2 k \: \tau_0} }
   \label{Eq:PdeltaxTherm}

Discussion
==========

Equations. [Eq:PdeltaxDet] and [Eq:PdeltaxTherm] agree *exactly* with
what Loring and Obukhov et al. have derived.
