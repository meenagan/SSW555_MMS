from datetime import datetime
import unittest

def isMoreThan150YearsOld(birth_date, date_format):
 birth_date_datetime = datetime.strptime(birth_date, date_format)
 if int((datetime.now() - birth_date_datetime).days) > 54750:  # current date should be less than 150 years after birth for all living people
    return True
 else:
     return False

def isDeathAfter150YearsAfterBirth(birth_date, death_date, date_format):
    birth_date_datetime = datetime.strptime(birth_date, date_format)
    death_date_datetime = datetime.strptime(death_date, date_format)
    if birth_date != 'NA':
        if int((death_date_datetime - birth_date_datetime).days) > 54750:  # if death is after 150 years of birth
         return True
        else:
         return False

def isDivorceAfterMarriage(data_list):
    numrows = len(data_list)
    date_format = "%d %b %Y"
    for index, record in enumerate(data_list):
        if 'INDI' in record:
            unique_id = record.split(" ")[1][1:-1]
            j = index
            birth_date = 'NA'
            while True:
                j = j + 1
                if (j >= numrows) or ('INDI' in data_list[j]):
                    break
                if 'BIRT' in data_list[j]:
                    birth_date = data_list[j + 1].partition("DATE ")[2]
                    birth_date_datetime = datetime.strptime(birth_date, date_format)
                    if isMoreThan150YearsOld(birth_date, date_format):# if isMoreThan150YearsOld(birth_date, date_format):
                        print("ERROR: INDIVIDUAL: US07 : ", unique_id, ": More than 150 years old - Birth ",
                              birth_date)
                if 'DEAT' in data_list[j]:
                    death_date = data_list[j + 1].partition("DATE ")[2]
                    death_date_datetime = datetime.strptime(death_date, date_format)
                    if birth_date != 'NA':
                        if isDeathAfter150YearsAfterBirth(birth_date, death_date, date_format):
                            print("ERROR: INDIVIDUAL: US07 : ", unique_id,": More than 150 years old at death - Birth ", birth_date, ": Death ", death_date)
        if 'FAM' in record[-3:]:
            j = index
            marriage_date = 'NA'
            divorce_date = 'NA'
            husband_id = 'NA'
            wife_id = 'NA'
            while True:
                j = j + 1
                if (j >= numrows) or ('FAM' in data_list[j]):
                    break
                if 'HUSB' in data_list[j]:
                    husband_id = data_list[j].partition("HUSB ")[2][1:-1]
                if 'WIFE' in data_list[j]:
                    wife_id = data_list[j].partition("WIFE ")[2][1:-1]
                if 'MARR' in data_list[j]:
                    divorce_date = 'NA'
                    marriage_date = data_list[j + 1].partition("DATE ")[2]
                if 'DIV' in data_list[j]:
                    divorce_date = data_list[j + 1].partition("DATE ")[2]
            if divorce_date != 'NA' and marriage_date != 'NA':
                if divorce_date < marriage_date:
                    print("ERROR: FAMILY: US04 : ", husband_id, ": Divorced ", divorce_date," before married on ", marriage_date)
                    print("ERROR: FAMILY: US04 : ", wife_id, ": Divorced ", divorce_date," before married on ", marriage_date)


class AddTest(unittest.TestCase):
    def test_isMoreThan150YearsOld(self):
        self.assertTrue(isMoreThan150YearsOld("28 JUL 1091", "%d %b %Y" ))

    def test_isMoreThan150YearsOld(self):
        self.assertFalse(isMoreThan150YearsOld("28 JUL 1991", "%d %b %Y"))

    def test_isMoreThan150YearsOld(self):
        self.assertEqual(isMoreThan150YearsOld("19 JUL 1867", "%d %b %Y"),True)

    def test_isDeathAfter150YearsAfterBirth(self):
        self.assertEqual(isDeathAfter150YearsAfterBirth("19 JUL 1867", "13 JUN 2017", "%d %b %Y"),True)

    def test_isDeathAfter150YearsAfterBirth(self):
        self.assertEqual(isDeathAfter150YearsAfterBirth("7 MAY 1998", "13 JUN 2017", "%d %b %Y"),False)


if __name__ == '__main__':
    unittest.main()