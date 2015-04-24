# -*- coding: utf-8 -*-. 
'''
Created on 22/04/2015

@author: Luis Colorado   09-11086
@author: Jose Barrientos 10-10800

'''

import unittest
from mdlaccesscontrol import clsAccessControl

class controlTester(unittest.TestCase):
    
    def testEncriptStringEmpty(self):
        stringEmpty = clsAccessControl()
        caso = ""
        casoResultado = stringEmpty.encript(caso)
        self.assertEqual(casoResultado, "")
        
    def testEncriptStringUpper(self):
        stringUpper = clsAccessControl()
        caso8 = "ABCDEFGH"
        caso16 = "ABCDEFGHIJKLMNOP"
        casoResultado8 = stringUpper.encript(caso8)
        casoResultado16 = stringUpper.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)
        
    def testEncriptStringLongEight(self):
        stringLongEight = clsAccessControl()
        caso8 = "JHGF.45j"
        casoResultado8 = stringLongEight.encript(caso8)
        self.assertTrue(casoResultado8)
        
    def testEncriptStringLongSixteen(self):
        stringLongSixteen = clsAccessControl()
        caso16 = "&/&hgbGTDK98()k."
        casoResultado16 = stringLongSixteen.encript(caso16)
        self.assertTrue(casoResultado16)
        
    def testEncriptStringGreaterSixteen(self):
        stringGreater = clsAccessControl()
        caso = "JSCHBBS47KSC:;)(&GBSCLKBSC"
        casoResultado = stringGreater.encript(caso)
        self.assertEqual(casoResultado, "")
        
    def testEncriptStringLeesEight(self):
        stringLess = clsAccessControl()
        caso = "A.t2"
        casoResultado = stringLess.encript(caso)
        self.assertEqual(casoResultado, "")
    '''    
    def testEncriptStringWithoutChar(self):
        StringWithoutChar = clsAccessControl()
        caso = "At2sAd65scd75"
        casoResultado = StringWithoutChar.encript(caso)
        self.assertEqual(casoResultado, "")    
    '''
    '''    
    def testEncriptStringWithoutNumber(self):
        StringWithoutNumber = clsAccessControl()
        caso = "Atssadd=scd,#"
        casoResultado = StringWithoutNumber.encript(caso)
        self.assertEqual(casoResultado, "")   
    '''    