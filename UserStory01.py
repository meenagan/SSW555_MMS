from __future__ import division
import datetime
import time
from collections import OrderedDict
from tabulate import tabulate 
import pandas as pd 

import unittest
#Code for Test Cases:
class TestCheckDate(unittest.TestCase):
    def testcheckdate(self):
        self.assertEqual(checkdatebeforecurrentdate(datetime.date.today().strftime("%d %b %Y")), False)
    
    def testcheckdate(self):
        self.assertTrue(checkdatebeforecurrentdate("07 JAN 1990"))
    
    def testcheckdate(self):
        self.assertFalse(checkdatebeforecurrentdate("08 AUG 2020"))
    
    def testcheckdate(self):
        self.assertTrue(checkdatebeforecurrentdate("27 FEB 1987"))
    
    def testcheckdate(self):
        self.assertFalse(checkdatebeforecurrentdate("09 SEP 5054"))

#Code for User Story01:

def checkdatebeforecurrentdate(inputdate):
    date_format = "%d %b %Y"
    presentdatestring = datetime.date.today().strftime(date_format)
    presentdate = time.strptime(presentdatestring, date_format)
    inputdate = time.strptime(inputdate, date_format)
    return inputdate < presentdate

def datebeforecurrent(fam_dict,ind_dict):    
    datebeforecurrent = {}
    for fam in fam_dict:
        if fam_dict[fam][0] == 'NA':
            datebeforecurrent[fam] = 'NA'
        else:
            inputdate = fam_dict[fam][0]
        if checkdatebeforecurrentdate(inputdate) == True:
            datebeforecurrent[fam] = 'Date is Valid'
        else:
            datebeforecurrent[fam] = 'Error: Date occurs After Current Date'
    return datebeforecurrent


if __name__ == '__main__':
    unittest.main()
