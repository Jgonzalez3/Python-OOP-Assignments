# pylint: disable=print-statement
class MathDojo(object):
    def __init__(self, name):
        self.name = name
        self.total = 0
    def Add(self, *y):
        for data in range(0, len(y)):
            if type(y[data]) == int:
                self.total += int(y[data])
                print self.total
            if type(y[data]) == list:
                print self.total
                for val in range(0, len(y[data])):
                    self.total += y[data][val]
            if type(y[data]) == tuple:
                for val in range(0, len(y[data])):
                    self.total += y[data][val]
        return self
    def Subtract(self, *y):
        for data in range(0, len(y)):
            if type(y[data]) == int:
                self.total -= int(y[data])
            if type(y[data]) == list:
                for val in range(0, len(y[data])):
                    self.total -= y[data][val]
            if type(y[data]) == tuple:
                for val in range(0, len(y[data])):
                    self.total -= y[data][val]
        return self
    def Result(self):
        print self.total
        return self

md = MathDojo('part1')
md.Add(2).Add(2,5).Subtract(3,2)
print "part I result", md.Result()

md1 = MathDojo("part2")
md1.Add([1], 3,4).Add([3,5,7,8], [2,4.3,1.25]).Subtract(2, [2,3], [1.1,2.3])
print "part2 result", md1.Result()

md2 = MathDojo("part3")
md2.Add(1).Add([2,3], (2,3)).Subtract([2,3], (2,3))
print "part 3 result", md2.Result() 

### practice below for class above. Already copy and pasted in above class
a = ([1], (3,4), 2) # 10
total = 0
for data in range(0, len(a)):
    if type(a[data]) == int:
        total += int(a[data])
    if type(a[data]) == list:
        for val in range(0, len(a[data])):
            total += a[data][val]
    if type(a[data]) == tuple:
        for val in range(0, len(a[data])):
            total += a[data][val]
print total
