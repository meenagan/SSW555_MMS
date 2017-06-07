from __future__ import division
from datetime import datetime
from collections import OrderedDict

if __name__ == "__main__":	
	
	filename = 'My-Family-25-May-2017-601.txt'
	with open(filename) as f:
		data_list = f.read().splitlines()
	ind_dict = {}
	numrows = len(data_list)
	date_format = "%d %b %Y"
	
	for ind_id,ind_line in enumerate(data_list):
		if 'INDI' in ind_line:
			unique_id = ind_line.split(" ")[1][1:-1]
			ind_dict[unique_id] = []
			j = ind_id
			famc_set = set()
			fams_set = set()
			while True:								
				j = j + 1
				if (j >= numrows) or ('INDI' in data_list[j]):
					break
				if 'NAME' in data_list[j]:
					name = data_list[j].partition("NAME ")[2]
				if 'SEX' in data_list[j]:
					sex = data_list[j].partition("SEX ")[2]
				if 'BIRT' in data_list[j]:
					birth_date = data_list[j+1].partition("DATE ")[2]
					birth_date_datetime = datetime.strptime(birth_date,date_format)
					alive_flag = 'True'
					age = int((datetime.now() - birth_date_datetime).days/365)
					death_date = 'NA'
				if 'DEAT' in data_list[j]:
					alive_flag = 'False'
					death_date = data_list[j+1].partition("DATE ")[2]
					death_date_datetime = datetime.strptime(death_date,date_format)					
					age = int((death_date_datetime - birth_date_datetime).days/365)	
				if 'FAMC' in data_list[j]:
					famc_set.add(data_list[j].partition("FAMC ")[2][1:-1])
				if 'FAMS' in data_list[j]:
					fams_set.add(data_list[j].partition("FAMS ")[2][1:-1])		
			if len(famc_set) == 0:
				famc_set = {'NA'}
			if len(fams_set) == 0:
				fams_set = {'NA'}
			ind_dict[unique_id].extend((name,sex,birth_date,age,alive_flag,death_date,famc_set,fams_set))	
	ind_dict_sorted = OrderedDict(sorted(ind_dict.items(),key = lambda s: int(s[0][1:])))