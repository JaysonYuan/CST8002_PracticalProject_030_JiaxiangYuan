"""
dataset_handler.py
Parses milk dataset CSV and returns polymorphic RecordBase objects.

Author: Jiaxiang Yuan
"""

import csv
import os
from typing import List
from model.record_base import RecordBase
from model.formatted_record_a import FormattedRecordA
from model.formatted_record_b import FormattedRecordB

DATASET_PATH = os.path.join(
    os.path.dirname(__file__), "..", "dataset", "nms_strontium90_milk_ssn_strontium90_lait.csv"
)

def try_float(value: str) -> float:
    """
    Safely parse a float from a string. Returns 0.0 if conversion fails.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0

def load_milk_dataset(file_path: str = DATASET_PATH) -> List[RecordBase]:
    """
    Load the milk dataset from a CSV file and return a list of polymorphic record objects.

    Alternates between FormattedRecordA and FormattedRecordB to demonstrate polymorphism.
    """
    records: List[RecordBase] = []

    try:
        # Use 'latin1' to support accented French characters
        with open(file_path, mode='r', encoding='latin1') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Skip header row

            for index, row in enumerate(reader):
                row = row[:9]
                if len(row) < 7:
                    continue

                station = row[4].strip()
                province = row[5].strip()
                start_date = row[2].strip()
                sr90_activity = try_float(row[6])

                record_id = f"{index:03d}"
                name = f"{station}-{province}-{start_date}"
                value = sr90_activity

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

def get_raw_data():
    """
    Reload dataset and return a list of dictionaries for charting.
    """
    raw_records = load_milk_dataset(DATASET_PATH)

    expanded_data = []
    for record in raw_records:
        try:
            station, province, start_date = record.name.split('-')
        except ValueError:
            station = province = start_date = "Unknown"

        expanded_data.append({
            "id": record.id,
            "name": record.name,
            "value": record.value,
            "station": station,
            "province": province,
            "start_date": start_date
        })

    return expanded_data
