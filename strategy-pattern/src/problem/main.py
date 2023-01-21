from normal_vehicle import NormalVehicle
from offroad_vehicle import OffRoadVehicle
from sport_vehicle import SportVehicle


def test():
    offroad_vehicle = OffRoadVehicle()
    sport_vehicle = SportVehicle()
    normal_vehicle = NormalVehicle()

    offroad_vehicle.drive()
    normal_vehicle.drive()
    sport_vehicle.drive()


if __name__ == "__main__":
    test()
