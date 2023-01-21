from vehicle import NormalVehicle, OffRoadVehicle, SportVehicle


def test():
    offroad_vehicle = OffRoadVehicle()
    sport_vehicle = SportVehicle()
    normal_vehicle = NormalVehicle()

    offroad_vehicle.drive()
    normal_vehicle.drive()
    sport_vehicle.drive()


if __name__ == "__main__":
    test()
