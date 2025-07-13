# formatted_record_b.py
"""
Implements an uppercase label-style format.

Author: Jiaxiang Yuan
"""

from model.record_base import RecordBase

class FormattedRecordB(RecordBase):
    """
    Displays the record in uppercase with label format.
    """

    def display(self) -> str:
        # Format multi-line label style without uppercase, matching unit test
        return f"ID: {self.id}\nName: {self.name}\nValue: {self.value}"
