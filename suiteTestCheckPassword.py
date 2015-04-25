# -*- coding: utf-8 -*-. 
'''
Created on 24/04/2015

@author: Luis Colorado   09-11086
@author: Jose Barrientos 10-10800

'''

import unittest
from mdlaccesscontrol import clsAccessControl

class cTesterCheckPasword(unittest.TestCase):
    
    # Caso cadena de 7 caracteres
    def testStringSevenTeen(self):
        sizeString = clsAccessControl()
        caso17 = "U.i4J#l2P@k8N+b0t"
        casoResultado = sizeString.check_password("", caso17)
        self.assertFalse(casoResultado)
    
    # Caso cadena de 17 caracteres    
    def testStringSeven(self):
        sizeString = clsAccessControl()
        caso7 = "MG.#ne4"
        casoResultado = sizeString.check_password("", caso7)
        self.assertFalse(casoResultado)
        