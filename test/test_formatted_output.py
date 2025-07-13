import unittest
from model.formatted_record_a import FormattedRecordA
from model.formatted_record_b import FormattedRecordB

class TestFormattedRecord(unittest.TestCase):
    """
    Unit tests for FormattedRecordA and FormattedRecordB
    """

    def test_format_a(self):
        rec = FormattedRecordA("001", "station-prov-2025-07-13", 1.23456)
        expected = "Record 001 - station-prov-2025-07-13 - Sr90: 1.23456 Bq/L"
        self.assertEqual(rec.display(), expected)

    def test_format_b(self):
        rec = FormattedRecordB("002", "station-prov-2025-07-14", 2.5)
        expected = "[RECORD ID: 002] :: STATION-PROV-2025-07-14 ==> Sr90 LEVEL = 2.50000 Bq/L"
        self.assertEqual(rec.display(), expected)

if __name__ == '__main__':
    unittest.main()
