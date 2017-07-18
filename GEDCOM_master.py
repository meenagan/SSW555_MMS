from __future__ import division
from datetime import datetime
from collections import OrderedDict
from tabulate import tabulate  # added
import pandas as pd  # added
from sonali_sprint1 import isDivorceAfterMarriage
from sonali_sprint2 import  isBirthAfterMarriage, isBirthBeforeDeathofParents
from sonali_sprint3 import  getRecentBirths, getRecentDeaths
from Matt_sprint1 import Marriage_before_HusbDeath,Marriage_before_WifeDeath,Divorce_before_HusbDeath,Divorce_before_WifeDeath
from Matt_sprint02 import US12_US14
from Meena_sprint1 import marriagebeforebirth, datebeforecurrent
from Meena_sprint2_stories import isbirthbeforedeath, isGenderCorrectForRole

if __name__ == "__main__":

    filename = 'My-Family-25-May-2017-601.txt'
    with open(filename) as f:
        data_list = f.read().splitlines()
    ind_dict = {}
    numrows = len(data_list)
    date_format = "%d %b %Y"

    for ind_id, ind_line in enumerate(data_list):
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
                    birth_date = data_list[j + 1].partition("DATE ")[2]
                    birth_date_datetime = datetime.strptime(birth_date, date_format)
                    alive_flag = 'True'
                    age = int((datetime.now() - birth_date_datetime).days / 365)
                    death_date = 'NA'
                if 'DEAT' in data_list[j]:
                    alive_flag = 'False'
                    death_date = data_list[j + 1].partition("DATE ")[2]
                    death_date_datetime = datetime.strptime(death_date, date_format)
                    age = int((death_date_datetime - birth_date_datetime).days / 365)
                if 'FAMC' in data_list[j]:
                    famc_set.add(data_list[j].partition("FAMC ")[2][1:-1])
                if 'FAMS' in data_list[j]:
                    fams_set.add(data_list[j].partition("FAMS ")[2][1:-1])
            if len(famc_set) == 0:
                famc_set = {'NA'}
            if len(fams_set) == 0:
                fams_set = {'NA'}
            ind_dict[unique_id].extend((name, sex, birth_date, age, alive_flag, death_date, famc_set, fams_set))
    ind_dict_sorted = OrderedDict(sorted(ind_dict.items(), key=lambda s: int(s[0][1:])))

#added
df = pd.DataFrame.from_dict(ind_dict_sorted, orient="index")
df.columns = ["Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
df.index.name = "ID"
print (tabulate(df, headers='keys', tablefmt='fancy_grid'))

fam_dict = {}

for fam_id, ind_line in enumerate(data_list):
    if 'FAM' in ind_line[-3:]:
        unique_id = ind_line.split(" ")[1][1:-1]
        fam_dict[unique_id] = []
        j = fam_id
        child_set = set()
        marr_date = 'NA'
        div_date = 'NA'
        husb_id = 'NA'
        husb_name = 'NA'
        wife_id = 'NA'
        while True:
            j = j + 1
            if (j >= numrows) or ('FAM' in data_list[j]):
                break
            if 'HUSB' in data_list[j]:
                husb_id = data_list[j].partition("HUSB ")[2]
            if 'WIFE' in data_list[j]:
                wife_id = data_list[j].partition("WIFE ")[2]
            if 'CHIL' in data_list[j]:
                child_set.add(data_list[j].partition("CHIL ")[2][1:-1])
            if 'MARR' in data_list[j]:
                div_date = 'NA'
                marr_date = data_list[j + 1].partition("DATE ")[2]
            if 'DIV' in data_list[j]:
                div_date = data_list[j + 1].partition("DATE ")[2]
        if len(child_set) == 0:
            child_set = {'NA'}
        if husb_id != 'NA':
            husb_name = ind_dict[husb_id[1:-1]][0]
        if wife_id != 'NA':
            wife_name = ind_dict[wife_id[1:-1]][0]

        fam_dict[unique_id].extend((marr_date, div_date, husb_id, husb_name, wife_id, wife_name, child_set))
dict_fam_sorted = OrderedDict(sorted(fam_dict.items(), key=lambda s: int(s[0][1:])))

df_fam = pd.DataFrame.from_dict(dict_fam_sorted, orient="index")
df_fam.columns = ["Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
df_fam.index.name = "ID"
print(tabulate(df_fam, headers='keys', tablefmt='fancy_grid'))

isDivorceAfterMarriage(data_list)
isBirthAfterMarriage(ind_dict,fam_dict,date_format)
isBirthBeforeDeathofParents(ind_dict,fam_dict,date_format)
Marriage_before_HusbDeath(fam_dict,ind_dict)
Marriage_before_WifeDeath(fam_dict,ind_dict)
Divorce_before_HusbDeath(fam_dict,ind_dict)
Divorce_before_WifeDeath(fam_dict,ind_dict)
marriagebeforebirth(fam_dict,ind_dict)
datebeforecurrent(fam_dict,ind_dict)
isbirthbeforedeath(ind_dict)
isGenderCorrectForRole(ind_dict,fam_dict)
US12_US14(fam_dict,ind_dict)

getRecentBirths(ind_dict,date_format)
getRecentDeaths(ind_dict,date_format)