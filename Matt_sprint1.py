
def Marriage_before_HusbDeath(fam_dict):
    for key, value in fam_dict.items():

        marr_date = value[0]
        if marr_date == 'NA':
            continue
        if marr_date != 'NA':
            marr_date_datetime = datetime.strptime(marr_date, date_format)
        
        husb_id = value[2][1:-1]
        husb_value = ind_dict.get(husb_id)
        husb_deathdate = husb_value[5]
        
        if husb_deathdate != 'NA':
            husb_deathdate_datetime = datetime.strptime(husb_deathdate, date_format)
        elif husb_deathdate == 'NA':
            husb_deathdate_datetime = datetime.now()
    
        if husb_deathdate_datetime < marr_date_datetime:
            print "Error: US 05: Death date (", husb_deathdate_datetime, ") of husband", husb_id, "before marriage date (", marr_date, ")" "\n"
            return True
            
def Marriage_before_WifeDeath():
    for key, value in fam_dict.items():

        marr_date = value[0]
        if marr_date == 'NA':
            continue
        if marr_date != 'NA':
            marr_date_datetime = datetime.strptime(marr_date, date_format)
        
        wife_id = value[4][1:-1]
        wife_value = ind_dict.get(wife_id)
        wife_deathdate = wife_value[5]
        
        if wife_deathdate != 'NA':
            wife_deathdate_datetime = datetime.strptime(wife_deathdate, date_format)
        elif wife_deathdate == 'NA':
            wife_deathdate_datetime = datetime.now()
    
        if wife_deathdate_datetime < marr_date_datetime:
            print "Error: US 05: Death date (" , wife_deathdate_datetime, ") of wife,", wife_id, "before marriage date (", marr_date, ")" "\n"
            return True
               
def Divorce_before_HusbDeath():
    for key, value in fam_dict.items():
       
        div_date = value[1]   
        if div_date == 'NA':
            continue
        if div_date != 'NA':
            div_date_datetime = datetime.strptime(div_date, date_format)
        
        husb_id = value[2][1:-1]
        husb_value = ind_dict.get(husb_id)
        husb_deathdate = husb_value[5]
        
        if husb_deathdate != 'NA':
            husb_deathdate_datetime = datetime.strptime(husb_deathdate, date_format)
        elif husb_deathdate == 'NA':
            husb_deathdate_datetime = datetime.now()
        
        if husb_deathdate_datetime < div_date_datetime:
            print "Error: US 06: Death date (" , husb_deathdate_datetime, ")of husband", husb_id, "before divorce date (", div_date, ")" "\n"
            return True
    
def Divorce_before_WifeDeath():
    for key, value in fam_dict.items():
       
        div_date = value[1]   
        if div_date == 'NA':
            continue
        if div_date != 'NA':
            div_date_datetime = datetime.strptime(div_date, date_format)
            
        wife_id = value[4][1:-1]
        wife_value = ind_dict.get(wife_id)
        wife_deathdate = wife_value[5]
        
        if wife_deathdate != 'NA':
            wife_deathdate_datetime = datetime.strptime(wife_deathdate, date_format)
        elif wife_deathdate == 'NA':
            wife_deathdate_datetime = datetime.now()
   
        if wife_deathdate_datetime < div_date_datetime:
            print "Error: US 06: Death date (" , wife_deathdate_datetime, ") of wife", wife_id, "before divorce date (", div_date, ")" "\n"
            return True