# ------------------------------------------------------------------------------------------------- #
# Title: test_data_classes.py
# # Description: script to test data_classes class functionality
# ChangeLog: (Who, When, What)
# AWysocki, 03/10/24, created new module
# ------------------------------------------------------------------------------------------------- #
import unittest

from data_classes import Person, Employee

class TestPerson(unittest.TestCase):

    def test_person_init(self):
        person = Person("Topra","Malinfrun")
        self.assertEqual(person.first_name,"Topra")
        self.assertEqual(person.last_name,"Malinfrun")

    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):
            person = Person("123","Malinfrun")
        with self.assertRaises(ValueError):
            person = Person("Topra","123")

    def test_person_str(self):
        person = Person("Topra", "Malinfrun")
        self.assertEqual(str(person),"Topra,Malinfrun")

class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("Christopher", "Cipolla", "2024-03-09", 2)
        self.assertEqual(employee.first_name, "Christopher")
        self.assertEqual(employee.last_name, "Cipolla")
        self.assertEqual(employee.review_date, "2024-03-09")
        self.assertEqual(employee.review_rating,2)

    def test_employee_invalid_review_date(self):
        with self.assertRaises(ValueError):
            employee = Employee("Christopher", "Cipolla", "March 9th, 2024", 2)
        with self.assertRaises(ValueError):
            employee = Employee("Christopher", "Cipolla", "03/09/24", 2)
        with self.assertRaises(ValueError):
            employee = Employee("Christopher", "Cipolla", "03-09-24", 2)
        with self.assertRaises(ValueError):
            employee = Employee("Christopher", "Cipolla", "03-09-2024", 2)



if __name__ == '__main__':
    unittest.main()