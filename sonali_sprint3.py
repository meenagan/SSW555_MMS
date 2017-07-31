from datetime import datetime
def getRecentBirths(ind_dict,date_format):
    print("List of people who were born in the last 30 days:")
    for key in ind_dict:
        value = ind_dict[key]
        unique_id = key
        name = value[0]
        name = name[:name.index('/')].strip()
        birth_date = value[2]
        if birth_date is not 'NA':
         birth_date_datetime = datetime.strptime(birth_date, date_format)
         if (datetime.now()-birth_date_datetime).days<31 and (datetime.now()-birth_date_datetime).days>0 :
                    print(unique_id, name)

def getRecentDeaths(ind_dict,date_format):
    print("List of people who died in the last 30 days:")
    for key in ind_dict:
        value = ind_dict[key]
        unique_id = key
        name = value[0]
        name = name[:name.index('/')].strip()
        death_date = value[5]
        if death_date is not 'NA':
            death_date_datetime = datetime.strptime(death_date, date_format)
            if (datetime.now() - death_date_datetime).days < 31 and (datetime.now() - death_date_datetime).days > 0:
                print(unique_id, name)


