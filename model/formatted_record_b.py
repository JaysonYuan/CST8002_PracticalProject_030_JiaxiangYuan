"""
formatted_record_b.py
Implements an uppercase label-style format.

Author: Jiaxiang Yuan
"""

from model.record_base import RecordBase

class FormattedRecordB(RecordBase):
    """
    Displays the record in uppercase with label format.
    """

    def display(self) -> str:
        return f"[RECORD ID: {self.id}] :: {self.name.upper()} ==> Sr90 LEVEL = {self.value:.5f} Bq/L"
