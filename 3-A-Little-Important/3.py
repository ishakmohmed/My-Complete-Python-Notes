# property allows us to get/set value of attribute

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    # price = property(get_price, set_price)
    # all these args are optional: fn1- get, fn2- set, fn3- del, fn4- documentation
    # here, I commented out the code cause we're just gonna use the @property decorator


product = Product(50)
product.price = 10
# now if you set to negative value, it'll throw exception!

# ALL OF THESE CODES JUST TO CREATE A PROPERTY WITH VALIDATION
