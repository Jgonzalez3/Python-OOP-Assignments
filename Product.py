# pylint: disable=print-statement

defective = "defective"
opened = "used"
forsale = "for sale"
sold = "sold"
unopen = "for sale"
tax = .10

class Product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = forsale
    def Sell(self, tax):
        self.status = sold
        self.AddTax(tax)
        return self
    def AddTax(self, tax):
        self.tax = tax
        self.price = self.price * (1 + tax)
        return self
    def Return(self, reason):
        self.reason = reason
        if self.reason == defective:
            self.status = "defective"
            self.price = 0
        if self.reason == unopen: #returned in box
            self.status = "for sale"
        if self.reason == opened: # box opened
            self.status = "used"
            self.price = self.price - (self.price * .2)
        return self
    def DisplayInfo(self):
        print "  "
        print "Item Name:", self.item_name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        return self

product1 = Product(10, "stereo", "5lbs", "sony", "status")
product2 = Product(25, "microwave", "10lbs", "lg", "status")
product3 = Product(400, "washer", "80lbs", "whirlpool", "status")
product4 = Product(10, "dryer", "85lbs", "ge", "status")


product1.Sell(tax).DisplayInfo()

product2.Return(unopen).DisplayInfo()

product3.Return(opened).DisplayInfo()

product4.Return(defective).DisplayInfo()
print product1, product2, product3, product4