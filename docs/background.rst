Theoretical Background
======================

OK ... 

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