Tutorials
=========

The two tutorials derive the properties of a microcantilever in thermal equilibrium at temperature :math:`T`.  We characterize the cantilever by its resonance frequency :math:`f_0 \: [\mathrm{Hz}]`, ringdown time :math:`\tau_0 \: [\mathrm{s}]`, and frictional coefficient :math:`\Gamma \: [\mathrm{N} \mathrm{s} \mathrm{m}^{-1}]`.

The cantilever experiences a stochastic force arising from its interaction with the environment that gives rise to thermal fluctuations in cantilever position.  In the first tutorial we show that the resulting power spectrum of these thermal fluctuations in cantilever position is given by

.. math::
    :label: Eq:Pdzf
    
    P_{\delta z}(f) =  \frac{k_b T \tau_0^2}{\Gamma}
        \frac{1}{(\pi \tau_0)^4 (f_0^2 - f^2)^2 + (\pi \tau_0)^2 f^2}

with  :math:`k_b` Boltzmann's constant.  Assuming that the cantilever's temperature is known, we can fit the observed power spectrum of position fluctuations to equation :eq:`Eq:Pdzf` to obtain :math:`f_0`, :math:`\tau_0`, and :math:`\Gamma`.  In terms of the quantities in equation :eq:`Eq:Pdzf`, the cantilever spring constant and quality factor are computed as :math:`k = 2 \pi^2 f_0^2 \tau_0 \Gamma \: [\mathrm{N} \: \mathrm{m}^{-1}]` and :math:`Q = \pi f_0 \tau_0 \: [\mathrm{unitless}]`, respectively. 

Both thermomechanical position fluctuations and detector noise contribute to the noise observed in the cantilever frequency determined using the algorithm described in the Introduction.  In the second tutorial we show that these two noise sources give rise to apparent fluctuations in cantilever frequency whose power spectrum is given by 

.. math::
    :label: Eq:Pdff

    P_{\delta f}(f) = \frac{1}{x_{\mathrm{rms}}^2} 
    \left( 
        \frac{1}{4 \pi^2} \frac{k_b T}{\Gamma} \frac{1}{(\pi \tau_0 f_0^2)^2}
        + f^2 P_{\delta x}^{\mathrm{det}}
    \right)

with :math:`x_{\mathrm{rms}}` the root-mean-square amplitude of the driven cantilever, :math:`P_{\delta x}^{\mathrm{det}} \: [\mathrm{m}^2 \: \mathrm{Hz}^{-1}]` the power spectrum of detector noise written as an equivalent position fluctuation, assumed for simplicity in equation :eq:`Eq:Pdff` to be frequency indepenent in the vicinity of the cantilever resonance.


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