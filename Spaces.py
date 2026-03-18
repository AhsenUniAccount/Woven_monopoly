# define the spaces here

class Space:
    def __init__(self,name,position): #lock the datatypes?
        self.name = name
        self.position = position

class Go(Space):
        def __init__(self, name, position):
            super().__init__(name, position)

class Property(Space):
        def __init__(self, name, position, price, colour, rent):
            super().__init__(name, position)
            self.price = price
            self.rent = rent
            self.colour = colour
            self.rent = price #change later ?
            self.owner = None
        




            
