from __future__ import division
import nltk

def US15(fam_dict,ind_dict):
    for key, value in fam_dict.items():
        children_id=value[6]
        if children_id is None:
                continue
        child_count=len(children_id)
            
        if child_count>=15:
            print "ERROR: US 15: There are", child_count, "children (", children_id, ") in one family. (Max = 14)"
            
    return True


def US25(fam_dict,ind_dict):
    for key, value in fam_dict.items():
        children_id=value[6]
        child_name_birth_list=[]
        for child in children_id:
            child_value=ind_dict.get(child) 
            if child_value is None:
                continue
            child_name=child_value[0]
            child_birthdate=child_value[2]
            child_name_birth=child_name + " ",child_birthdate
            child_name_birth_list.append(child_name_birth) 
                        
        child_namebirth_freqdist = nltk.FreqDist(child_name_birth_list)
        child_namebirth_common = child_namebirth_freqdist.most_common()
        child_namebirth_common_dict = dict(child_namebirth_common)
        
        for k,v in child_namebirth_common_dict.iteritems():
            if v > 3:
                print "ERROR: US 25:", v, "siblings with the same name and birth date (", k, "). (Max=1) "
        
    return True
            