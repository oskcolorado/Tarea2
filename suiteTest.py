# -*- coding: utf-8 -*-. 
'''
Created on 22/04/2015

@author: Luis Colorado   09-11086
@author: Jose Barrientos 10-10800

'''

import unittest
from mdlaccesscontrol import clsAccessControl

class controlTester(unittest.TestCase):
   
    def testEncriptStringWithoutChar(self):
        StringWithoutChar = clsAccessControl()
        caso = "At2sAd65scd75"
        casoResultado = StringWithoutChar.encript(caso)
        self.assertEqual(casoResultado, "")  
  
    def testEncriptStringWithoutNumber(self):
        StringWithoutNumber = clsAccessControl()
        caso = "Atssadd=scd,#"
        casoResultado = StringWithoutNumber.encript(caso)
        self.assertEqual(casoResultado, "")
    # ........................................   


    # Casos Validos----------------------------------------

    def testEncriptStringValid1(self):
        stringValid1 = clsAccessControl()
        caso = 'Josema#996'
        casoResultado = stringValid1.encript(caso)
        self.assertTrue(casoResultado)
    
    def testEncriptStringValid2(self):
        stringValid2 = clsAccessControl()
        caso = 'Oskcolorado.21'
        casoResultado = stringValid2.encript(caso)
        self.assertTrue(casoResultado)
    #------------------------------------------------------

    # Casos Malicia----------------------------------------
    def testEncriptStringEmpty(self):
        stringEmpty = clsAccessControl()
        caso = ""
        casoResultado = stringEmpty.encript(caso)
        self.assertEqual(casoResultado, "")

    def testEncriptStringWithEmpty(self):
        stringWithEmpty = clsAccessControl()
        caso = "CYT 123*OWH"
        casoResultado = stringWithEmpty.encript(caso)
        self.assertFalse(casoResultado,"No puede haber espacios en blanco")
        
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
    
    def testEncriptStringChar(self):
        stringChar = clsAccessControl()
        caso8 = "@*+.$+$#"
        caso16 = "@*+.$+$#@*+.$+$#"
        casoResultado8 = stringChar.encript(caso8)
        casoResultado16 = stringChar.encript(caso16)
        self.assertFalse(casoResultado8, None)
        self.assertFalse(casoResultado16, None)      
    #-------------------------------------------------------
  
    # Casos Frontera----------------------------------------
    def testEncriptStringLongEight(self):
        stringLongEight = clsAccessControl()
        caso8 = "JHGF.45J"
        casoResultado8 = stringLongEight.encript(caso8)
        self.assertTrue(casoResultado8)
     
    def testEncriptStringLongSixteen(self):
        stringLongSixteen = clsAccessControl()
        caso16 = "#@+HGBGTDK98**K."
        casoResultado16 = stringLongSixteen.encript(caso16)
        self.assertTrue(casoResultado16)
    #------------------------------------------------------
    
    # Casos Esquina----------------------------------------
    def testEncriptStringLongSeven(self):
        stringLongSeven = clsAccessControl()
        caso7 = "HgF.45J"
        casoResultado7 = stringLongSeven.encript(caso7)
        self.assertFalse(casoResultado7,"")
        
    def testEncriptStringLongSeventeen(self):
        stringLongSeventeen = clsAccessControl()
        caso17 = "#@+HGB.GTDK98**k."
        casoResultado17 = stringLongSeventeen.encript(caso17)
        self.assertFalse(casoResultado17)
       
            
    def testEncriptStringWithoutLetter(self):
        stringWithoutLetter = clsAccessControl()
        caso = "76254*123*#,#"
        casoResultado = stringWithoutLetter.encript(caso)
        self.assertEqual(casoResultado, "")