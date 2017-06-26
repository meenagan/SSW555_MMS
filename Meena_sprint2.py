#Code for User-Story-02
from __future__ import division
import datetime
import time
def marriagebeforebirth(fam_dict,ind_dict):    
    fam_dict_marriagebeforebirth = {}
    for fam in fam_dict:
        if fam_dict[fam][0] == 'NA':
            fam_dict_marriagebeforebirth[fam] = 'single ready to mingle'
        else:
            marriagedate = fam_dict[fam][0]
            husbid = fam_dict[fam][2][1:-1]
            wifeid = fam_dict[fam][4][1:-1]
            husbbirthdate = ind_dict[husbid][2]
            wifebirthdate = ind_dict[wifeid][2]
            if not isMarriageBeforeBirth(husbbirthdate,marriagedate):
                print "ERROR: FAMILY: US02 :",husbid," Husband's birth date ", husbbirthdate, ": after marriage date ",marriagedate
            if  not isMarriageBeforeBirth(wifebirthdate,marriagedate):
                print "ERROR: FAMILY: US02 :", wifeid, " Wife's birth date ", wifebirthdate,": after marriage date ", marriagedate


def isMarriageBeforeBirth(birthdate, marriagedate):
    date_format = "%d %b %Y"
    marriagedate = time.strptime(marriagedate, date_format)
    birthdate = time.strptime(birthdate, date_format)
    return birthdate < marriagedate


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
            print "ERROR: FAMILY: US01 :",inputdate, ": occurs in the future"


