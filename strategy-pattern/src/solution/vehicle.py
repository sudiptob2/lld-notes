from drive_strategy import IDriveStrategy, NormalDrive, SportDrive


class Vehicle:
    """Vehicle Base class."""
    drive_strategy: IDriveStrategy

    def __init__(self, drive_strategy) -> None:
        self.drive_strategy = drive_strategy

    def drive(self):
        """Drive method implementation using injected strategy"""
        self.drive_strategy.drive()


class NormalVehicle(Vehicle):
    """Normal extends Vehicle."""

    def __init__(self) -> None:
        super().__init__(NormalDrive())


class OffRoadVehicle(Vehicle):
    """OffRoadVehicle extends Vehicle."""

    def __init__(self) -> None:
        super().__init__(SportDrive())


class SportVehicle(Vehicle):
    """SportVehicle extends Vehicle."""

    def __init__(self) -> None:
        super().__init__(SportDrive())
