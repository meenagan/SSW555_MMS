from datetime import datetime
def isDivorceAfterMarriage(data_list):
    numrows = len(data_list)
    date_format = "%d %b %Y"
    for ind_id, ind_line in enumerate(data_list):
        if 'INDI' in ind_line:
            unique_id = ind_line.split(" ")[1][1:-1]
            j = ind_id
            birth_date = 'NA'
            while True:
                j = j + 1
                if (j >= numrows) or ('INDI' in data_list[j]):
                    break
                if 'BIRT' in data_list[j]:
                    birth_date = data_list[j + 1].partition("DATE ")[2]
                    birth_date_datetime = datetime.strptime(birth_date, date_format)
                    if int((datetime.now() - birth_date_datetime).days) > 54750:  # current date should be less than 150 years after birth for all living people
                        print "ERROR: INDIVIDUAL: US07 : ",unique_id, ": More than 150 years old - Birth ", birth_date
                if 'DEAT' in data_list[j]:
                    death_date = data_list[j + 1].partition("DATE ")[2]
                    death_date_datetime = datetime.strptime(death_date, date_format)
                    if birth_date != 'NA':
                        if int((death_date_datetime - birth_date_datetime).days) > 54750:  # if death is after 150 years of birth
                            print "ERROR: INDIVIDUAL: US07 : ", unique_id,": More than 150 years old at death - Birth ", birth_date, ": Death ", death_date
    for fam_id, ind_line in enumerate(data_list):
        if 'FAM' in ind_line[-3:]:
            j = fam_id
            marr_date = 'NA'
            div_date = 'NA'
            husb_id = 'NA'
            wife_id = 'NA'
            while True:
                j = j + 1
                if (j >= numrows) or ('FAM' in data_list[j]):
                    break
                if 'HUSB' in data_list[j]:
                    husb_id = data_list[j].partition("HUSB ")[2][1:-1]
                if 'WIFE' in data_list[j]:
                    wife_id = data_list[j].partition("WIFE ")[2][1:-1]
                if 'MARR' in data_list[j]:
                    div_date = 'NA'
                    marr_date = data_list[j + 1].partition("DATE ")[2]
                if 'DIV' in data_list[j]:
                    div_date = data_list[j + 1].partition("DATE ")[2]
            if div_date != 'NA' and marr_date != 'NA':
                if div_date < marr_date:
                    print "ERROR: FAMILY: US04 : ", husb_id, ": Divorced ", div_date," before married on ", marr_date
                    print "ERROR: FAMILY: US04 : ", wife_id, ": Divorced ", div_date," before married on ", marr_date
