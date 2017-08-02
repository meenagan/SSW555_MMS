from datetime import datetime
from dateutil import relativedelta

def isMarriageAfter14(fam_dict,ind_dict,date_format):
    for family_id in fam_dict:
        value = fam_dict[family_id]
        marriage_date = value[0]
        if marriage_date is not 'NA':
         husb_id = value[2][1:-1]
         wife_id = value[4][1:-1]
         husb_birth_date = ""
         wife_birth_date =  ""
         if husb_id is not 'NA':
          husb_birth_date = ind_dict[husb_id][2]
         if wife_id is not 'NA':
          wife_birth_date = ind_dict[wife_id][2]
         if husb_birth_date is not 'NA' and family_id is not 'NA' and marriage_date is not 'NA':
             husb_birth_date_datetime = datetime.strptime(husb_birth_date, date_format)
             wife_birth_date_datetime = datetime.strptime(wife_birth_date, date_format)
             marriage_date_datetime = datetime.strptime(marriage_date, date_format)
             if relativedelta.relativedelta(marriage_date_datetime, husb_birth_date_datetime).years>0 and relativedelta.relativedelta(marriage_date_datetime, husb_birth_date_datetime).years < 14:
                 print "ERROR: FAMILY: US10 :",husb_id," Husband less than 14 years old(Birth date: ", husb_birth_date,") at the time of marriage ",marriage_date
             if relativedelta.relativedelta(marriage_date_datetime, husb_birth_date_datetime).years>0 and relativedelta.relativedelta(marriage_date_datetime, wife_birth_date_datetime).years < 14:
                 print "ERROR: FAMILY: US10 :",wife_id, " Wife less than 14 years old(Birth date: ", wife_birth_date, ") at the time of marriage ", marriage_date

def isLastNameSame(fam_dict,ind_dict,date_format):
    for family_id in fam_dict:
        family_name = fam_dict[family_id][3]
        family_name = family_name[family_name.index('/')+1:].strip()
        family_name = family_name[:family_name.index("/")].strip()
        isSameFamilyname = True
        if family_id is not 'NA':
         for ind_id in ind_dict:
             family_id_from_ind_dict = ind_dict[ind_id][6]
             gender = ind_dict[ind_id][1]
             name = ind_dict[ind_id][0]
             last_name = name[name.index('/') + 1:].strip()
             last_name = last_name[:last_name.index("/")].strip()
             if family_id==family_id_from_ind_dict and gender is "M":
                 if family_name!=last_name:
                     isSameFamilyname = False
                     print "ERROR: INDIVIDUAL: US 16 : Male family member", ind_id, "does not have same last name (",last_name,") as family name ", family_name
                     # alternate code
                     # use flag to set false if any of the indiavidual from the family does not have the last name same as family name and when the loop which is iterating through
                     # individual dictionary ends, check if the flag is false print error saying "Not all male have same surname"
         # if not isSameFamilyname:
                     #print("Not all male from same familt have same last name")

