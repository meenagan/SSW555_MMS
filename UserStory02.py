import datetime
import time

def isMarriageBeforeBirth(birthdate, marriagedate):
	date_format = "%d %b %Y"
	marriagedate = time.strptime(marriagedate, date_format)
	birthdate = time.strptime(birthdate, date_format)
	return birthdate < marriagedate
