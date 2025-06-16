"""
tests/test_record_manager.py
Unit test for RecordManager class.

Program by Jiaxiang Yuan
"""

import unittest
from business.record_manager import RecordManager
from model.record import Record

class TestRecordManager(unittest.TestCase):

    def setUp(self):
        self.manager = RecordManager()
        # Add initial record
        self.record1 = Record("Milk", "Type1", "2020-01-01", "2020-01-31",
                              "Station A", "ProvinceA", "10.5", "0.1", "5.0")
        self.manager.add_record(self.record1)

    def test_add_record(self):
        new_record = Record("Milk", "Type2", "2020-02-01", "2020-02-28",
                            "Station B", "ProvinceB", "12.0", "0.2", "6.0")
        self.manager.add_record(new_record)
        self.assertEqual(len(self.manager.get_all_records()), 2)
        self.assertEqual(self.manager.get_all_records()[1].station_name, "Station B")

    def test_edit_record(self):
        updated_record = Record("Milk", "Type1-Updated", "2020-01-01", "2020-01-31",
                                "Station A", "ProvinceA", "11.0", "0.1", "5.5")
        result = self.manager.edit_record(0, updated_record)
        self.assertTrue(result)
        self.assertEqual(self.manager.get_all_records()[0].type_, "Type1-Updated")

    def test_delete_record(self):
        result = self.manager.delete_record(0)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.get_all_records()), 0)

    def test_find_records_by_province(self):
        found = self.manager.find_records_by_province("ProvinceA")
        self.assertEqual(len(found), 1)
        found_none = self.manager.find_records_by_province("NonExistent")
        self.assertEqual(len(found_none), 0)

if __name__ == "__main__":
    unittest.main()
