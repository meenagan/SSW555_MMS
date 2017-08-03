from __future__ import division
from datetime import datetime


date_format = "%d %b %Y"


def US28(fam_dict,ind_dict):
    fam_counter=0
    for key, value in fam_dict.items():
        child_name_list=[]
        child_age_list=[]
        children_id=value[6]
        for child in children_id:
            child_value=ind_dict.get(child) 
            if child_value is None:
                continue
            child_name=child_value[0]
            child_name_list.append(child_name)
            
            child_deathdate=child_value[5]
            if child_deathdate != 'NA':
                child_deathdate_datetime = datetime.strptime(child_deathdate, date_format)
                    
            elif child_deathdate == 'NA':
                child_deathdate_datetime = datetime.now()
            
            child_birthdate=child_value[2]
            child_birthdate_datetime=datetime.strptime(child_birthdate, date_format)       
        
            child_age = int((child_deathdate_datetime - child_birthdate_datetime).days/365)
            child_age_list.append(child_age)
            
        child_name_age_dict = dict(zip(child_name_list, child_age_list))
        
        fam_counter+=1
        print "\n" "These are the children for Family", fam_counter, "from oldest to youngest: "
        child_name_age_sort = [ (v,k) for k,v in child_name_age_dict.iteritems() ]
        child_name_age_sort.sort(reverse=True)
        for v,k in child_name_age_sort:
            print "%s: %d" % (k,v)       


def US33(fam_dict,ind_dict):
        for key, value in fam_dict.items():
        
            husb_id = value[2][1:-1]
            husb_value = ind_dict.get(husb_id)
            if husb_value is None:
                continue
            husb_flag = husb_value[4]
            
            wife_id = value[4][1:-1]
            wife_value = ind_dict.get(wife_id)
            if wife_value is None:
                continue
            wife_flag = wife_value[4]            
        
            children_id=value[6]
            for child in children_id:
                child_value=ind_dict.get(child) 
                if child_value is None:
                    continue
                child_birthdate=child_value[2]
                child_name=child_value[0]
                
                child_birthdate_datetime = datetime.strptime(child_birthdate, date_format)
        
                child_age = int((datetime.now() - child_birthdate_datetime).days/365)
            
            
                if (wife_flag=='False' and husb_flag=='False' and child_age < 18):                
                    print "\n" "US 33:", child, ":", child_name, "is an orphan." "\n"   
        
