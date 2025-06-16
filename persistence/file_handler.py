"""
persistence/file_handler.py
Handles file input/output for Sr-90 records.

Program by Jiaxiang Yuan
"""

import csv
import uuid
from model.record import Record

def load_records_from_csv(file_path, max_records=100):
    records = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                if i >= max_records:
                    break
                record = Record(
                    sample_type=row['Sample Type/ Type d\'échantillon'],
                    type_=row['Type'],
                    start_date=row['Start Date/ Date de Début'],
                    stop_date=row['Stop Date/ Date de Fin'],
                    station_name=row['Station Name/ Nom de Station'],
                    province=row['Province'],
                    sr90_activity=row['Sr90 Activity/ Activité (Bq/L)'],
                    sr90_error=row['Sr90 Error'],  
                    sr90_calcium_activity=row['Sr90 Calcium Activity'] 
                )
                records.append(record)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return records

def save_records_to_csv(file_path, records):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'Sample Type/ Type d\'échantillon',
                'Type',
                'Start Date/ Date de Début',
                'Stop Date/ Date de Fin',
                'Station Name/ Nom de Station',
                'Province',
                'Sr90 Activity/ Activité (Bq/L)',
                'Sr90 Error',
                'Sr90 Calcium Activity'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for r in records:
                writer.writerow({
                    'Sample Type/ Type d\'échantillon': r.sample_type,
                    'Type': r.type_,
                    'Start Date/ Date de Début': r.start_date,
                    'Stop Date/ Date de Fin': r.stop_date,
                    'Station Name/ Nom de Station': r.station_name,
                    'Province': r.province,
                    'Sr90 Activity/ Activité (Bq/L)': r.sr90_activity,
                    'Sr90 Error': r.sr90_error,
                    'Sr90 Calcium Activity': r.sr90_calcium_activity
                })
        print(f"Saved {len(records)} records to {file_path}")
    except Exception as e:
        print(f"Error saving file: {e}")

def generate_uuid_filename():
    return f"output_{uuid.uuid4()}.csv"
