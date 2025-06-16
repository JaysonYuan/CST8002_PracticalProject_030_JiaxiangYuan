"""
tests/test_record_manager.py
Unit tests for the RecordManager class.
"""

import unittest
from business.record_manager import RecordManager
from model.record import Record

class TestRecordManager(unittest.TestCase):
    def setUp(self):
        self.manager = RecordManager()
        self.record = Record("MILK", "WHOLE", "2020-01-01", "2020-01-31",
                             "OTTAWA", "ON", "0.05", "0.01", "0.03")
        self.manager.add_record(self.record)

    def test_add_record(self):
        self.assertEqual(len(self.manager.records), 1)

    def test_remove_record_valid(self):
        result = self.manager.remove_record(0)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.records), 0)

    def test_remove_record_invalid(self):
        result = self.manager.remove_record(10)
        self.assertFalse(result)

    def test_search_by_province_found(self):
        results = self.manager.search_by_province("ON")
        self.assertEqual(len(results), 1)

    def test_search_by_province_not_found(self):
        results = self.manager.search_by_province("BC")
        self.assertEqual(len(results), 0)

if __name__ == "__main__":
    unittest.main()
