#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# John A. Marohn (jam99@cornell.edu)
# 2014/06/28

"""

Unit Testing
------------

Unit tests for the package `freqdemod.py`were developed using the `unittest` package.  To run the unit tests, open up a terminal in the ``freqdemod`` directory and run::

	python -m unittest discover 

or::

	python -m unittest discover --verbose

Unit tests
----------

"""

from freqdemod.demodulate import Signal
import unittest
# import logging
# import os
# import re



class FilterTests(unittest.TestCase):
    """
    Make sure the filters are set up correctly
    """

    def test(self):
        """A dummy test; just so that we can be sure the tests are running.
        Delete when more tests are added to the package.""" 
        pass
    
    #def setUp(self):
    #    """
    #    Set up the logger.  Load the user's preferences file.  Override the 
    #    logging level read in from the preferences file; set the logging level
    #    to high so that no messages are printed out during unit testing.
    #    
    #    """
    #    
    #    logging.basicConfig()
    #    p = Preferences()
    #    p.Load()        
    #    p.pref['logging_level'] = 40
    #    self.p = p    
            
    #def test_ref__xml__accented_1(self):
    #    """crossref.org test #1: retrieve xml data for
    #    10.1016/j.ccr.2011.01.042, which has accented characters."""
    #    
    #    b = BibData(self.p)        
    #    b.set_doi('10.1016/j.ccr.2011.01.042')   
    #    b.query_crossref()
    #    b.decode_XML()
    #
    #    self.assertEqual(b.xml, b1)
        
# ===============================================
# ===== XML to BIB (expected failures) ==========
# ===============================================

#class BibTestsExpectedFailures(unittest.TestCase):
#    """See if we can convert xml to bib properly."""
# 
#    def setUp(self):
#        """
#        Set up the logger.  Load the user's preferences file.  Override the 
#        logging level read in from the preferences file; set the logging level
#        to high so that no messages are printed out during unit testing.
#        
#        """
#        
#        logging.basicConfig()
#        p = Preferences()
#        p.Load()        
#        p.pref['logging_level'] = 40
#        self.p = p
#        
#    def get_doi(self,doi):
#        """ 
#        Workhorse function to get the xml from crossref.org, determine 
#        the month, generate the bibkey, and convert the xml to bib.
#        
#        """
#        
#        a = ArticleData(self.p)
#        a.set_doi(doi)   
#        a.query_crossref()
#        a.decode_XML()
#        
#        a.generate_bib()
#        a.determine_month()
#        a.generate_bibkey()
#        a.order_bib()       
#        
#        self.a = a
#
#    @unittest.expectedFailure
#    def test_ref__bib__poorly_formed_xml_1(self):
#        """ 
#        Poorly formed xml:  This is an example of an author conversion
#        that fails, I believe, because the xml returned by crossref.org
#        is poorly formed. 
#        
#        """
#                               
#        self.get_doi('10.1109/JSSC.2002.808283')
#        self.assertEqual(self.a.bib['author'],u"Ham, D. and Hajimiri, A.")
