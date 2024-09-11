from vehicle import Vehicles, Car , Motorcycle
class ParkingLot:
    def __init__(self, car_spots: int, motorcycle_spots: int):
        self.car_spots = car_spots
        self.motorcycle_spots = motorcycle_spots
        self.parked_vehicles = []

    def park_vehicle(self,vehicle: Vehicles):
            self.vehicle = vehicle
            self.Maxsize = self.car_spots + self.motorcycle_spots

            if isinstance(vehicle,Car):
                if self.parked_vehicles != self.car_spots:
                    self.parked_vehicles.append(vehicle)
                    print("Vehicle was parked successfully")
                else:
                    print("No space ")
            elif isinstance(vehicle,Motorcycle):
                if self.parked_vehicles != self.motorcycle_spots:
                    self.parked_vehicles.append(vehicle)
                    print("Motorcycle was successfully parked")
                elif self.parked_vehicles == self.motorcycle_spots:
                    for i in range(self.car_spots):
                        if self.parked_vehicles != self.car_spots:
                            self.parked_vehicles.append(vehicle)
                        print("Motorcycle was successfully parked")
                else:
                    print("No space")
            else:
                print("Park space is full")
    def remove_vehicle(self, license_plate: str):
            self.licence_plate = license_plate

    def get_parked_vehicles(self):
        if self.parked_vehicles != []:
            for id, item in enumerate(self.parked_vehicles):
                print(id,item)
        else:
            print("Park is empty")
                    