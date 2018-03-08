# pylint: disable=print-statement

class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def Walk(self):
        self.health -= 1
        return self
    def Run(self):
        self.health -= 5
        return self
    def DisplayHealth(self):
        print self.health
        return self
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150) # name is here since name is in __init__ function above, here health is not needed as attribute since health not a parameter of __init__ function for this class 
        self.name = name
    def Pet(self):
        self.health += 5
        return self
class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
        self.name = name
    def Fly(self):
        self.health -= 10
        return self
    def DisplayHealth(self):
        super(Dragon, self).DisplayHealth()
        print "I am a Dragon"
        return self

animal1 = Animal("Juan", 100)
print animal1.Walk().Walk().Walk().Run().Run().DisplayHealth()

dog1 = Dog("bernie")
dog1.Walk().Walk().Walk().Pet().Pet().DisplayHealth()

dragon1 = Dragon("Snake")
dragon1.Fly().DisplayHealth()

animal2 = Animal("rust", 20)
print animal2.DisplayHealth()
