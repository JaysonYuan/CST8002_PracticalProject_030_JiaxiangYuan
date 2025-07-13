from model.record_base import RecordBase

class FormattedRecordB(RecordBase):
    """
    Displays the record in uppercase with a label format.
    """

    def display(self):
        return f"[ID: {self.id}] {self.name.upper()} = ${self.value:.2f}"
