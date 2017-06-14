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
    for ind_id, ind_line in enumerate(data_list):
        if 'INDI' in ind_line:
            unique_id = ind_line.split(" ")[1][1:-1]
            j = ind_id
            birth_date = 'NA'
            while True:
                j = j + 1
                if (j >= numrows) or ('INDI' in data_list[j]):
                    break
                if 'BIRT' in data_list[j]:
                    birth_date = data_list[j + 1].partition("DATE ")[2]
                    birth_date_datetime = datetime.strptime(birth_date, date_format)
                    if isMoreThan150YearsOld(birth_date, date_format):
                        print("ERROR: INDIVIDUAL: US07 : 14: ", unique_id, ": More than 150 years old - Birth ",
                              birth_date)
                if 'DEAT' in data_list[j]:
                    death_date = data_list[j + 1].partition("DATE ")[2]
                    if birth_date != 'NA':
                        if isDeathAfter150YearsAfterBirth(birth_date, death_date,date_format ):
                            print("ERROR: INDIVIDUAL: US07 : 14: ", unique_id,
                                  ": More than 150 years old at death - Birth ", birth_date, ": Death ", death_date)


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
