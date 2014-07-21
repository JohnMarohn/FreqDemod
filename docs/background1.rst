Oscillator Thermomechanical Fluctuations
========================================

This tutorial discusses the steady-state response of a cantilever to both
a coherent and an incoherent driving force. The cantilever is modeled
classically as a damped harmonic oscillator.  


This tutorial is organized as
follows.

In :ref:`sect:equation-of-motion` the equation of motion for a damped
harmonic oscillator is summarized. When a *coherent* force is driving the
oscillator, the solution of the equation of motion is greatly simplified
by recasting the equation in terms of a complex variable whose real and
imaginary parts track the in-phase and out-of-phase response, respectively. 
This recasting is done in section :ref:`sect:phasors`. The steady-state response 
of a damped harmonic oscillator is derived in
:ref:`sect:steady-state-response-I`.

Understanding the response of a damped oscillator to an *incoherent*
driving force is greatly simplified by thinking in terms of correlation
functions, introduced below in :ref:`sect:correlation-functions`. In this 
section we establish a link between the time-domain correlation function and the
frequency-domain power spectrum.  A slightly more sophisticated correlation
function then is introduced that is more suitable for understanding physical
phenomena.

The steady-state-response of a damped harmonic oscillator to an
incoherent is derived in :ref:`sect:steady-state-response-II`. The
solution relates the power spectrum of the response to the power
spectrum of the incoherent force.  The soluton is examined in the limit where
the incoherent driving force has a flat frequency content. In
:ref:`sect:analyzing-data` the fitting of a cantilever power-spectrum is
discussed.

In the case where the incoherent driving force represents the oscillator
in thermal contact with a bath of modes at a definite temperature, the
form of the force can be derived using the equipartition theorem of
statistical mechanics. This is accomplished in
:ref:`sect:equipartition-theorem`, where it is also shown that if oscillator
temperature is known, then from the area under the cantilever power
spectrum the cantilever spring constant can be determined.

In :ref:`sect:minimum-detectable-force`, it is shown that the thus
derived thermomechanical cantilever fluctuations limit the minimum
applied force that can be detected by measuring cantilever displacement.
Designing an experiment to achieve the smallest possible detectable
force is discussed. In :ref:`sect:cantilever-design` a scaling
analysis is done to show the dependence of the minimum detectable force
on cantilever parameters such as length, width, and thickness.

.. _sect:equation-of-motion:

Equation of Motion
------------------

The equation of motion for a **damped harmonic oscillator** is

.. math::
    :label: eq:HO
    
    m \: \ddot{x} + \alpha \: \dot{x} + k \: x = F

The variables are

.. math::

   \begin{array}{lll}
    x & \mbox{oscillator position} & [\mathrm{meter}] \\ 
    m & \mbox{mass} & [\mathrm{kilogram}] \\
    \alpha & \mbox{friction parameter} & [\mathrm{kilogram} \: {\mathrm{second}}^{-1} = \mathrm{newton} \: \mathrm{second} \: {\mathrm{meter}}^{-1}] \\
    k & \mbox{spring constant} & [\mathrm{newton} \: {\mathrm{meter}}^{-1}] \\
    F & \mbox{applied force} & [\mathrm{newton}]
   \end{array}

It is useful to rewrite this equation in a more canonical form. Divide
equation :eq:`eq:HO` by :math:`m`, and define new variables according to the
following equations.

.. math:: \frac{\alpha}{m} = \frac{\omega_0}{Q}, \: \: \frac{k}{m} = \omega_0^2, \: \mbox{and} \: \frac{F}{m} = \frac{\omega_0^2 F}{k} = A

The new variables are

.. math::

   \begin{array}{lll}
    \omega_0 &\mbox{resonance frequency} & [\mathrm{rad} \: {\mathrm{second}}^{-1}] \\
    Q & \mbox{quality factor} & [\mbox{unitless}] \\
    A & \mbox{applied force amplitude} & [\mathrm{meter} \: {\mathrm{second}}^{-2}]
   \end{array}

The canonical equation of motion for a classical harmonic oscillator is
thus

.. math::
    :label: eq:HO-canonical

    \ddot{x} + \frac{\omega_0}{Q} \: \dot{x} + \omega_0^2 \: x 
        = A = \frac{\omega_0^2 \: F}{k}

.. _sect:phasors:

Phasors
-------

We wish to calculate the response of the oscillator to a resonant force,

.. math:: F(t) \propto \cos{\omega t}

Here :math:`\omega` is the driving frequency, close to but not
necessarily equal to :math:`\omega_0`. At *steady state*, the cantilever
response must also be periodic, of the general form

.. math:: x(t) = x_c \cos{\omega t} + x_s \sin{\omega t}

We wish to solve for :math:`x_c` and :math:`x_s` as a function of
driving frequency. It is convenient to introduce a complex number
:math:`z` that tracks cantilever displacement,
:math:`x = \mathrm{Re}(z)`. If we make the ansatz that
:math:`z = z_0 \exp{(\imath \: \omega t)}` then

.. math::
    
    \begin{split}
    x(t) 
    & = \mathrm{Re} \{ z \} \\
    &  = \mathrm{Re} \{ z_0 \: e^{\imath \: \omega t} \} \\
    & = \underbrace{\mathrm{Re} \{ z_0 \} }_{x_c} \cos{\omega t}
        - \underbrace{\mathrm{Im} \{ z_0 \} }_{x_s} \sin{\omega t}
    \end{split}

