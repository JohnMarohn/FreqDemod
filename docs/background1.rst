Oscillator Thermomechanical Fluctuations
----------------------------------------

**Overview**.  In this tutorial we examine the steady-state response of a microcantilever to both a coherent and an incoherent driving force.  The cantilever is modeled classically as a damped harmonic oscillator.  

When the cantilever is driven by a *coherent* sinusoidal force, the steady-state solution of the equation of motion is greatly simplified by recasting the equation in terms of a complex variable whose real and imaginary parts track the in-phase and out-of-phase response, respectively, of the cantilever.  Using this approach we derive the steady-state in-phase and out-of-phase amplitude of the driven cantilever as a function of frequency.

Even when no external driving force is applied, the cantilever is acted upon by its surroundings.  The action of the surroundings can be treated as an *incoherent* driving force acting on the cantilever.  This incoherent driving force casuses fluctuations in the cantilever position which are desribed in terms of correlation functions.  We establish a link between the time-domain correlation function and the frequency-domain power spectrum of the fluctuating cantilever position.  For a cantilever in thermal contact with a bath of modes at a well-defined temperature, the form of the incoherent environmental force can be derived using the equipartition theorem of statistical mechanics.  We derive an expression of the force's power spectrum in terms of the cantilever's
friction coefficient.  We show that if the cantilever's temperature, resonance frequency, and ringdown time are known, then the cantilever spring constant can be determined from the area under the power spectrum of cantilever position fluctuations.

**Equation of Motion**.  The equation of motion for a **damped harmonic oscillator** is

.. math::
    :label: eq:HO
    
    m \: \ddot{x} + \Gamma \: \dot{x} + k \: x = F

The variables are

.. math::

   \begin{array}{lll}
    x & \text{oscillator position} & [\text{m}] \\ 
    m & \text{mass} & [\text{kg}] \\
    \Gamma & \text{friction coefficient} & [\text{kg} \: {\text{s}}^{-1} 
    = \text{N} \: \text{s} \: {\text{m}}^{-1}] \\
    k & \text{spring constant} & [\text{N} \: {\text{m}}^{-1}] \\
    F & \text{applied force} & [\text{N}]
   \end{array}

It is useful to rewrite this equation in a more canonical form. Divide
equation :eq:`eq:HO` by :math:`m`, and define new variables according to the
following equations.

.. math:: \frac{\Gamma}{m} = \frac{\omega_0}{Q}, \: \: \frac{k}{m} = \omega_0^2, \: \mbox{and} \: \frac{F}{m} = \frac{\omega_0^2 F}{k} = A

The new variables are

.. math::

   \begin{array}{lll}
    \omega_0 &\text{resonance frequency} & [\text{rad} \: {\text{s}}^{-1}] \\
    Q & \text{quality factor} & [\text{unitless}] \\
    A & \text{acceleration} & [\text{m} \: {\text{s}}^{-2}]
   \end{array}

The canonical equation of motion for a classical harmonic oscillator is
thus

.. math::
    :label: eq:HO-canonical

    \ddot{x} + \frac{\omega_0}{Q} \: \dot{x} + \omega_0^2 \: x 
        = A = \frac{\omega_0^2 \: F}{k}

**Phasors**. We wish to calculate the response of the oscillator to a resonant
force,

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
variable, :math:`z_0`.  With this goal in mind, let us introduce another complex 
variable :math:`F_c` that tracks the applied force. If the force is a sinusoidal
function of time, then :math:`F_c = F_0 \exp{(\imath \: \omega t)}` where
:math:`F_0 = | F_0 | \: \exp{(\imath \: \phi)}` is a complex number that 
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

The equation of motion for :math:`z` is

.. math::
    :label: eq:z
    
    \ddot{z} + \frac{\omega_0}{Q} \: \dot{z} + \omega_0^2 \: z 
    = \frac{\omega_0^2 \: F_c}{k}


.. _sect:steady-state-response-I: 

**Steady State Response**: It is convenient to work with the frequency expressed 
in  experimental units of :math:`[\mathrm{cyc}/{\mathrm{s}}] = [{\mathrm{Hz}}]` 
instead of :math:`[\mathrm{rad}/{\mathrm{s}}]`.  Let us therefore define

