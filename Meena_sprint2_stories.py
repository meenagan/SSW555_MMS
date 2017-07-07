from __future__ import division
import datetime
import time
def compareTwoDates(date1, date2,date_format = "%d %b %Y"):    
    date1 = time.strptime(date1, date_format)
    date2 = time.strptime(date2, date_format)
    return date1 < date2
#Code for User Story 03:
def isbirthbeforedeath(ind_dict): 
    birthbeforedeath = {}
    for ind in ind_dict:
        if ind_dict[ind][4] == 'True':
            birthbeforedeath[ind] = 'Living life to the fullest!'
        else:
            birthdate = ind_dict[ind][2]
            deathdate = ind_dict[ind][5]
            if compareTwoDates(birthdate, deathdate) == True:
                birthbeforedeath[ind] = 'Bithdate and Deathdate are valid.'
            else:
                print 'Error: US 03: Birthdate and Deathdate for {} are not valid. Please check the dates.'.format(ind)
                birthbeforedeath[ind] = 'Birthdate and Deathdate are not valid. Please check the dates.'
    return birthbeforedeath

#Code for User Story 21: Correct gender for role:
def isGenderCorrectForRole(ind_dict, fam_dict):
    GenderForRole = {}
    for fam in fam_dict:
        GenderForRole[fam] = []
        if fam_dict[fam][0] == 'NA':
            GenderForRole[fam].append('Not a Married Couple')
        else:
            temp_husb_id = fam_dict[fam][2][1:-1]
            temp_wife_id = fam_dict[fam][4][1:-1]
            husb_gender = ind_dict[temp_husb_id][1]
            wife_gender = ind_dict[temp_wife_id][1]
            if husb_gender == 'M':
                GenderForRole[fam].append('Husband Gender is valid.')
            else:
                print 'Error: US 21: Husband Gender for {} in family {} is invalid.'.format(temp_husb_id,fam)
                GenderForRole[fam].append('Husband Gender is Invalid.')
            if wife_gender == 'F':
                GenderForRole[fam].append('Wife Gender is Valid.')
            else:
                print 'Error: US 21: Wife Gender for {} in family {} is invalid.'.format(temp_wife_id,fam)
                GenderForRole[fam].append("Wife Gender is Invalid.")
    return GenderForRole