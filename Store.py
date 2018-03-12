# pylint: disable=print-statement

defective = "defective"
opened = "used"
forsale = "for sale"
sold = "sold"
unopen = "for sale"
tax = .10

class Store(object):
    def __init__(self, address, owner):
        self.products = []
        self.address =  address
        self.owner = owner
    def AddProduct(self, product):
        self.products.append(product)
        return self
    def RemoveProduct(self, product):
        for item in range(0, len(self.products)):
            if self.products[item].item_name == product.item_name:
                self.products.remove(self.products[item])
                break
        return self
    def Inventory(self):
        print "Amount of Inventory", len(self.products)
        print self.products
        for i in range(0, len(self.products)):
            print self.products[i].item_name
            print self.products[i].price
            print self.products[i].weight
            print self.products[i].brand
            print self.products[i].status
        return self

class Product(object):
    def __init__(self, price, item_name, weight, brand):
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
        print "Item Name:", self.item_name
        print "Price:", self.price
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        return self

store1 = Store("My Way", "James")
store2 = Store("Your Way", "Albert")

p1 = Product(10, "stereo", "5lbs", "sony")
p2 = Product(25, "microwave", "10lbs", "lg")
p3 = Product(400, "washer", "80lbs", "whirlpool")
p4 = Product(10, "dryer", "85lbs", "ge")

store1.AddProduct(p1).AddProduct(p2).RemoveProduct(p1).Inventory()
print "Store:", store1