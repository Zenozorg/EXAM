from parking_lot import ParkingLot
import vehicle 
def main():
    parking_lot = ParkingLot(car_spots = 3 , motorcycle_spots=1)
    car1 = vehicle.Car("ABC123")
    car2 = vehicle.Car("DEF456")
    car3 = vehicle.Car("GHI789")
    motorcycle1 = vehicle.Motorcycle("MOTO1")
    motorcycle2 = vehicle.Motorcycle("MOTO2")
    parking_lot.park_vehicle(car1)
    parking_lot.park_vehicle(car2)
    parking_lot.park_vehicle(motorcycle1)
    parking_lot.park_vehicle(motorcycle2)
    parking_lot.park_vehicle(car3)
    parking_lot.get_parked_vehicles()
    parking_lot.remove_vehicle("ABC123")
    parking_lot.get_parked_vehicles()

if __name__ in "__main__":
    main()