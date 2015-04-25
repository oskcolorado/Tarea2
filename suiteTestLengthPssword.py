# -*- coding: utf-8 -*-. 
'''
Created on 24/04/2015

@author: Luis Colorado   09-11086
@author: Jose Barrientos 10-10800

'''
import unittest
from mdlaccesscontrol import clsAccessControl

class cTesterLengthPassword(unittest.TestCase):

    # Caso Valido--------------------------------------------
    def ctestLengthStringValid(self):
        sizeStringValid = clsAccessControl()
        caso = 'JOS1E*M*A1'
        casoResultado = sizeStringValid.length_password(caso)
        self.assertTrue(casoResultado)
    #-------------------------------------------------------

    # Caso Malicia------------------------------------------
    def ctestLengthStringEmpty(self):
        sizeStringEmpty = clsAccessControl()
        caso = ""
        casoResultado = sizeStringEmpty.length_password(caso)
        self.assertFalse(casoResultado)
        
    def ctestLengthStringGreatest(self):
        sizeStringGreatest = clsAccessControl()
        caso = "a * ((2**32)-1)"
        casoResultado = sizeStringGreatest.legth_password(caso)
        self.asserFalse(casoResultado,"Cadena demasiado grande")
    #---------------------------------------------------------

    # Caso Frontera-------------------------------------------
    def ctestLengthStringEight(self):
        sizeStringEight = clsAccessControl()
        caso8 = "LUIS.*12"
        casoResultado = sizeStringEight.length_password(caso8)
        self.assertFalse(casoResultado)
        
    def ctestLengthStringSixteen(self):
        sizeStringSixteen = clsAccessControl()
        caso16 = "LUIS.*12JO*SE$MA"
        casoResultado = sizeStringSixteen.length_password(caso16)
        self.assertFalse(casoResultado)
        
    # Caso Esquina----------------------------------------       
    def ctestLengthStringSeven(self):
        sizeStringSeven = clsAccessControl()
        caso7 = "LUIS.*1"
        casoResultado = sizeStringSeven.length_password(caso7)
        self.assertFalse(casoResultado)

    def ctestLengthStringNine(self):
        sizeStringNine = clsAccessControl()
        caso9 = "S.*12JOA$"
        casoResultado = sizeStringNine.length_password(caso9)
        self.assertFalse(casoResultado)

    def ctestLengthStringFitteen(self):
        sizeStringFifteen = clsAccessControl()
        caso15 = "LUIS.*1JO*SE$MA1"
        casoResultado = sizeStringFifteen.length_password(caso15)
        self.assertFalse(casoResultado)

    def ctestLengthStringSeventeen(self):
        sizeStringSeventeen = clsAccessControl()
        caso17 = "LUI1S.*12JO*SE$MA"
        casoResultado = sizeStringSeventeen.length_password(caso17)
        self.assertFalse(casoResultado)