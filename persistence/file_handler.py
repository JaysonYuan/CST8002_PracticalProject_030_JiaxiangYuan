"""
persistence/file_handler.py
Handles reading and writing CSV data for Sr-90 dataset.
"""

import csv
from model.record import Record

CSV_COLUMNS = [
    "Sample Type/ Type d'échantillon", "Type", "Start Date/ Date de Début",
    "Stop Date/ Date de Fin", "Station Name/ Nom de Station", "Province",
    "Sr90 Activity/ Activité (Bq/L)", "Sr90 Error/ Erreur (Bq/L)",
    "Sr90 Activity/Calcium / Activité/Calcium  (Bq/g)"
]

def load_records_from_csv(file_path: str):
    records = []
    with open(file_path, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                record = Record(
                    row[CSV_COLUMNS[0]],
                    row[CSV_COLUMNS[1]],
                    row[CSV_COLUMNS[2]],
                    row[CSV_COLUMNS[3]],
                    row[CSV_COLUMNS[4]],
                    row[CSV_COLUMNS[5]],
                    row[CSV_COLUMNS[6]],
                    row[CSV_COLUMNS[7]],
                    row[CSV_COLUMNS[8]]
                )
                records.append(record)
            except Exception as e:
                print(f"Error parsing row: {e}")
    return records

def save_records_to_csv(file_path: str, records):
    with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(CSV_COLUMNS)
        for record in records:
            writer.writerow([
                record.sample_type,
                record.type_,
                record.start_date,
                record.stop_date,
                record.station_name,
                record.province,
                record.sr90_activity,
                record.sr90_error,
                record.sr90_calcium_activity
            ])
