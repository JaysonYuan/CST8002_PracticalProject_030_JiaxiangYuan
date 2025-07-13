# /model/formatted_record_b.py
"""
formatted_record_b.py
Implements an uppercase label-style record format.

Author: Jiaxiang Yuan
"""

from model.record_base import RecordBase

class FormattedRecordB(RecordBase):
    """
    Displays the record in uppercase with a label format.
    """

    def display(self) -> str:
        return f"[ID: {self.id}] {self.name.upper()} = ${self.value:.2f}"
