# -*- coding: utf-8 -*-. 
'''
Created on 24/04/2015

@author: Luis Colorado   09-11086
@author: Jose Barrientos 10-10800

'''

import unittest
from mdlaccesscontrol import clsAccessControl

class cTesterCheckPasword(unittest.TestCase):
    
    # Casos Esquina .............................
    
    # Caso cadena de 17 caracteres
    def testStringSevenTeen(self):
        sevenTeenString = clsAccessControl()
        caso17 = "U.i4J#l2P@k8N+b0t"
        casoResultado = sevenTeenString.check_password("", caso17)
        self.assertFalse(casoResultado)
    
    # Caso cadena de 7 caracteres    
    def testStringSeven(self):
        sevenString = clsAccessControl()
        caso7 = "MG.#ne4"
        casoResultado = sevenString.check_password("", caso7)
        self.assertFalse(casoResultado)
        
    # Csaos Frontera  ......................
    
    # Caso cadena valida de 8 caracteres
    def testStringEightValid(self):
        eightValidString = clsAccessControl()
        caso8 = "lMan4n4."
        casoTrue = eightValidString.encript(caso8)
        casoResultado = eightValidString.check_password(casoTrue, caso8)
        self.assertTrue(casoResultado)
 
    # Caso cadena valida de 16 caracteres    
    def testStringSixteenValid(self):
        sixteenValidString = clsAccessControl()
        caso16 = "#mcjubJBs86*gTK."
        casoTrue = sixteenValidString.encript(caso16)
        casoResultado = sixteenValidString.check_password(casoTrue, caso16)
        self.assertTrue(casoResultado)
  
    # Casos Malicia ............................
    
    # Caso cadena de 8 caracteres vacios
    def testStringEightSpace(self):
        spaceString = clsAccessControl()
        caso = "        "
        casoResultado = spaceString.check_password("", caso)
        self.assertFalse(casoResultado)

    
