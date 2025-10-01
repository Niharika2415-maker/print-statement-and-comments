class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed= max_speed
        self.mileage= mileage
model= vehicle(123,45)
print("model max speed",model.max_speed)
print("model mileage",model.mileage)
