# /model/formatted_record_a.py
"""
formatted_record_a.py
Implements a simple dash-separated record format.

Author: Jiaxiang Yuan
"""

from model.record_base import RecordBase

class FormattedRecordA(RecordBase):
    """
    Displays the record in standard dash-separated format.
    """

    def display(self) -> str:
        return f"{self.id} - {self.name} - ${self.value:.2f}"
