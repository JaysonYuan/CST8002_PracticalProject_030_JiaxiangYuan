"""
Unit test for FormattedRecordA and FormattedRecordB classes.

Author: Jiaxiang Yuan
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from model.formatted_record_a import FormattedRecordA
from model.formatted_record_b import FormattedRecordB

class TestPolymorphicRecords(unittest.TestCase):

    def test_dash_format(self):
        """
        Test FormattedRecordA display method.
        """ 
        rec = FormattedRecordA("001", "Calgary-AB-01-Jan-84", 0.105)
        expected = "001 - Calgary-AB-01-Jan-84 - 0.105"
        self.assertEqual(rec.display(), expected)

    def test_label_format(self):
        """
        Test FormattedRecordB display method.
        """
        rec = FormattedRecordB("002", "Calgary-AB-01-Apr-84", 0.0628)
        expected = "ID: 002\nName: Calgary-AB-01-Apr-84\nValue: 0.0628"
        self.assertEqual(rec.display(), expected)

if __name__ == '__main__':
    print("Unit test by Jiaxiang Yuan")
    unittest.main()
