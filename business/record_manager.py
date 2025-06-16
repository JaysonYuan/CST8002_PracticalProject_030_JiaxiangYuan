"""
business/record_manager.py
Handles business logic for Sr-90 Record objects.
"""

from model.record import Record

class RecordManager:
    def __init__(self):
        self.records = []

    def add_record(self, record: Record):
        self.records.append(record)

    def remove_record(self, index: int):
        if 0 <= index < len(self.records):
            del self.records[index]
            return True
        return False

    def get_all_records(self):
        return self.records

    def search_by_province(self, province: str):
        return [r for r in self.records if r.province.lower() == province.lower()]
