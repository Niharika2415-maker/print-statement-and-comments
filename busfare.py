class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100  # Default fare
class Bus(Vehicle):
    def fare(self):
        # Get base fare from Vehicle class
        total_fare = super().fare()
        # Add 10% maintenance charge
        total_fare += total_fare * 0.10
        return total_fare
# Create an object of Bus
school_bus = Bus("School Volvo", 12, 50)
# Display total fare
print(f"Total Bus fare is: INR {school_bus.fare()}")