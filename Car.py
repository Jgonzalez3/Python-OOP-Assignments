# pylint: disable=print-statement

class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax):
        self.price = price
        if price > 10000:
            self.tax = .15
        elif price <= 10000:
            self.tax = .12
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.displayall()
    def displayall(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax
        return self

car1 = Car(15000, "100mph", "Full", "35mpg", "4000")
car2 = Car(8000, "70mph", "Quarter Tank", "25mpg", "60000")
car3 = Car(20000, "120mph", "Full Tank", "30mpg", "20000")
car4 = Car(9000, "100mph", "Half Tank", "35mpg", "80000")
car5 = Car(2000, "65mph", "Empty", "25mpg", "75000")
car6 = Car(10000, "90mph", "Half Tank", "30mpg", "30000")

print car1, car2, car3, car4, car4, car5, car6