.. math:: f_0 = \frac{\omega_0}{2 \pi} \: \sim \: [\frac{\mathrm{cyc}}{{\mathrm{s}}}] = [{\mathrm{Hz}}]

and from now on with frequencies in :math:`{\mathrm{Hz}}`.

We are now ready to explore the response of the cantilever to a
**coherent sinusoidal driving force**. Substitute :math:`F_c = F_0
\exp{(\imath \: 2 \pi f t)}` into equation :eq:`eq:z` and assume that the
response :math:`z` is of the form
:math:`z_0 \exp{(\imath \: 2 \pi f t)}`.  This will be true at steady state.

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
the *out of phase* part of the response.  We can see that when the applied force
drives the oscillator right on resonance, :math:`\omega = \omega_0` and 

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
These two results are captured in the single equation

.. math:: z_0(\omega_0) = - \imath \: \frac{Q \: F_0}{k}

The response on resonance is purely imaginary and therefore ninety degrees out of phase with the applied force. 

**Correlation Functions**.  The section explores a connection between a function’s correlation function and its power spectrum.  Correlation functions
are usually applied to fluctuating quantities having zero mean.  In our case, we wish to aply correlation functions to understand fluctuations in cantilever position:

.. math::

    \delta x(t) = x(t) - \mathrm{mean}(x(t))

The correlation function of :math:`\delta x(t)` is defined as

.. math:: 
    :label: eq:Cx

    C_{\delta x}(\tau) = \int_{-\infty}^{\infty} dt \: 
        \delta x(t) \: \delta x(t+\tau) \: 
        \sim \: [\frac{{\mathrm{m}}^2}{{\mathrm{Hz}}}]

