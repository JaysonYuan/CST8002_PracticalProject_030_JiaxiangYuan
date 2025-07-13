from model.record_base import RecordBase

class FormattedRecordA(RecordBase):
    """
    Displays the record in standard dash-separated format.
    """

    def display(self):
        return f"{self.id} - {self.name} - ${self.value:.2f}"
