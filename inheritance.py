class vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("i am a vehicle")
        print("the mileage is",self.mileage)
        print("the cost is", self.cost)

V1=vehicle(344,33343)
V1.show_details()

class car(vehicle):
    def show_car_details(self):
        print("I am a car")
c1=car(112,2200)
c1.show_details()
c1.show_car_details()
# over-riding method
class car(vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp
    def show_car_details(self):
        print("the no of tyres are",self.tyres)
        print("the hp is",self.hp)
c1= car(500,60000,4,200)
c1.show_details()
c1.show_car_details()
