class pharmacy_items:
    # class properties
    available = {}
    needed = {}
    #
    #
    def __init__(self, name, quantity, expiration, price):
        self.name = name
        self.cuantity = quantity
        self.expiration = expiration
        self.price = price
        

                
    @classmethod
    def sell(cls, name):
        pass
