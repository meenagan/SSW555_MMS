from __future__ import division
import datetime
import time
import math
#Code for User Story 22
def checkUniqueID(data_list):
    ListofID = []
    for ind_id, ind_line in enumerate(data_list):
        if ('INDI' in ind_line) or ('FAM' in ind_line[-3:]):
            unique_id = ind_line.split(" ")[1][1:-1]
            ListofID.append(unique_id)
    if len(ListofID) > len(set(ListofID)):
        print "Your List of ID's is not Unique"
        return False
    else:
        print "Your List of ID's is Unique!"
        return True

#Code for User Story 27
def getAges(ind_dict):
    ind_Ages = {}
    date_format = "%d %b %Y"
    presentdatestring = datetime.date.today().strftime(date_format)
    presentdate = datetime.datetime.strptime(presentdatestring, date_format)
    for ind in ind_dict:
        birthdate = datetime.datetime.strptime(ind_dict[ind][2],date_format)        
        if ind_dict[ind][4] == 'True':
            ind_Ages[ind] = math.floor((presentdate - birthdate).days / 365)
        else:
            deathdate = datetime.datetime.strptime(ind_dict[ind][5], date_format)
            ind_Ages[ind] = math.floor((deathdate - birthdate).days / 365)
    print "The Dictionary of Ages: "
    print ind_Ages
    return ind_Ages


