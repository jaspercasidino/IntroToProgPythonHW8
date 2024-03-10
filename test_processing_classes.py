# ------------------------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: script to test processing_classes class functionality
# ChangeLog: (Who, When, What)
# AWysocki, 03/10/24, created new module
# ------------------------------------------------------------------------------------------------- #
import json
import unittest
import tempfile

from data_classes import Employee
from processing_classes import FileProcessor

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def tearDown(self):
        # clean up an delete temporary file
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        # Create some temporary data to write to the file
        tData = [
            {"FirstName": "Bosco", "LastName": "Hamlin", "ReviewDate": "2024-03-09", "ReviewRating": 5},
            {"FirstName": "Topra", "LastName": "Malinfrun", "ReviewDate": "2024-03-04", "ReviewRating": 2}
        ]
        with open(self.temp_file_name,"w") as file:
            json.dump(tData,file)

        FileProcessor.read_employee_data_from_file(file_name=self.temp_file_name,employee_data=self.employee_data,employee_type=Employee)

        # Assert that the employee_data list contains the expected employee objects
        self.assertEqual(len(self.employee_data),len(tData))

        self.assertEqual(self.employee_data[0].first_name,"Bosco")
        self.assertEqual(self.employee_data[0].last_name,"Hamlin")
        self.assertEqual(self.employee_data[0].review_date, "2024-03-09")
        self.assertEqual(self.employee_data[0].review_rating, 5)

        self.assertEqual(self.employee_data[1].first_name, "Topra")
        self.assertEqual(self.employee_data[1].last_name, "Malinfrun")
        self.assertEqual(self.employee_data[1].review_date, "2024-03-04")
        self.assertEqual(self.employee_data[1].review_rating,2)

    def test_write_employee_data_to_file(self):
        eData = [
            Employee("Bosco","Hamlin","2024-03-09",5),
            Employee("Topra", "Malinfrun", "2024-03-04", 2)
        ]

        # Call the write_data_to_file method to write the data to the temporary file
        FileProcessor.write_employee_data_to_file(self.temp_file_name,eData)

        # Read the data from the temporary file and check if it matches the expected JSON data
        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(file_data),len(eData))

        self.assertEqual(file_data[0]["FirstName"], "Bosco")
        self.assertEqual(file_data[0]["LastName"], "Hamlin")
        self.assertEqual(file_data[0]["ReviewDate"], "2024-03-09")
        self.assertEqual(file_data[0]["ReviewRating"], 5)

        self.assertEqual(file_data[1]["FirstName"], "Topra")
        self.assertEqual(file_data[1]["LastName"], "Malinfrun")
        self.assertEqual(file_data[1]["ReviewDate"], "2024-03-04")
        self.assertEqual(file_data[1]["ReviewRating"], 2)


if __name__ == "__main__":
    unittest.main()
