# pylint: disable=print-statement

class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        if self.miles <= 0:
            self.miles = 0
        return self

bike1 = Bike(350, "20mph", 0)
bike2 = Bike(550, "25mph", 0)
bike3 = Bike(650, "30mph", 0)

bike1.ride().ride().ride().reverse().displayinfo()
print bike1

bike2.ride().ride().reverse().reverse().displayinfo()
print bike2

bike3.ride().ride().reverse().reverse().displayinfo()
print bike3.reverse().reverse().reverse().displayinfo()
