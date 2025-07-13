class RecordBase:
    """
    Base class for records, used to demonstrate polymorphism.
    """

    def __init__(self, id, name, value):
        self.id = id
        self.name = name
        self.value = value

    def display(self):
        """
        Abstract method to display a record.
        """
        raise NotImplementedError("Subclasses must implement the display method")
