import unittest
from business.record_manager import RecordManager
from model.record import Record

class TestRecordManager(unittest.TestCase):
    def test_add_record(self):
        manager = RecordManager()
        record = Record("milk", "typeA", "2023-01-01", "2023-01-31",
                        "Station1", "ON", "5.0", "0.1", "1.2")
        manager.add_record(record)
        self.assertEqual(len(manager.records), 1)
        self.assertEqual(manager.records[0].station_name, "Station1")

if __name__ == "__main__":
    unittest.main()
