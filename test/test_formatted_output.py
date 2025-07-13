import unittest
from model.formatted_record_a import FormattedRecordA
from model.formatted_record_b import FormattedRecordB

class TestFormattedRecord(unittest.TestCase):
    """
    Unit tests for FormattedRecordA and FormattedRecordB
    """

    def test_format_a(self):
        rec = FormattedRecordA(1, "apple", 1.23)
        self.assertEqual(rec.display(), "1 - apple - $1.23")

    def test_format_b(self):
        rec = FormattedRecordB(2, "banana", 2.50)
        self.assertEqual(rec.display(), "[ID: 2] BANANA = $2.50")

if __name__ == '__main__':
    unittest.main()
