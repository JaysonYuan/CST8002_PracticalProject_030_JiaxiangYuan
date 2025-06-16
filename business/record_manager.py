"""
business/record_manager.py
Business logic for managing Sr-90 milk records in-memory.

Program by Jiaxiang Yuan
"""

from model.record import Record

class RecordManager:
    """
    Manages a collection (list) of Record objects with CRUD operations.
    """
    def __init__(self):
        self.records = []

    def load_records(self, records_list):
        """
        Replace current records with a new list of Record objects.
        """
        self.records = records_list

    def get_all_records(self):
        """
        Return the list of all records.
        """
        return self.records

    def find_records_by_province(self, province):
        """
        Find and return all records matching a given province (case-insensitive).
        """
        return [r for r in self.records if r.province.lower() == province.lower()]

    def add_record(self, record):
        """
        Add a new Record object to the collection.
        """
        self.records.append(record)

    def edit_record(self, index, new_record):
        """
        Replace the Record at given index with new_record.
        Returns True if successful, False if index out of range.
        """
        if 0 <= index < len(self.records):
            self.records[index] = new_record
            return True
        else:
            return False

    def delete_record(self, index):
        """
        Delete the Record at given index.
        Returns True if successful, False if index out of range.
        """
        if 0 <= index < len(self.records):
            del self.records[index]
            return True
        else:
            return False
