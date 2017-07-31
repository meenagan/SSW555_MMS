from __future__ import division
import datetime
import time
import math
#Code for User Story 29: List Deceased individuals
def checkDeceased(ind_dict):
	ListofDead = {}
	counter = 0
	for ind in ind_dict:
		if ind_dict[ind][4] == 'False':
			ListofDead[counter] = ind_dict[ind][0]
			counter = counter + 1
	return ListofDead.values()

#Code for user Story 30: List Living & Married
def checkAliveAndMarried(ind_dict, fam_dict):
	ListofAliveandMarried = {}
	counter = 0
	for fam in fam_dict:
		if fam_dict[fam][1] == 'NA':
			temp_husb_id = fam_dict[fam][2][1:-1]
			temp_wife_id = fam_dict[fam][4][1:-1]
			if len(temp_husb_id)>0 and len(temp_wife_id)>0:
				temp_husb_name = fam_dict[fam][3]
				temp_wife_name = fam_dict[fam][5]
				if ind_dict[temp_husb_id][4] == 'True' and ind_dict[temp_wife_id][4] == 'True':
					ListofAliveandMarried[counter] = temp_wife_name + "is happily married to" + temp_husb_name
					counter = counter + 1
	return ListofAliveandMarried.values()