Following the Fourier Transform conventions in *Numerical Recipes*
[#Press1986]_, the Fourier and inverse Fourier transforms of
:math:`x(t)` are:

.. math:: 

    \widehat{\delta x}(f) 
    = \int_{-\infty}^{\infty} dt \: \delta x(t) 
        \: e^{\imath \: 2 \pi f t}

.. math:: 

    \delta x(t) 
    = \int_{-\infty}^{\infty} df \: \widehat{\delta x}(f) 
        \: e^{-\imath \: 2 \pi f t}

Substitute for :math:`\delta x(t)` and :math:`\delta x(t+\tau)` the appropriate
Fourier transform relation

.. math::

    C_{\delta x}(\tau) 
    = \int df  \int df^{\prime}  \: 
        \widehat{\delta x}(f^{\prime}) \: \widehat{\delta x}(f) \: 
        e^{-\imath \: 2 \pi f \tau} 
        \underbrace{\int dt \: e^{-\imath \: 2 \pi f t}  e^{-\imath \: 2 \pi f^{\prime} t}}_{\delta(f+f^{\prime}) \Longrightarrow f^{\prime} = -f}

The integral over time involving exponentials reduces to a Dirac delta
function.  Only frequencies :math:`f^{\prime} = -f` contribute to the
final double integral, so that

.. math:: C_{\delta x}(\tau) 
    = \int_{-\infty}^{\infty} df \: \: 
        \widehat{\delta x}(-f) \: \widehat{\delta x}(f) 
        \: e^{-\imath \: 2 \pi f \tau}

If :math:`\delta x(t)` is a real function of time, then it can be shown that

.. math::

    \widehat{\delta x}(-f) = {\widehat{\delta x}}^{*}(f) 


where the star indicates the complex conjugate. We have finally

.. math::
    
    \begin{split}
    C_{\delta x}(\tau) 
    & = \int_{-\infty}^{\infty} df \: 
        {\widehat{\delta x}}^{*}(f) \: \widehat{\delta x}(f) \: 
            e^{-\imath \: 2 \pi f \tau} \\ 
    & = \int_{-\infty}^{\infty} df \: 
        | \widehat{\delta x}(f) |^2 \: e^{-\imath \: 2 \pi f \tau}
    \end{split}

If we define the one-sided power spectral density as

.. math:: 

    P_{\delta x}(f) 
    = | \widehat{\delta x}(f) |^2 + | \widehat{\delta x}(-f) |^2  \: 
    \sim \: [\frac{{\mathrm{m}}^2}{{\mathrm{Hz}}^2}]

then

.. math:: 
    :label: eq:Cxresult

    C_{\delta x}(\tau)
    = \int_{0}^{\infty} df \: P_{\delta x}(f) \: 
        e^{-\imath \: 2 \pi f \tau}

This is an important result: The correlation function and the power spectrum are Fourier transform pairs.  

While equations :eq:`eq:Cx` and :eq:`eq:Cxresult` can in principle be used to
analyze thermomechanical fluctuations in the position of a microcantilever, in
practice we need to introduce a modified correlation function to analyze the
fluctuations.  The reason for this can be seen by considering the correlation
function of equation :eq:`eq:Cx` at :math:`\tau = 0`:

.. math::

    C_{\delta x}(0) 
    = \int_{-\infty}^{\infty} dt \: 
        \delta x(t)^2 \longrightarrow \infty

As indicated, this integral will diverge if applied to a real-world laboratory
signal such as a cantilever oscillation. Following Weissbluth
[#Weissbluth1989]_, let's define a more physically-relevant correlation
function as follows.

.. math:: G(\tau) \equiv \langle \delta x(t) \: \delta x(t+\tau) \rangle

.. math::
    :label: eq:CF
    
    G(\tau) \equiv \lim_{T \rightarrow \infty} \: 
    \frac{1}{T} \int_{0}^{T} 
        \delta x(t) \: \delta x(t+\tau) \: dt \: 
        \sim \: [{\mathrm{m}}^2]

The units of this correlation function are :math:`[{\mathrm{m}}^2]`, if the
units of x are :math:`[{\mathrm{m}}]`. This correlation function is quite
different from the mathematically-defined correlation function
:math:`C(\tau)` of equation :eq:`eq:Cx` whose units are
:math:`[{\mathrm{m}}^2/{\mathrm{Hz}}]`.  The correlation function at
:math:`\tau=0` (zero delay) has special significance:

.. math:: 

    \begin{split}
    G(0) 
    & = \lim_{T \rightarrow \infty} \: 
        \frac{1}{T} \int_{0}^{T} \delta x^2(t) \: dt 
    & = x_{\mathrm{rms}}^2
    \end{split}

We see that :math:`G(0)` is the mean square value of :math:`\delta x(t)` and
therefore the root-mean-square is 
:math:`{\delta x}_{\mathrm{rms}} = \sqrt{G(0)}`.

We will now reproduce Weissbluth’s treatment [#Weissbluth1989]_ relating the
(physically-relevant) correlation function :math:`G(\tau)` to an
analogous power spectrum.  Following Weissbluth, let us define the function
:math:`{\delta x}_{T}(t)` which is equal to :math:`\delta 
x(t)` on the time interval :math:`(0,T)` and is zero at all other times:

.. math:: 

    {\delta x}_{T}(t) = 
    \left\{
        \begin{array}{cc} \delta x(t) & 0 \leq t \leq T \\ 
        0 & \mathrm{otherwise} 
        \end{array}
    \right.

Let us define correlation function for :math:`{\delta x}_T` as follows:

.. math::

    \begin{split}
    G_{T}(\tau) 
    & = \frac{1}{T} \int_{0}^{T} 
        {\delta x}_T(t) \: {\delta x}_T(t+\tau) \: dt \\
    & = \frac{1}{T} \int_{-\infty}^{+\infty} 
        {\delta x}_T(t) \: {\delta x}_T(t+\tau) \: dt
    \end{split}

Since we’ve confined :math:`{\delta x}_T` to the time interval :math:`(0,T)` we can extend the limits in integration out to infinity. Now take the Fourier transform of :math:`G_{T}(\tau)`:

.. math::

    \begin{multline}
    \int_{-\infty}^{+\infty} G_{T}(\tau) 
        \: e^{\imath \: 2 \pi f \tau} \: d\tau
    = \frac{1}{T} \int_{-\infty}^{+\infty} d\tau \: 
        e^{\imath \: 2 \pi f \tau} \int_{-\infty}^{+\infty} dt
            \: {\delta x}_{T}(t) \: {\delta x}_{T}(t+\tau) \\
    = \frac{1}{T} \int_{-\infty}^{+\infty} dt 
            \: {\delta x}_{T}(t) \: e^{-\imath \: 2 \pi f t} 
        \int_{-\infty}^{+\infty} d\tau \:  
            {\delta x}_{T}(t+\tau) \: e^{\imath \: 2 \pi f (t+\tau)}
   \end{multline}

where we have inserted :math:`1 = \exp{(-\imath \: 2 \pi f t)}
\exp{(+\imath \: 2 \pi f t)}`. In the second integral, change the
variable of integration to :math:`t^{\prime} = t+\tau`. This lets us
write

.. math::

    \int_{-\infty}^{+\infty} G_{T}(\tau) 
        \: e^{\imath \: 2 \pi f \tau} \: d\tau
    = \frac{1}{T} \underbrace{\int_{-\infty}^{+\infty} dt 
        \: {\delta x}_{T}(t) \:
        e^{-\imath \: 2 \pi f t}}_{{\widehat{\delta x}}_T(-f) = {\widehat{\delta x}}^{*}_{T}(f)} \underbrace{\int_{-\infty}^{+\infty} dt^{\prime} \: {\delta x}_{T}(t^{\prime}) \: e^{\imath \: 2 \pi f t^{\prime}}}_{{\widehat{\delta x}}_T(f)}

Since :math:`x(t)` is a real function, it follows that :math:`{\widehat{\delta x}}_{T}(-f) = {\widehat{\delta x}}^{*}_{T}(f)`. We can thus write 

.. math::
    :label: eq:limitG

    \int_{-\infty}^{+\infty} G_{T}(\tau) \: e^{\imath \: 2 \pi f \tau} \: d\tau 
        = \frac{1}{T} \: | {\widehat{\delta x}}_{T}(f) |^{2}

We recover the “real” correlation function by a limiting procedure.

.. math:: 

    G(\tau) = \lim_{T \rightarrow \infty} \: G_{T}(\tau)

Take the limit on each side of equation :eq:`eq:limitG` as :math:`T \rightarrow
\infty`. On the left-hand side, :math:`G_T` becomes :math:`G`; the terms on the
right-hand side motivate us to define

.. math::
    :label: eq:PS
    
    J(f) \equiv \lim_{T \rightarrow \infty} \: 
    \frac{1}{T} \: | {\widehat{\delta x}}_{T}(f) |^{2} \: 
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
        ( | {\widehat{\delta x}}_{T}(f) |^{2} + 
          | {\widehat{\delta x}}_{T}(-f) |^{2})
    \end{split}

With these definitions of correlation function (equation :eq:`eq:CF`) and
spectral density (equation :eq:`eq:PS`), we still have that the correlation
function :math:`G(\tau)` and the power spectrum :math:`J(f)` of 
:math:`\delta x(t)` are Fourier transform pairs.

Finally, equation :eq:`eq:FTOSPS` can be used to calculate the root-mean-square
of :math:`x(t)` given a measured one-sided power spectral density:

.. math::
    :label: eq:xrmsP
    
    \begin{split}
    {\delta x}_{\mathrm{rms}}^2 
        & = \langle {\delta x}^2(t) \rangle \\
        & = G(0) = \int_{0}^{+\infty} P(f) \: df.
    \end{split}

We conclude that the area under the one-sided spectrum is the mean-square
displacement.  We note that this connection is *not* valid for the mathematically-defined power-spectrum of the last section.

**Steady-State Response Revisited**.    In this section we explore the response of the cantilever to an **incoherent** driving force.  We assume that the driving force averages to zero over long times:

.. math:: 

    \langle F(t) \rangle 
    = \lim_{T \rightarrow \infty} \: \frac{1}{T} \int_{0}^{T} F(t) \: dt
        \longrightarrow 0

The change in cantilever position resulting from such a force will likewise average to zero at long times.  At short times, however, the cantilever will experience force fluctuations :math:`\delta F(t)` and these force fluctuations will stimulate fluctuations :math:`\delta z(t)` in the cantilever's position.  Let us define correlation functions for both :math:`\delta z` and :math:`\delta F` as above,

.. math::

    G_{\delta z}(\tau) 
    \equiv \lim_{T \rightarrow \infty} \: 
        \frac{1}{T} \int_{0}^{T} \delta z(t) \: \delta z(t+\tau) \: dt \: 
        \sim \: [{\mathrm{m}}^2]

.. math::

    G_{\delta F}(\tau) 
    \equiv \lim_{T \rightarrow \infty} \: 
        \frac{1}{T} \int_{0}^{T} \delta F(t) \: \delta F(t+\tau) \: dt \: 
        \sim \: [{\mathrm{N}}^2]

With each of these correlation functions is associated a power spectrum:

.. math::

   \begin{aligned}
   G_{\delta z}(\tau) \overset{\mathrm{\small FT}}{\iff} 
        J_{\delta z}(f) \: \text{or} \: P_{\delta z}(f) \\
   G_{\delta F}(\tau) \overset{\mathrm{\small FT}}{\iff}
        J_{\delta F}(f) \: \text{or} \: P_{\delta F}(f)
   \end{aligned}

Because :math:`z` and :math:`F` are connected by an equation of motion, we can write :math:`J_{\delta z}` in terms of :math:`J_{\delta F}`, as we will now show.  Let us use a Fourier expansion to write the fluctuating quantities as follows

.. math::
    :label: eq:FTF
    
    \delta F(t) 
    = \int_{-\infty}^{\infty} df \: \widehat{\delta F}(f) 
        \: e^{-\imath \: 2 \pi f t}
    
.. math::
    :label: eq:FTz

    \delta z(t) 
    = \int_{-\infty}^{\infty} df \: \widehat{\delta z}(f) 
        \: e^{-\imath \: 2 \pi f t}

Substitute equations :eq:`eq:FTF` and :eq:`eq:FTz` into the equation of motion
connecting :math:`F` and :math:`z`, equation :eq:`eq:z`.

.. math::

    \int_{-\infty}^{+\infty} 
    (-f^2 - \imath f \: \frac{f_0}{Q} + f_0^2 ) \: \widehat{\delta z}(f) 
        \: e^{-\imath \: 2 \pi f t} \: df 
    =
    \int_{-\infty}^{+\infty}
    \frac{f_0^2}{k} \widehat{\delta F}(f) \: e^{-\imath \: 2 \pi f t} \: df

For both sides to be equal, we must have that at each frequency

.. math:: 

    \widehat{\delta z}(f) 
    = \frac{\widehat{\delta F}(f)}{k} 
        \frac{f_0^2}{f_0^2 - f^2 - \imath f \: f_0 / Q}

Taking the magnitude of each side, we infer that the power spectra are related by

.. math:: 

    | \widehat{\delta z}(f) |^2 
    = \frac{| \widehat{\delta F}(f) |^2}{k^2} 
        \frac{f_0^4}{(f_0^2 - f^2)^2 + f^2 f_0^2 / Q^2}

This equation relates “mathematical” correlation functions. It is a straightforward matter to introduce the time-averaging and limiting procedure employed above to obtain this result in terms of “physically-relevant” correlation functions:

.. math::

    P_{\delta z}(f) 
    = \lim_{T \rightarrow \infty} \frac{1}{T} 
        \: ( | {\widehat{\delta z}}_{T}(f) |^{2} + 
             | {\widehat{\delta z}}_{T}(-f) |^{2}) \: 
            \sim \: [\frac{{\text{m}}^2}{{\text{Hz}}}]

.. math::
    :label: eq:PF

    P_{\delta F}(f) 
    = \lim_{T \rightarrow \infty} \frac{1}{T} 
        \: ( | {\widehat{\delta F}}_{T}(f) |^{2} + 
             | {\widehat{\delta F}}_{T}(-f) |^{2}) \: 
            \sim \: [\frac{{\text{N}}^2}{{\text{Hz}}}]

The result, which we write in terms of *one-sided power spectral
densities* is:

.. math::
    :label: eq:PzPF
    
    P_{\delta z}(f) = 
    \frac{P_{\delta F}(f)}{k^2}
    \frac{f_0^4}{(f_0^2 - f^2)^2 + f^2 f_0^2 / Q^2}

Given a fluctuating force :math:`\delta F(t)`, we can form a one-sided power spectrum :math:`P_{\delta F}(f)` by Fourier transforming the time-domain spectrum of :math:`\delta F` and averaging (equation :eq:`eq:PF`). We can then predict the resulting one-sided power spectrum :math:`P_{\delta z}(f)` of the response :math:`\delta z(t)` using equation :eq:`eq:PzPF`. Finally, if we wish, we could determine the time-correlation function :math:`G_{\delta z}(\tau)` of :math:`\delta z(t)` by inverse Fourier-transforming :math:`P_{\delta z}(f)`.

We can proceed no further in discussing the response of the harmonic oscillator to an incoherent driving force unless we specify a form for either :math:`\delta F(t)`, :math:`G_{\delta F}(\tau)`, :math:`J_{\delta F}(f)`, or the power spectrum :math:`P_{\delta F}(f)`. The simplest approximation is to assume that the environmental force fluctuation driving the cantilever is well-described as being *white noise*, e.g., a randomly-fluctuating with a power spectrum that is flat up to some very high frequency cutoff:

.. math::
    :label: eq:whitenoise
    
    P_{\delta F}(f) 
    = \left\{ 
        \begin{array}{cc} 
            P_{\delta F}(0) & 0 \leq f \leq f_m \\ 
            0 & f_m \leq f 
        \end{array} 
    \right.

The cutoff frequency’s numerical value is determined by the physical process giving rise to the force fluctuation. Atomic force microscope cantilevers experience force fluctuations due to random collisions with gas molecules and fluctuating cantilever phonon populations, for example. Both of these processes have characteristic timescales on the order of nanoseconds, which implies, by Fourier transforming the associated correlation function, that :math:`f_m \sim 1 / {\mathrm{ns}} = \mathrm{GHz}`.  The resonance frequencies of atomic-force microscope cantilevers are in the range of :math:`f_0 \sim 1 \: \text{to} \: 500 \: \text{kHz}`; consequently, :math:`f_0 << f_m`, and thus when considering a cantilever’s response to the above-mentioned force fluctuations the approximation of equation :eq:`eq:whitenoise` is a good one. An example of a case where the white-force-noise approximation of equation :eq:`eq:whitenoise` would *not* be valid is the cantilever being driven by acoustic room vibrations. The power spectrum of doors closing, mechanical vibrations from transformers, and people walking by the cantilever is generally not flat near the cantilever resonance frequency.

If the cantilever is being driven by white force noise, then

.. math::
    :label: eq:PzPFconst
    
    P_{\delta z}(f) = 
    \underbrace{\frac{P_{\delta F}(0)}{k^2}}_{\mathrm{\small freq. independent}} 
    \underbrace{\frac{f_0^4}{(f_0^2 - f^2)^2 + f^2 f_0^2 / Q^2}}_{\mathrm{\small freq. dependent}}






**Equipartition Theorem**.  As may be derived using statistical mechanics, a
harmonic oscillator in equilibrium with a bath of temperature :math:`T` has a 
energy expectation value for each mode equal to :math:`k_B T/2`. Thus

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


**References**

.. [#Press1986] Press, W. H.; Flannery, B. P.; Teukolsky, S. A. & Vetterling, W. T. Numerical Recipes, The Art of Scientific Computing.  Cambridge University Press, New York (1986).

.. [#Weissbluth1989] Weissbluth, M. Photon-Atom Interactions. Academic Press, New York (1989).  We modify Weiessbluth's treatment a little.  He considers a signal that extends in time from :math:`t = -T` to :math:`t = +T` while we consider instead a signal that extends in time from :math:`t = 0` to :math:`t = T`.  

