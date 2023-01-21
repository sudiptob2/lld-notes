from vehicle import Vehicle


class SportVehicle(Vehicle):
    """SportVehicle extends Vehicle."""

    def drive(self):
        """Provides own implementation of the base drive."""
        print("I drive as max speed of 200km/h")  # Duplicated code
