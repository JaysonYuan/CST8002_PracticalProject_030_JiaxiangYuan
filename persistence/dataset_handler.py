"""
dataset_handler.py
Parses milk dataset CSV and returns polymorphic RecordBase objects.

Author: Jiaxiang Yuan
"""

import csv
from typing import List
from model.record_base import RecordBase
from model.formatted_record_a import FormattedRecordA
from model.formatted_record_b import FormattedRecordB

def try_float(value: str) -> float:
    """
    Safely parse a float from a string. Returns 0.0 if conversion fails.

    :param value: String representation of a numeric value
    :return: Float value or 0.0 if conversion fails
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0

def load_milk_dataset(file_path: str) -> List[RecordBase]:
    """
    Load the milk dataset from a CSV file and return a list of polymorphic record objects.

    Alternates between FormattedRecordA and FormattedRecordB to demonstrate polymorphism.

    :param file_path: Path to the CSV dataset file
    :return: List of RecordBase (FormattedRecordA or FormattedRecordB) instances
    """
    records: List[RecordBase] = []

    try:
        # Use 'latin1' to support accented French characters
        with open(file_path, mode='r', encoding='latin1') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Skip header row

            for index, row in enumerate(reader):
                # Only use first 9 columns to prevent extra commas from breaking the format
                row = row[:9]

                # Ensure the row contains at least the required columns
                if len(row) < 7:
                    continue

                station = row[4].strip()
                province = row[5].strip()
                start_date = row[2].strip()
                sr90_activity = try_float(row[6])

                record_id = f"{index:03d}"  # Zero-padded 3-digit ID
                name = f"{station}-{province}-{start_date}"
                value = sr90_activity

                # Alternate between format A and B
                if index % 2 == 0:
                    record = FormattedRecordA(record_id, name, value)
                else:
                    record = FormattedRecordB(record_id, name, value)

                records.append(record)

    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
    except Exception as e:
        print(f"[ERROR] Exception during loading: {e}")

    return records
