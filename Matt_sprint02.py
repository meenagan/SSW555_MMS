from __future__ import division
from datetime import datetime
import nltk


date_format = "%d %b %Y"

def US12_US14(fam_dict,ind_dict):
    for key, value in fam_dict.items():
        
        husb_id = value[2][1:-1]
        husb_value = ind_dict.get(husb_id)
        if husb_value is None:
            continue
        husb_deathdate = husb_value[5]
        husb_birthdate = husb_value[2]
        husb_birthdate_datetime = datetime.strptime(husb_birthdate, date_format)
        
        if husb_deathdate != 'NA':
            husb_deathdate_datetime = datetime.strptime(husb_deathdate, date_format)
            
        elif husb_deathdate == 'NA':
            husb_deathdate_datetime = datetime.now()
            
        husb_age = int((husb_deathdate_datetime - husb_birthdate_datetime).days/365)
        
        wife_id = value[4][1:-1]
        wife_value = ind_dict.get(wife_id)
        if wife_value is None:
            continue
        wife_deathdate = wife_value[5]
        wife_birthdate = wife_value[2]
        wife_birthdate_datetime = datetime.strptime(wife_birthdate, date_format)
        
        if wife_deathdate != 'NA':
            wife_deathdate_datetime = datetime.strptime(wife_deathdate, date_format)
        elif wife_deathdate == 'NA':
            wife_deathdate_datetime = datetime.now()
        
        wife_age = int((wife_deathdate_datetime - wife_birthdate_datetime).days/365)
        
        # Create list for USER STORY 15
        child_birthdate_list=[]
        children_id=value[6]
        for child in children_id:
            child_value=ind_dict.get(child) 
            if child_value is None:
                continue
            child_deathdate=child_value[5]
            child_birthdate=child_value[2]
            
            child_birthdate_list.append(child_birthdate)           
            child_birthdate_datetime = datetime.strptime(child_birthdate, date_format)
            
            
            if child_deathdate != 'NA':
                child_deathdate_datetime = datetime.strptime(child_deathdate, date_format)
                    
            elif child_deathdate == 'NA':
                child_deathdate_datetime = datetime.now()
        
            child_age = int((child_deathdate_datetime - child_birthdate_datetime).days/365)
                
        
            husb_age_diff = husb_age - child_age
            wife_age_diff = wife_age - child_age
            
            
            if husb_age_diff > 80:                
                print "Error: US 12: Father (", husb_id, ") more than eighty years older than child (", child, ") \n"   
            if wife_age_diff > 60:
                print "Error: US 12: Mother (", wife_id, ") more than sixty years older than child (", child, ") \n"
                
                
        #USER STORY 15: No more than five siblings should be born at the same time
        child_birthdate_freqdist = nltk.FreqDist(child_birthdate_list)
        child_birthdate_common = child_birthdate_freqdist.most_common()
        child_birthdate_common_dict = dict(child_birthdate_common)
       
        if any(value > 5 for value in child_birthdate_common_dict.itervalues()):
            print "Error: US 14: More than five children (", children_id, ") born on the same date:", child_birthdate
        
    return True
