class BMW:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "240 km/h"
class Ferrari:
    def fuel_type(self):
        return "Petrol (High Octane)"
    def max_speed(self):
        return "340 km/h"
def car_details(car):
    print(f"Fuel Type: {car.fuel_type()}")
    print(f"Max Speed: {car.max_speed()}")
    print("-" * 30)
bmw_car = BMW()
ferrari_car = Ferrari()
for car in (bmw_car, ferrari_car):
    car_details(car)