from datetime import datetime
from dateutil import relativedelta

def isBirthAfterMarriage(ind_dict,fam_dict,date_format):
    for key in ind_dict:
        value = ind_dict[key]
        unique_id = key
        name = value[0]
        name = name[:name.index('/')].strip()
        birth_date = value[2]
        birth_date_datetime = datetime.strptime(birth_date, date_format)
        family_id = value[6]
        if family_id is not 'NA':
            marriage_date = fam_dict[family_id][0]
            if marriage_date is not 'NA':
                marriage_date_datetime = datetime.strptime(marriage_date, date_format)
                if birth_date_datetime<marriage_date_datetime:
                    print "ANOMALY: FAMILY: US08 : ", unique_id, ": child ", name, " born ", birth_date, " before marriage on ",marriage_date

            divorce_date = fam_dict[family_id][1]
            if divorce_date is not 'NA':
                divorce_date_datetime = datetime.strptime(marriage_date, date_format)
                if relativedelta.relativedelta(birth_date_datetime, divorce_date_datetime).months > 9:
                    print "ANOMALY: FAMILY: US08 : ", unique_id, ": child ", name, " born ", birth_date," after divorce on ", divorce_date


def isBirthBeforeDeathofParents(ind_dict,fam_dict,date_format):
    for key in fam_dict:
        value = fam_dict[key]
        wife_id = value[4]
        wife_id = wife_id.replace('@','')
        husb_id= value[2]
        husb_id = husb_id.replace('@', '')
        childSet = value[6]
        if not('NA'in childSet):
         indValue = ind_dict[wife_id]
         wifeDeathDate =  indValue[5]
         indValue = ind_dict[husb_id]
         husbDeathDate = indValue[5]
         for child in childSet:
            unique_id = child
            childValue = ind_dict[child]
            name = childValue[0]
            name = name[:name.index('/')].strip()
            childBirthDate = childValue[2]
            if wifeDeathDate is not 'NA' and  childBirthDate is not 'NA':
                wifeDeathDate_datetime = datetime.strptime(wifeDeathDate, date_format)
                childBirthDate_datetime = datetime.strptime(childBirthDate, date_format)
                if childBirthDate_datetime > wifeDeathDate_datetime:
                 print "ANOMALY: FAMILY: US09 : ", unique_id, ": child ", name, " born ", childBirthDate," after death of mother on ", wifeDeathDate
            if husbDeathDate is not 'NA' and childBirthDate is not 'NA':
                husbDeathDate_datetime = datetime.strptime(husbDeathDate, date_format)
                childBirthDate_datetime = datetime.strptime(childBirthDate, date_format)
                if relativedelta.relativedelta(childBirthDate_datetime, husbDeathDate_datetime).months > 9:
                     print "ANOMALY: FAMILY: US09 : ", unique_id, ": child ", name, " born ", childBirthDate," after 9 months of death of father on ", husbDeathDate






