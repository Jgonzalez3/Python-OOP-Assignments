# pylint: disable=print-statement

class Patient(object):
    def __init__(self, pid, name, allergies):
        self.pid = pid
        self.name = name
        self.allergies = allergies
        self.bed_num = None
    def display(self):
        print self.pid, type(self.pid)
        print self.name, type(self.name)
        print self.allergies, type(self.allergies)
        print self.bed_num, type(self.bed_num)
        return self
class Hospital(object):
    def __init__(self, hsname, capacity):
        self.patients = []
        self.hsname = hsname
        self.capacity = capacity # max capacity
    def Add(self, patient):
        # assign patient a bed number. if at capacity do not admit patient and return a message
        if self.capacity == 0:
            print "Cannot Admit at Full Capacity"
        else:
            self.patients.append(patient)
            for i in range(0, len(self.patients)):
                if self.patients[i].bed_num == None:
                    self.patients[i].bed_num = self.capacity
            self.capacity -= 1
            return self
    def Discharge(self, patient):
        if self.capacity == 0:
            print "Empty! No one to Discharge"
        else:
            for i in range(0, len(self.patients)):
                if self.patients[i].pid == patient.pid:
                    self.patients.remove(self.patients[i])
                    self.patients[i].bed_num = None
                    break
            self.capacity += 1
            return self
    def Display(self):
        print "Capacity", self.capacity
        for i in range(0, len(self.patients)):
            print self.patients[i].name
            print "allergies", self.patients[i].allergies
            print "bed num", self.patients[i].bed_num
        return self

p1 = Patient(1, "aaron", ["bees","olives"])
# print "p1", p1.display()
p2 = Patient(2, "james", ["pollen","lactose"])
p3 = Patient(3, "phillip", ["sleep","sun"])
p4 = Patient(4, "wess", ["gluten","nuts"])
p5 = Patient(5, "tom", "cotton")
p6 = Patient(6, "jaun", "penicllin")
p7 = Patient(7, "steve", "nuts")

h1 = Hospital("Sutter Gold", 4)
print h1.Display()
print h1.Add(p1).Add(p2).Add(p3).Add(p4).Add(p5).Display()
# print "Hospital", h1.Add(p1).Add(p2).Add(p3).Add(p4).Add(p5).Discharge(p1).Display()
