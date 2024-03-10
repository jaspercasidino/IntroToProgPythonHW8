# ------------------------------------------------------------------------------------------------- #
# Title: Test Presentation Classes Module
# # Description: script to test presentation class functionality
# ChangeLog: (Who, When, What)
# AWysocki, 03/10/24, created new module
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee

class TestIO(unittest.TestCase):
    def setUp(self):
        self.employee_data = []

    def test_input_menu_choice(self):
        # Simulate user input '2' and check if the function returns '2'
        with patch('builtins.input', return_value='2'):
            choice = IO.input_menu_choice()
            self.assertEqual(choice, '2')

    def test_input_employee_data(self):
        # Simulate user input for student data
        with patch('builtins.input', side_effect=['Bosco', 'Hamlin', '2024-03-09', '5']):
            IO.input_employee_data(self.employee_data,Employee)
            self.assertEqual(len(self.employee_data), 1)
            self.assertEqual(self.employee_data[0].first_name, 'Bosco')
            self.assertEqual(self.employee_data[0].last_name, 'Hamlin')
            self.assertEqual(self.employee_data[0].review_date, '2024-03-09')
            self.assertEqual(self.employee_data[0].review_rating, 5)

        # Simulate invalid first name input
        with patch('builtins.input', side_effect=['123', 'Malinfrun', '2024-03-09', 5]):
            IO.input_employee_data(self.employee_data, Employee)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

        # Simulate invalid last name input
        with patch('builtins.input', side_effect=['Topra', '123', '2024-03-09', 5]):
            IO.input_employee_data(self.employee_data, Employee)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

        # Simulate invalid review rating input
        with patch('builtins.input', side_effect=['Topra', 'Malinfrun', '2024-03-09', 6]):
            IO.input_employee_data(self.employee_data,Employee)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

        # Simulate invalid review date input
        with patch('builtins.input', side_effect=['Topra', 'Malinfrun', '03-09-2024', 5]):
            IO.input_employee_data(self.employee_data,Employee)
            self.assertEqual(len(self.employee_data), 1)  # Data should not be added due to invalid input

if __name__ == "__main__":
    unittest.main()