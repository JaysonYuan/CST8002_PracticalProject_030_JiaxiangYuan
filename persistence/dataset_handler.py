"""
dataset_handler.py
Parses milk dataset CSV and returns polymorphic RecordBase objects.
Supports pie chart data structure.

Author: Jiaxiang Yuan
"""

import csv
from typing import List
from model.record_base import RecordBase
from model.formatted_record_a import FormattedRecordA
from model.formatted_record_b import FormattedRecordB

DATASET_PATH = "data/milk_dataset.csv"

def try_float(value: str) -> float:
    """
    Safely parse a float from a string. Returns 0.0 if conversion fails.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0

def load_milk_dataset(file_path: str) -> List[RecordBase]:
    """
    Load the milk dataset and return a list of RecordBase objects.
    Alternates between FormattedRecordA and FormattedRecordB for polymorphism.
    """
    records: List[RecordBase] = []

    try:
        with open(file_path, mode='r', encoding='latin1') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)

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

def get_raw_data() -> List[dict]:
    """
    Reload dataset and return a list of dictionaries for charting.
    Each dict contains id, name, value, station, province, and start_date.
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
