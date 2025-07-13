"""
formatted_record_a.py
Implements a dash-separated format for milk radiation records.

Author: Jiaxiang Yuan
"""

from model.record_base import RecordBase

class FormattedRecordA(RecordBase):
    """
    Displays the record in standard dash-separated format
    including station, date, and Sr90 activity.
    """

    def display(self) -> str:
        return f"Record {self.id} - {self.name} - Sr90: {self.value:.5f} Bq/L"
