Practical Details
=================

**Fourier Transform and Units**.   We will analyze our signal using the discrete Fourier Transform (DFT) ``numpy.fft`` summarized in :ref:`Conventions`.  We will display the Fourier transformed data, however, as if it had been obtained by a continuous Fourier Transform (FT).  The outputs of the FT integral and the DFT sum are proportional but not equal.  We can see this immediately by units analysis:  for data :math:`a_n` (and :math:`a(t)`) having units of nanometers, the discrete Fourier transform :math:`A_k` has units of :math:`\text{nm}` while the continuous Fourier transform :math:`\hat{a}(f)` has units of :math:`\text{nm} \: \text{Hz}^{-1}`.  The FT is obtained from the DFT as follows.

Consider the continuous Fourier transform

.. math::
    
    \hat{a}(f) = \int_{-\infty}^{+\infty} dt \: 
        a(t) \: e^{-2 \pi \imath f t } 

We can convert this integral to a sum using the following correspondences.  With :math:`\Delta t` the time per point,

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

We conclude that the continous Fourier transform is obtained from the discrete Fourier transform using

.. math::

    \hat{a}(f_k) = \Delta t \: A_k    

**Power Spectrum and Units**.

**Hilbert Transform**.

**Analysis of Thermomechanical Motion**.

.. cross referencing: http://sphinx-doc.org/markup/inline.html