If we can recast equation :eq:`eq:HO-canonical` in terms of the complex variable
:math:`z` then we can reduce the problem of solving for two real
variables, :math:`x_c` and :math:`x_s`, to solving for one complex
variable, :math:`z_0`.

Towards this end, we introduce another complex variable :math:`F_c`
which tracks the applied force. If the force is a sinusoidal function of
time, then :math:`F_c = F_0 \exp{(\imath \: \omega t)}` where
:math:`F_0 = | F_0 | \: \exp{(\imath \: \phi)}` is complex number that 
describes the magnitude and phase of the harmonic driving force:

.. math::

    \begin{split}
    F(t)
    & = \mathrm{Re}\{ F_c \} \\
    & = \mathrm{Re} \{ F_0 \: e^{\imath \: \omega t} \} \\
    & = \mathrm{Re} \{ F_0 \} \cos{\omega t} 
        - \mathrm{Im} \{ F_0 \} \sin{\omega t} \\
    & = | F_0 | \cos{(\omega t + \phi)}
    \end{split}

The equation of motion for :math:`z` in terms of **phasors** is

.. math::
    :label: eq:z
    
    \ddot{z} + \frac{\omega_0}{Q} \: \dot{z} + \omega_0^2 \: z 
    = \frac{\omega_0^2 \: F_c}{k}


.. _sect:steady-state-response-I: 


Steady State Response I
-----------------------

It is convenient to work with frequency in experimental units of
:math:`[\mathrm{cyc}/{\mathrm{s}}] = [{\mathrm{Hz}}]` instead of
:math:`[\mathrm{rad}/{\mathrm{s}}]`. Therefore we’ll define

.. math:: f_0 = \frac{\omega_0}{2 \pi} \: \sim \: [\frac{\mathrm{cyc}}{{\mathrm{s}}}] = [{\mathrm{Hz}}]

and work throughout with frequencies in :math:`{\mathrm{Hz}}`.

In this section we explore the response of the harmonic oscillator to a
**coherent sinusoidal driving force**. Substitute :math:`F_c = F_0
\exp{(\imath \: 2 \pi f t)}` into equation :eq:`eq:z` and assume that the
response :math:`z` is of the form
:math:`z_0 \exp{(\imath \: 2 \pi f t)}`:

.. math::

    (-f^2 + \imath f \: \frac{f_0}{Q} + f_0^2 ) 
        \: z_0 \: e^{\imath \: 2 \pi f t} 
    = \frac{f_0^2}{k} F_0 \: e^{\imath \: 2 \pi f t}

where we have canceled a factor of :math:`4 \pi^2` from every term. We
infer that

.. math:: 

    z_0 = \frac{F_0}{k} \: \frac{f_0^2}{f_0^2 - f^2 + \imath \: f \: f_0 / Q}

so that at steady state

.. math::

    \begin{split}
    z(f) 
    & = z_0 \: e^{\imath \: 2 \pi f t} \\
    & = \frac{F_0 \: e^{\imath \: 2 \pi f t}}{k} \: 
        \frac{f_0^2}{f_0^2 - f^2 + \imath \: f \: f_0 / Q}
    \end{split}

It is useful to write :math:`z` as follows:

.. math::

    z(f) = \frac{| F_0 |}{k} \left( \frac{f_0^2 (f_0^2 - f^2)}{(f_0^2 - f^2)^2 + f^2 \: f_0^2 / Q^2} - \imath \: \frac{f \: f_0^3 / Q}{(f_0^2 - f^2)^2 + f^2 \: f_0^2 / Q^2} \right) \: e^{\imath \: ( 2 \pi f t + \phi)}

Using :math:`x = \mathrm{Re} \{ z \}` we can infer that
:math:`x(t)` is of the form

.. math::

    x(t) = x_c \: \cos{(2 \pi f t + \phi)} + x_s \: \sin{(2 \pi f t + \phi)}

where

.. math::

    x_c(f)
    = \frac{| F_0 |}{k} \frac{f_0^2 ( f_0^2 - f^2)}
            {(f_0^2 - f^2)^2 + f^2 \: f_0^2 / Q^2}

.. math::

    x_s(f)
    = \frac{| F_0 |}{k}
    \frac{f \: f_0^3 / Q}
        {(f_0^2 - f^2)^2 + f^2 \: f_0^2 / Q^2}

The signal :math:`x_c` is the part of the response detected with a
lock-in as *in phase* with the driving force. The signal :math:`x_s` is
the *out of phase* part of the response.

When the applied force drives the oscillator right on resonance,
:math:`\omega = \omega_0`, and we compute that

.. math::
    
    \begin{split}
    x_s(\omega_0) & =0 \\
    x_s(\omega_0) & =\frac{Q \: | F_0 |}{k}
    \end{split}

This is to be compared to the steady-state response to a non-oscillating
(DC) force

.. math::

    \begin{split}
    x_c(0) & = \frac{| F_0 |}{k} \\
    x_s(0) & = 0
    \end{split}

We conclude that the response to a resonant force is :math:`Q` times
larger than the response to a static DC force. The response at resonance
is also ninety degrees out of phase with the applied oscillating force.
We can see this immediately from

.. math:: z_0(\omega_0) = - \imath \: \frac{Q \: F_0}{k}


.. _sect:correlation-functions:

Correlation Functions
---------------------

The section explores a connection between a function’s correlation function and its power spectrum. The correlation function of :math:`x(t)` is defined as

