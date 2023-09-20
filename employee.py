class Retailitem:

  def __init__(self, itemdescription, unitsininventory, price):
    self.itemdescription = itemdescription
    self.unitsininventory = unitsininventory
    self.price = price

Item1 = Retailitem("Jacket", 12, 59.95)

Item2 = Retailitem("Designer Jeans", 40, 34.95)

Item3 = Retailitem("Shirt", 20, 24.95)
