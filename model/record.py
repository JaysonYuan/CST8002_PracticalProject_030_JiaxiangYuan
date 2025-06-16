"""
model/record.py
Data model for Sr-90 dataset.

Program by Jayson YUAN
"""

class Record:
    def __init__(self, sample_type, type_, start_date, stop_date,
                 station_name, province, sr90_activity,
                 sr90_error, sr90_calcium_activity):
        self.sample_type = sample_type  # Sample Type/ Type d'échantillon
        self.type_ = type_              # Type
        self.start_date = start_date    # Start Date/ Date de Début
        self.stop_date = stop_date      # Stop Date/ Date de Fin
        self.station_name = station_name  # Station Name/ Nom de Station
        self.province = province        # Province
        self.sr90_activity = sr90_activity  # Sr90 Activity/ Activité (Bq/L)
        self.sr90_error = sr90_error
        self.sr90_calcium_activity = sr90_calcium_activity

    def __str__(self):
        return (
            f"Sample Type: {self.sample_type}, Type: {self.type_}, "
            f"Start: {self.start_date}, Stop: {self.stop_date}, "
            f"Station: {self.station_name}, Province: {self.province}, "
            f"Sr-90 Activity: {self.sr90_activity}, Error: {self.sr90_error}, "
            f"Calcium Activity: {self.sr90_calcium_activity}"
        )