.. math:: 
    :label: eq:Cx

    C_x(\tau) = \int_{-\infty}^{\infty} dt \: x(t) \: x(t+\tau) \: 
        \sim \: [\frac{{\mathrm{m}}^2}{{\mathrm{Hz}}}]

Following the Fourier Transform conventions in *Numerical Recipes*
[#Press1986]_, the Fourier and inverse Fourier transforms of
:math:`x(t)` are:

.. math:: 

    \hat{x}(f) = \int_{-\infty}^{\infty} dt \: x(t) \: e^{\imath \: 2 \pi f t}

.. math:: 

    x(t) = \int_{-\infty}^{\infty} df \: \hat{x}(f) \: e^{-\imath \: 2 \pi f t}

Substitute for :math:`x(t)` and :math:`x(t+\tau)` the appropriate
Fourier transform relation

.. math::

    C_x(\tau) = \int df  \int df^{\prime}  \: \hat{x}(f^{\prime}) \: \hat{x}(f) \: e^{-\imath \: 2 \pi f \tau} \underbrace{\int dt \: e^{-\imath \: 2 \pi f t}  e^{-\imath \: 2 \pi f^{\prime} t}}_{\delta(f+f^{\prime}) \Longrightarrow f^{\prime} = -f}

The integral over time involving exponentials reduces to a delta
function. Only frequencies :math:`f^{\prime} = -f` contribute to the
final double integral, so that

.. math:: C_x(\tau) = \int_{-\infty}^{\infty} df \: \: \hat{x}(-f) \: \hat{x}(f) \: e^{-\imath \: 2 \pi f \tau}

If :math:`x(t)` is a real function of time, then it can be shown that
:math:`\hat{x}(-f) = \hat{x}^{*}(f)` where the star indicates the
complex conjugate. We have finally

.. math::
    
    \begin{split}
    C_x(\tau) 
    & = \int_{-\infty}^{\infty} df \: 
        \hat{x}^{*}(f) \: \hat{x}(f) \: e^{-\imath \: 2 \pi f \tau} \\ 
    & = \int_{-\infty}^{\infty} df \: 
        | \hat{x}(f) |^2 \: e^{-\imath \: 2 \pi f \tau}
    \end{split}

If we define the one-sided power spectral density as

.. math:: 

    \hat{P}_x(f) 
    = | \hat{x}(f) |^2 + | \hat{x}(-f) |^2  \: 
    \sim \: [\frac{{\mathrm{m}}^2}{{\mathrm{Hz}}^2}]

then

.. math:: 
    :label: eq:Cxresult

    C_x(\tau)
    = \int_{0}^{\infty} df \: \hat{P}_x(f) \: e^{-\imath \: 2 \pi f \tau}

This is an important result: The correlation function and the power spectrum are Fourier transform pairs.  

While equations :eq:`eq:Cx` and :eq:`eq:Cxresult` can in principle be used to
analyze thermomechanical fluctuations in the position of a microcantilever, in
practice we need to introduce a modified correlation function to analyze the
fluctuations.  The reason for this can be seen by considering the correlation
function of equation :eq:`eq:Cx` at :math:`\tau = 0`:

.. math::

    C_x(0) = \int_{-\infty}^{\infty} dt \: x(t)^2 \longrightarrow \infty

As indicated, this integral will diverge if applied to a real-world laboratory
signal such as a cantilever oscillation. Following Weissbluth
[#Weissbluth1989]_, let's define a more physically-relevant correlation
function as follows.

.. math:: G(\tau) \equiv \langle x(t) x(t+\tau) \rangle

.. math::
    :label: eq:CF
    
    G(\tau) \equiv \lim_{T \rightarrow \infty} \: \frac{1}{T} \int_{0}^{T} x(t) x(t+\tau) \: dt \: \sim \: [{\mathrm{m}}^2]

The units of this correlation function are :math:`[{\mathrm{m}}^2]`, if the
units of x are :math:`[{\mathrm{m}}]`. This correlation function is quite
different from the mathematically-defined correlation function
:math:`C(\tau)` of equation :eq:`eq:Cx` whose units are
:math:`[{\mathrm{m}}^2/{\mathrm{Hz}}]`.  The correlation function at
:math:`\tau=0`, zero delay, has special significance:

.. math:: 

    \begin{split}
    G(0) 
    & = \lim_{T \rightarrow \infty} \: \frac{1}{T} \int_{0}^{T} x^2(t) \: dt 
    & = x_{\mathrm{rms}}^2
    \end{split}

We see that :math:`G(0)` is the mean square value of :math:`x(t)` and
therefore the root-mean-square is :math:`x_{\mathrm{rms}} = \sqrt{G(0)}`.

We will now reproduce Weissbluth’s treatment relating the
(physically-relevant) correlation function :math:`G(\tau)` to an
analogous power spectrum.  Following Weissbluth, let us define the function
:math:`x_{T}(t)` which is equal to :math:`x(t)` on the time interval
:math:`(0,T)` and is zero at all other times:

.. math:: 

    x_{T}(t) = 
    \left\{
        \begin{array}{cc} x(t) & 0 \leq t \leq T \\ 
        0 & \mathrm{otherwise} 
        \end{array}
    \right.

Let us define correlation function for :math:`x_T` as follows:

.. math::

    \begin{split}
    G_{T}(\tau) 
    & = \frac{1}{T} \int_{0}^{T} x_T(t) x_T(t+\tau) \: dt \\
    & = \frac{1}{T} \int_{-\infty}^{+\infty} x_T(t) x_T(t+\tau) \: dt
    \end{split}

Since we’ve confined :math:`x_T` to the time interval :math:`(0,T)` we
can extend the limits in integration out to infinity. Now take the
Fourier transform of :math:`G_{T}(\tau)`:

.. math::

    \begin{multline}
    \int_{-\infty}^{+\infty} G_{T}(\tau) 
        \: e^{\imath \: 2 \pi f \tau} \: d\tau\
    = \frac{1}{T} \int_{-\infty}^{+\infty} d\tau \: 
        e^{\imath \: 2 \pi f \tau} \int_{-\infty}^{+\infty} dt
            \: x_{T}(t) \: x_{T}(t+\tau) \\
    = \frac{1}{T} \int_{-\infty}^{+\infty} dt 
            \: x_{T}(t) \: e^{-\imath \: 2 \pi f t} 
        \int_{-\infty}^{+\infty} d\tau \:  
            x_{T}(t+\tau) \: e^{\imath \: 2 \pi f (t+\tau)}
   \end{multline}

where we have inserted :math:`1 = \exp{(-\imath \: 2 \pi f t)}
\exp{(+\imath \: 2 \pi f t)}`. In the second integral, change the
variable of integration to :math:`t^{\prime} = t+\tau`. This lets us
write

.. math::

    \int_{-\infty}^{+\infty} G_{T}(\tau) 
        \: e^{\imath \: 2 \pi f \tau} \: d\tau
    = \frac{1}{T} \underbrace{\int_{-\infty}^{+\infty} dt \: x_{T}(t) \:
        e^{-\imath \: 2 \pi f t}}_{{\hat{x}}_T(-f) = {\hat{x}}^{*}_{T}(f)} \underbrace{\int_{-\infty}^{+\infty} dt^{\prime} \: x_{T}(t^{\prime}) \: e^{\imath \: 2 \pi f t^{\prime}}}_{{\hat{x}}_T(f)}

Since :math:`x(t)` is a real function, it follows that
:math:`{\hat{x}}_{T}(-f) = {\hat{x}}^{*}_{T}(f)`. We can thus write

.. math::
    :label: eq:limitG

    \int_{-\infty}^{+\infty} G_{T}(\tau) \: e^{\imath \: 2 \pi f \tau} \: d\tau 
        = \frac{1}{T} \: | {\hat{x}}_{T}(f) |^{2}

We recover the “real” correlation function by a limiting procedure.

.. math:: 

    G(\tau) = \lim_{T \rightarrow \infty} \: G_{T}(\tau)

Take the limit on each side of equation :eq:`eq:limitG` as :math:`T \rightarrow
\infty`. On the left-hand side, :math:`G_T` becomes :math:`G`; the terms on the
right-hand side motivate us to define

.. math::
    :label: eq:PS
    
    J(f) \equiv \lim_{T \rightarrow \infty} \: 
    \frac{1}{T} \: | {\hat{x}}_{T}(f) |^{2} \: 
        \sim \: [\frac{{\mathrm{m}}^2}{{\mathrm{Hz}}}]

as the *physically relevant spectral density*. It still holds that

.. math::

    J(f) 
    = \int_{-\infty}^{+\infty} G(\tau) \: e^{\imath \: 2 \pi f \tau} \: d\tau

and

.. math::
    :label: eq:FTOSPS
    
    \begin{split}
    G(\tau) 
        & = \int_{-\infty}^{+\infty} 
            J(f) \: e^{-\imath \: 2 \pi f \tau} \: df \\
        & = \int_{0}^{+\infty} 
            P(f) \: e^{-\imath \: 2 \pi f \tau} \: df.
    \end{split}

We have defined the one-sided power spectral density as

.. math::
    :label: eq:OSPS
    
    \begin{split}
    P(f)
    & = J(f) + J(-f) \\
    & = \lim_{T \rightarrow \infty} \frac{1}{T} \: 
        ( | {\hat{x}}_{T}(f) |^{2} + | {\hat{x}}_{T}(-f) |^{2})
    \end{split}

With these definitions of correlation function (equation :eq:`eq:CF`) and
spectral density (equation :eq:`eq:PS`), we still have that the correlation
function :math:`G(\tau)` and the power spectrum :math:`J(f)` of :math:`x(t)` are
Fourier transform pairs.

Finally, equation :eq:`eq:FTOSPS` can be used to calculate the root-mean-square
of :math:`x(t)` given a measured one-sided power spectral density:

.. math::
    :label: eq:xrmsP
    
    \begin{split}
    x_{\mathrm{rms}}^2 
        & = \langle x^2(t) \rangle \\
        & = G(0) = \int_{0}^{+\infty} P(f) \: df.
    \end{split}

We conclude that the area under the one-sided spectrum is the mean-square
displacement.  We note that this connection is *not* valid for the mathematically-defined power-spectrum of the last section.

.. _sect:steady-state-response-II:



Steady State Response II
------------------------

In this section we explore the response of the harmonic oscillator to an
**incoherent** driving force. If the force is random, it will have zero
average:

.. math:: 

    \langle F(t) \rangle 
    = \lim_{T \rightarrow \infty} \: \frac{1}{T} \int_{0}^{T} F(t) \: dt
        \longrightarrow 0

It will not, in general, have a vanishing correlation function – we will
discuss the force and response using correlation functions. Integrating
equation :eq:`eq:z` provides another route to understanding the response
:math:`z(t)` to a randomly fluctuating force :math:`F(t)` driving the
system; we will not follow such a Langevin treatment.

Define correlation functions for :math:`z` and :math:`F` as above,

.. math::

    G_z(\tau) 
    \equiv \lim_{T \rightarrow \infty} \: 
        \frac{1}{T} \int_{0}^{T} z(t) z(t+\tau) \: dt \: 
        \sim \: [{\mathrm{m}}^2]

.. math::

    G_F(\tau) 
    \equiv \lim_{T \rightarrow \infty} \: 
        \frac{1}{T} \int_{0}^{T} F(t) F(t+\tau) \: dt \: 
        \sim \: [{\mathrm{N}}^2]

With each of these correlation functions is associated a power spectrum:

.. math::

   \begin{aligned}
   G_z(\tau) \Leftarrow \mathrm{FT} \Rightarrow J_z(f) \: \mbox{or} \: P_z(f) \\
   G_F(\tau) \Leftarrow \mathrm{FT} \Rightarrow J_F(f) \: \mbox{or} \: P_z(f)
   \end{aligned}

Because :math:`z` and :math:`F` are connected by an equation of motion,
we can write :math:`J_z` in terms of :math:`J_F`, as we will now show.

Follow the motion by Fourier analysis:

.. math::
    :label: eq:FTF
    
    F(t) = \int_{-\infty}^{\infty} df \: \hat{F}(f) \: e^{-\imath \: 2 \pi f t}
    
.. math::
    :label: eq:FTz

    z(t) = \int_{-\infty}^{\infty} df \: \hat{z}(f) \: e^{-\imath \: 2 \pi f t}

Substitute equations :eq:`eq:FTF` and :eq:`eq:FTz` into the equation of motion
connecting :math:`F` and :math:`z`, equation :eq:`eq:z`.

.. math::

    \int_{-\infty}^{+\infty} (-f^2 - \imath f \: \frac{f_0}{Q} + f_0^2 ) \: \hat{z}(f) \: e^{-\imath \: 2 \pi f t} \: df = \int_{-\infty}^{+\infty} \frac{f_0^2}{k} \hat{F}(f) \: e^{-\imath \: 2 \pi f t} \: df

For both sides to be equal, we must have that at each frequency

.. math:: 

    \hat{z}(f) 
    = \frac{\hat{F}(f)}{k} \frac{f_0^2}{f_0^2 - f^2 - \imath f \: f_0 / Q}

Taking the magnitude of each side, we infer that the power spectra are
related by

.. math:: 

    | \hat{z}(f) |^2 
    = \frac{| \hat{F}(f) |^2}{k^2} 
        \frac{f_0^4}{(f_0^2 - f^2)^2 + f^2 f_0^2 / Q^2}

This equation relates “mathematical” correlation functions. It is a
straightforward matter to introduce the time-averaging and limiting
procedure employed above to obtain this result in terms of
“physically-relevant” correlation functions:

.. math::

    P_z(f) 
    = \lim_{T \rightarrow \infty} \frac{1}{T} 
        \: ( | {\hat{z}}_{T}(f) |^{2} + | {\hat{z}}_{T}(-f) |^{2}) \: 
            \sim \: [\frac{{\mathrm{m}}^2}{{\mathrm{Hz}}}]

.. math::
    :label: eq:PF

    P_F(f) 
    = \lim_{T \rightarrow \infty} \frac{1}{T} 
        \: ( | {\hat{F}}_{T}(f) |^{2} + | {\hat{F}}_{T}(-f) |^{2}) \: 
            \sim \: [\frac{{\mathrm{N}}^2}{{\mathrm{Hz}}}]

The result, which we write in terms of *one-sided power spectral
densities* is:

.. math::
    :label: eq:PzPF
    
    P_z(f) = 
    \frac{P_F(f)}{k^2}
    \frac{f_0^4}{(f_0^2 - f^2)^2 + f^2 f_0^2 / Q^2}

Given an :math:`F(t)`, form a one-sided power spectrum :math:`P_F(f)` by
Fourier transforming the time-domain spectrum of :math:`F` and averaging
(equation :eq:`eq:PF`). We can then predict the resulting one-sided power
spectrum :math:`P_z(f)` of the response :math:`z(t)` using
equation :eq:`eq:PzPF`. Finally, if we wish, we could determine what would be 
the time-correlation function :math:`G_z(\tau)` of :math:`z(t)`.

We can proceed no further in discussing the response of the harmonic
oscillator to an incoherent driving force unless we specify a form for
either :math:`F(t)`, :math:`G_F(\tau)`, :math:`J_F(f)`, or the power
spectrum :math:`P_F(f)`. The simplest approximation is to assume that
the force fluctuation driving the oscillator is well-described as being
*white noise*, e.g., a randomly-fluctuating with a power spectrum that
is flat up to some very high frequency cutoff:

.. math::
    :label: eq:whitenoise
    
    P_F(f) 
    = \left\{ 
        \begin{array}{cc} 
            P_F(0) & 0 \leq f \leq f_m \\ 
            0 & f_m \leq f 
        \end{array} 
    \right.

The cutoff frequency’s numerical value is determined by the physical
process giving rise to the force fluctuation. Atomic force microscope
cantilevers experience force fluctuations due to random collisions with
gas molecules and fluctuating cantilever phonon populations, for
example. Both of these processes have characteristic timescales on the
order of nanoseconds, which implies (by Fourier transform of the
associated correlation function) that
:math:`f_m \sim 1 / {\mathrm{ns}} = \mathrm{GHz}`.

Atomic force cantilever resonance frequencies are in the range of
:math:`f_0
\sim 1 - 500 \: \mathrm{kHz}`, so that :math:`f_0 << f_m`, and thus when
considering a cantilever’s response to the above-mentioned force
fluctuations the approximation of equation :eq:`eq:whitenoise` is a good one. An
example of a case where the white-noise approximation would not be valid
is the cantilever being driven by acoustic room vibrations. The power
spectrum of doors closing, mechanical vibrations from transformers, and
people walking by the cantilever is generally not flat near the
cantilever resonance frequency.

If the cantilever is being driven by white noise, then

.. math::
    :label: eq:PzPFconst
    
    P_z(f) = 
    \underbrace{\frac{P_F(0)}{k^2}}_{\mathrm{\small freq. independent}} 
    \underbrace{\frac{f_0^4}{(f_0^2 - f^2)^2 + f^2 f_0^2 / Q^2}}_{\mathrm{\small freq. dependent}}

.. _sect:analyzing-data:

Analyzing Data
--------------

As a practical matter, the the position fluctuation is fit to:

.. math::
    :label: eq:Pzfit
    
    P_z(f) 
    = P_z(0) \underbrace{\frac{f_0^4}{(f_0^2 - f^2)^2 + f^2 f_0^2 / Q^2}}_{\mathrm{\small unitless}} 
    + P_x^{\mathrm{ noise}}

The first term is the power spectrum of the cantilever, the form of
which we derived above, and the second term represents detector noise.
Here

.. math::
    :label: eq:Pz0
    
    P_z(0) = \frac{P_F(0)}{k^2} \: 
        \sim \: [\frac{{\mathrm{m}}^2}{{\mathrm{Hz}}}]

is the apparent position fluctuation at zero frequency. If the
cantilever and instrument-noise related fluctuations are uncorrelated –
a good assumption – then the power spectrums just add.

Over a narrow bandwidth centered at the cantilever frequency, the
instrument noise power spectrum :math:`P_x^{\mathrm{ noise}}` can
often be approximated as constant. If working with a low-Q cantilever
near zero-frequency, “:math:`1/f`” instrument noise begins to contribute.
In this case, the “:math:`1/f`” component can often be well-approximated
by adding a linear term:

.. math:: P_x^{\mathrm{ noise}} \approx P^{(0)} + P^{(0)} (f - f_0)

Here :math:`P^{(0)} \: \sim \: [{\mathrm{m}}^2/{\mathrm{Hz}}]` is the
frequency-independent term and :math:`P^{(1)} \: \sim \:
[{\mathrm{m}}^2/{\mathrm{Hz}}^2]` approximates frequency-dependent noise sources,
including “:math:`1/f`” circuit noise.

By fitting the observed :math:`P_z(f)` to equation :eq:`eq:Pzfit`, the 
cantilever resonance frequency :math:`f_0` and quality factor :math:`Q` may be
determined. If :math:`k` is known, the force fluctuation power spectral
density can be inferred using equation :eq:`eq:Pz0`. If the force fluctuations
are described by a bath of modes at a well defined *temperature*, then
statistical mechanics constrains what :math:`P_F(0)` *must* be, as will
now be discussed.

.. _sect:equipartition-theorem:

Equipartition Theorem
---------------------

As may be derived using statistical mechanics, a harmonic oscillator in
equilibrium with a bath of temperature :math:`T` has a energy
expectation value for each mode equal to :math:`k_B T/2`. Thus

.. math::
    :label: eq:equip
    
    \frac{1}{2} \: k \langle x^2 \rangle = \frac{1}{2} \: k_B T

where
:math:`k_B = 1.38 \: \times \: {10}^{-23} \: {\mathrm{J}} \: {{\mathrm{K}}}^{-1}`
is Boltzmann’s constant and :math:`T \: [{\mathrm{K}}]` is the absolute
temperature. Here :math:`\langle x^2 \rangle` is mean-square
displacement :math:`x_{\mathrm{rms}}^2`. If the oscillator is in
thermal equilibrium with a bath described by a temperature :math:`T`,
then if :math:`x_{\mathrm{rms}}^2` can be measured, the oscillator
spring constant can be inferred from

.. math::
    :label: eq:k
    
    k = \frac{k_B T}{x_{\mathrm{rms}}^2} \: 
        \sim \: [\frac{{\mathrm{N}}}{{\mathrm{m}}}]

The mean-square displacement can be measured directly from time-domain
observations. An alternative and more accurate way to determine
:math:`x_{\mathrm{rms}}` is to employ equation :eq:`eq:xrmsP`
and calculate :math:`x_{\mathrm{rms}}` as the area
under the position-fluctuation power spectrum. In practice both circuit
noise and cantilever fluctuations contribute to the power spectrum, and
therefore, by equation :eq:`eq:xrmsP`, to the observed time-domain
:math:`x_{\mathrm{rms}}`. Having fit data to
equation :eq:`eq:Pzfit`, the integral of the cantilever’s contribution to the
power spectrum may be calculated analytically in from the fit parameters
as follows (see the appendix):

.. math::
    :label: eq:xrmscalc
    
    \begin{split}
    x_{\mathrm{rms}}^2 
    & = P_z(0) f\: _0^4 \: (\int_{0}^{\infty} df 
        \frac{1}{(f^2 - f_0^2)^2 + f^2 f_0^2 / Q^2}) \\
    & = \frac{\pi}{2} \: P_z (0) \: Q \: f_0
    \end{split}

Having thus employed correlation-function results to accurately
:math:`x_{\mathrm{rms}}`, the spring constant my be
inferred. Substituting equation :eq:`eq:xrmscalc` into equation :eq:`eq:k` gives 
the desired relation

.. math::
    :label: eq:k2
    
    k = \frac{2 \: k_B T}{\pi P_z(0) \: Q \: f_0} \: 
        \sim \: [\frac{{\mathrm{N}}}{{\mathrm{m}}}]

.. _sect:minimum-detectable-force:

Minimum Detectable Force
------------------------

We can turn equation :eq:`eq:k2` around to read

.. math:: 
    :label: eq:Pz0therm

    P_z(0) = \frac{2 \: k_B T}{\pi k Q f_0} \: 
        \sim \: [\frac{{\mathrm{m}}^2}{{\mathrm{Hz}}}]

We conclude from this equation that if the harmonic oscillator is to satisfy the equipartition theorem (equation :eq:`eq:equip`) then:

    A harmonic oscillator in thermal equilibrium at temperature
    :math:`T` must have a  :math:`P_z(0)` given by :eq:`eq:Pz0therm`.

The power spectral density at all frequencies for a
harmonic oscillator at thermal equilibrium is obtained by substituting
this :math:`P_z(0)` into equation :eq:`eq:Pzfit`:

.. math:: 

    P_z(f) =  (\frac{2 \: k_B T}{\pi k Q f_0})(\frac{f_0^4}{(f_0^2 - f^2)^2 + f^2 f_0^2 / Q^2})

The first term in parenthesis has units of :math:`[{\mathrm{m}}^2/{\mathrm{Hz}}]` 
and serves to fix the area under the power spectrum. The second term is
unitless and traces out the response versus frequency of the oscillator
to thermal-bath fluctuations.

We can infer the thermal force-fluctuation spectral density using
:math:`P_F(0) = k^2 P_z(0)`. The answer is

.. math::
    :label: eq:PF0
    
    P_F(0) = \frac{2 \: k \: k_B T}{\pi Q f_0} \: 
        \sim \: [\frac{{\mathrm{N}}^2}{{\mathrm{Hz}}}]

Thermal cantilever position fluctuations can be treated as if due to a
*force* fluctuation of this spectral density.

At resonance

.. math:: P_z(f_0) = (\frac{2 \: k_B T}{\pi k Q f_0})(Q^2) = \frac{2 \: Q \: k_B T}{\pi k f_0} \: \sim \: [\frac{{\mathrm{m}}^2}{{\mathrm{Hz}}}]

We are interested in the position-noise power in a narrow bandwidth
:math:`\Delta \! f` centered at the oscillator resonance frequency
:math:`f_0`, such as would be measured with a lock-in amplifier. 
The noise power is:

.. math::

    \begin{split}
    x_{\mathrm{ min}}^2(f_0) 
    & = \int_{f_0 - \Delta \! f / 2}^{f_0 + \Delta \! f / 2} P_z(f) \: df \\
    & \approx P_z(f_0) \int_{f_0 - \Delta \! f/2}^{f_0 + \Delta \! f/2} df \\
    & = \frac{2 \: Q \: k_B T}{\pi k f_0} \times \Delta \! f \: 
        \sim \: [{\mathrm{m}}^2]
    \end{split}
   
The root-mean-square detectable position at resonance is the square root
of this quantity:

.. math:: x_{\mathrm{ min}}(f_0) = \sqrt{ \frac{2 \: Q \: \Delta \! f \: k_B T}{\pi k f_0} } \: \sim \: [{\mathrm{m}}]

It is interesting to calculate the position-noise power in a narrow
bandwidth centered at *zero* frequency. Calculate:

.. math::

    \begin{split}
    x_{\mathrm{ min}}^2(0)
    & \approx P_z(0) \: \Delta \! f \\
    & = \frac{2 \: k_B T}{\pi k Q f_0} \times \Delta \! f \: 
        \sim \: [{\mathrm{m}}^2]
    \end{split}

As we expect, there is less power in fluctuations far away from
resonance. For completeness, the zero-frequency root-mean-square
detectable position is:

.. math:: 

    x_{\mathrm{ min}}(0) 
    = \sqrt{ \frac{2 \: \Delta \! f \: k_B T}{\pi k Q f_0} } \: 
        \sim \: [{\mathrm{m}}]

The minimum detectable force is inferred from the force-noise power in a
narrow band of frequency near resonance:

.. math::

    \begin{split}
    F_{\mathrm{ min}}^2 
    & = \int_{f_0 - \Delta \! f / 2}^{f_0 + \Delta \! f / 2} P_F(f) \: df \\
    & =  P_F(0) \int_{f_0 - \Delta \! f/2}^{f_0 + \Delta \! f/2} df \\
    & = \frac{2 \: k \: k_B T}{\pi Q f_0} \times \Delta \! f \: 
        \sim \: [{\mathrm{N}}^2]
    \end{split}

where we have taken :math:`P_F(f) = P_F(0)` from equation :eq:`eq:PF0`. The
root-mean-square detectable force is thus:

.. math::
    :label: eq:Fmin
    
    F_{\mathrm{min}} 
    = \sqrt{ \frac{2 \: k \: \Delta \! f \: k_B T}{\pi Q f_0} } \: 
        \sim \: [{\mathrm{N}}]

Note that the :math:`x_{\mathrm{ min}}` calculated above is only
valid near resonance, whereas equation :eq:`eq:Fmin` for
:math:`F_{\mathrm{ min}}` is valid at *all frequencies*.

It is convenient to write :math:`x_{\mathrm{ min}}` in terms of a
position-fluctuation spectral density at resonance
:math:`S_x \sim [{\mathrm{m}}
\: {\mathrm{Hz}}^{-1/2}]` times the square root of the detection bandwidth, as
follows. Similarly :math:`F_{\mathrm{ min}}` can be recast in terms
of a force-fluctuation spectral density
:math:`S_F \sim [{\mathrm{N}} \: {\mathrm{Hz}}^{-1/2}]`.

.. math::

   \begin{aligned}
   x_{\mathrm{min}} = S_x \: \sqrt{\Delta \! f} \\
   F_{\mathrm{min}} = S_F \: \sqrt{\Delta \! f}
   \end{aligned}

Here the position- and force-fluctuation spectral density near resonance
are:

.. math::
    
    S_x = \sqrt{ \frac{2 \: Q \: k_B T}{\pi k f_0} } \: 
        \sim \: [\frac{{\mathrm{m}}}{\sqrt{{\mathrm{Hz}}}}]
        
.. math::
    :label: eq:SF
    
    S_F = \sqrt{ \frac{2 \: k \: k_B T}{\pi Q f_0} } \: 
        \sim \: [\frac{{\mathrm{N}}}{\sqrt{{\mathrm{Hz}}}}]

The quantity :math:`S_F` is an especially useful figure of merit for
force detection near resonance; it allows one to compare cantilevers
without specifying a detection bandwidth. Equation :eq:`eq:SF` makes clear
what is required for best force sensitivity:

-  lowest possible spring constant :math:`k`

-  lowest possible temperature :math:`T`

-  highest possible quality factor :math:`Q`

-  highest possible resonance frequency :math:`f_0`

Rewrite :math:`S_F` by substituting :math:`k = 4 \pi^2 f_0^2 m` and
writing :math:`Q =
\tau f_0` where :math:`\tau` here is the cantilever damping time. This
recasts :math:`S_F` as

.. math:: S_F = \sqrt{ 8 \pi \: k_B T \: \frac{m}{\tau} \: \Delta \! f}

Another way to achieve the best possible force sensitivity is to:

-  work at the lowest possible temperature :math:`T`

-  minimize cantilever motional mass :math:`m`

-  maximize cantilever damping times :math:`\tau`

.. _sect:cantilever-design:

Cantilever Design
-----------------

The resonance frequency and spring constant for a beam cantilever of
length :math:`l`, width :math:`w`, and thickness :math:`t` are:

.. math:: f_0 = \frac{3.516}{2 \pi} \frac{t}{l^2} \left( \frac{E}{12 \rho} \right)^{1/2}

.. math:: k = 1.030 \frac{l}{4} \frac{E w t^3}{l^3}

where :math:`E` is Young’s modulus and :math:`\rho` is density
(:math:`E = 1.9 \times
10^{11} \: {\mathrm{N}} \: {\mathrm{m}}^{-2}` and
:math:`\rho = 2.3 \times 10^{3} \:
\mathrm{kg} \: {\mathrm{m}}^{-3}` for silicon). In terms of cantilever
properties,

.. math:: S_F = 1.588 \left( \frac{k_B T}{Q} \right)^{1/2} (\rho E)^{1/4} \left( \frac{w}{l} \right)^{1/2} t

The critical cantilever parameter to optimize to achieve the best
possible force sensitivity is thus cantilever thickness :math:`t`. The
next best cantilever property to optimize is the width to length ratio,
:math:`w/l`. Finally, cantilever material density and Young’s modulus,
because they appear in :math:`S_F` to the 1/4 power, are the least
important parameters to optimize.

.. _sect:appendix-an-integral:

Appendix
--------

We wish to compute the following integral

.. math:: P = P_z(0) \: f_0^4 \int_{0}^{\infty} df \frac{1}{(f^2 - f_0^2)^2 + f^2 f_0^2 / Q^2}

This integral can be rearranged to resemble an integral found in
standard tables or that Mathematica can solve. Let

.. math::

   \begin{split}
   f & = f_0 F \\
   df & = f_0 dF
   \end{split}

where :math:`F` is a unitless frequency parameter. The integral
rewritten in terms of :math:`F` is

.. math:: P = P_z(0) \: f_0^4 \int_{0}^{\infty} \frac{f_0 \: dF}{(f_0^2 F^2 - f_0^2)^2 + F^2 f_0^4 / Q^2}

which may be rewritten as

.. math:: P = P_z(0) \: Q \: f_0 \int_{0}^{\infty} \frac{Q \: dF}{Q^2 (F^2 - 1)^2 + F^2}

The integral is of order unity: the integrand is a function that is
:math:`\sim Q` wide and :math:`\sim Q` tall, so the area of the function
is approximately one. The integral is computed by Mathematica to be

.. math:: \int_{0}^{\infty} \frac{Q \: dF}{Q^2 (F^2 - 1)^2 + F^2} = \frac{\pi}{2}

We conclude that

.. math:: P = \frac{\pi}{2} \: P_z (0) \: Q \: f_0

References
==========

.. [#Press1986] Press, W. H.; Flannery, B. P.; Teukolsky, S. A. & Vetterling, W. T. Numerical Recipes, The Art of Scientific Computing.  Cambridge University Press, New York (1986).

.. [#Weissbluth1989] Weissbluth, M. Photon-Atom Interactions. Academic Press, New York (1989).  We modify Weiessbluth's treatment a little.  He considers a signal that extends in time from :math:`t = -T` to :math:`t = +T` while we consider instead a signal that extends in time from :math:`t = 0` to :math:`t = T`.  

