"""
model/record.py
Data model for Sr-90 dataset.

Program by Jiaxiang Yuan
"""

class Record:
    def __init__(self, sample_type, type_, start_date, stop_date,
                 station_name, province, sr90_activity,
                 sr90_error, sr90_calcium_activity):
        self.sample_type = sample_type
        self.type_ = type_
        self.start_date = start_date
        self.stop_date = stop_date
        self.station_name = station_name
        self.province = province
        self.sr90_activity = sr90_activity
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
