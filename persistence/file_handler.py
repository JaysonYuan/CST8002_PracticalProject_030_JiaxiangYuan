"""
persistence/file_handler.py
Handles file input/output for Sr-90 Milk Records.

Program by Jiaxiang Yuan
"""

import csv
import uuid
from model.record import Record

def load_records_from_csv(file_path, max_records=100):
    """
    Load records from CSV file, up to max_records, using latin-1 encoding.
    Returns a list of Record objects.
    """
    records = []
    try:
        with open(file_path, newline='', encoding='latin-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                if i >= max_records:
                    break
                record = Record(
                    sample_type=row.get("Sample Type/ Type d'échantillon", "").strip(),
                    type_=row.get("Type", "").strip(),
                    start_date=row.get("Start Date/ Date de Début", "").strip(),
                    stop_date=row.get("Stop Date/ Date de Fin", "").strip(),
                    station_name=row.get("Station Name/ Nom de Station", "").strip(),
                    province=row.get("Province", "").strip(),
                    sr90_activity=row.get("Sr90 Activity/ Activité (Bq/L)", "").strip(),
                    sr90_error=row.get("Sr90 Error/ Erreur (Bq/L)", "").strip(),
                    sr90_calcium_activity=row.get("Sr90 Activity/Calcium / Activité/Calcium  (Bq/g)", "").strip()
                )
                records.append(record)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
    return records

def save_records_to_csv(file_path, records):
    """
    Save list of Record objects to CSV file with UTF-8 encoding.
    """
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                "Sample Type/ Type d'échantillon",
                "Type",
                "Start Date/ Date de Début",
                "Stop Date/ Date de Fin",
                "Station Name/ Nom de Station",
                "Province",
                "Sr90 Activity/ Activité (Bq/L)",
                "Sr90 Error/ Erreur (Bq/L)",
                "Sr90 Activity/Calcium / Activité/Calcium  (Bq/g)"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for r in records:
                writer.writerow({
                    "Sample Type/ Type d'échantillon": r.sample_type,
                    "Type": r.type_,
                    "Start Date/ Date de Début": r.start_date,
                    "Stop Date/ Date de Fin": r.stop_date,
                    "Station Name/ Nom de Station": r.station_name,
                    "Province": r.province,
                    "Sr90 Activity/ Activité (Bq/L)": r.sr90_activity,
                    "Sr90 Error/ Erreur (Bq/L)": r.sr90_error,
                    "Sr90 Activity/Calcium / Activité/Calcium  (Bq/g)": r.sr90_calcium_activity
                })
        print(f"Saved {len(records)} records to {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

def generate_uuid_filename():
    """
    Generate a unique filename using UUID.
    """
    return f"output_{uuid.uuid4()}.csv"
