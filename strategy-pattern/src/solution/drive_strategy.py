from abc import ABCMeta, abstractmethod


class IDriveStrategy(metaclass=ABCMeta):
    """Abstract Factory Interface"""

    @abstractmethod
    def drive(self):
        """Abstract drive method"""


class NormalDrive(IDriveStrategy):
    """Normal Drive class."""

    def drive(self):
        """Implements normal drive capability."""
        print("This is a normal drive")


class SportDrive(IDriveStrategy):
    """Sport Drive class."""

    def drive(self):
        """Implements sport drive capability."""
        print("I drive as max speed of 200km/h")
