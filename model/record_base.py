"""
record_base.py
Defines the base class for records to demonstrate polymorphism.

Author: Jiaxiang Yuan
"""

from abc import ABC, abstractmethod

class RecordBase(ABC):
    """
    Abstract base class for records, used to demonstrate polymorphism.
    """

    def __init__(self, id: str, name: str, value: float):
        self.id = id
        self.name = name
        self.value = value

    @abstractmethod
    def display(self) -> str:
        """
        Abstract method to return a string representation of the record.

        :return: Formatted string.
        """
        pass
