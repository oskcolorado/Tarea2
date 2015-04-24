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

    def testEncriptStringLower(self):
        stringLower = clsAccessControl()
        caso8 = "abcdefgh"
        caso16 = "abcdefghijklmnop"
        casoResultado8 = stringLower.encript(caso8)
        casoResultado16 = stringLower.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)  
    
    def testEncriptStringNumeric(self):
        stringNumeric = clsAccessControl()
        caso8 = "12345678"
        caso16 = "1234567887654321"
        casoResultado8 = stringNumeric.encript(caso8)
        casoResultado16 = stringNumeric.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)    
        self.assertTrue(casoResultado16)

    def testEncriptStringChar(self):
        stringChar = clsAccessControl()
        caso8 = "@*+.$+$#"
        caso16 = "@*+.$+$#@*+.$+$#"
        casoResultado8 = stringChar.encript(caso8)
        casoResultado16 = stringChar.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)      
    
    def testEncriptStringLongEight(self):
        stringLongEight = clsAccessControl()
        caso8 = "JHGF.45j"
        casoResultado8 = stringLongEight.encript(caso8)
        self.assertTrue(casoResultado8)
        
    def testEncriptStringLongSixteen(self):
        stringLongSixteen = clsAccessControl()
        caso16 = "#@+HGBGTDK98**k."
        casoResultado16 = stringLongSixteen.encript(caso16)
        self.assertTrue(casoResultado16)

    def testEncriptStringLongsSeven(self):
        stringLongSeven = clsAccessControl()
        caso7 = "HGF.45j"
        casoResultado7 = stringLongSeven.encript(caso8)
        self.assertTrue(casoResultado7)
        
    def testEncriptStringLongSeventeen(self):
        stringLongSeventeen = clsAccessControl()
        caso17 = "#@+HGB.GTDK98**k."
        casoResultado17 = stringLongSeventeen.encript(caso16)
        self.assertTrue(casoResultado17)


    
  
    '''            
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