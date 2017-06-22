#Code for User-Story-02

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
            if isMarriageBeforeBirth(husbbirthdate,marriagedate) and isMarriageBeforeBirth(wifebirthdate,marriagedate):
                fam_dict_marriagebeforebirth[fam] = 'birthdate before marriage'
            else:
                fam_dict_marriagebeforebirth[fam] = 'birthdate not before marriage'
    return fam_dict_marriagebeforebirth



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
