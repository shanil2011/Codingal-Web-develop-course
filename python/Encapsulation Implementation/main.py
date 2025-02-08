class computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxprice(self, price):
        self.__maxprice = price

c = computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxprice(1000)
c.sell()
