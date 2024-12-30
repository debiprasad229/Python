# single inheritance
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
# multiple inheritance
class parent1():
    def assign_str1(self,str1):
        self.str1=str1
    def show_str1(self):
        print(self.str1)
class parent2():
    def assign_str2(self,str2):
        self.str2=str2
    def show_str2(self):
        print(self.str2)
class derived(parent1,parent2):
    def assign_str3(self,str3):
        self.str3=str3
    def show_str3(self):
        print(self.str3)

d1=derived()
d1.assign_str1("hello")
d1.assign_str2("hi")
d1.assign_str3("bye")
d1.show_str1()
d1.show_str2()
d1.show_str3()
# multilevel inheritance
class parent():
    def assign_name(self,name):
        self.name=name
    def show_name(self):
        print(self.name)
class child(parent):
    def assign_age(self,age):
        self.age=age
    def show_age(self):
        print(self.age)
class grandchild(child):
    def assign_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        print(self.gender)
g1=grandchild()
g1.assign_name("sai")
g1.assign_age(20)
g1.assign_gender("male")
g1.show_name()
g1.show_age()
