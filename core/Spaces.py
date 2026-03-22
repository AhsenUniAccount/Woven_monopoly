# define the spaces here

class Space:
    def __init__(self,name: str,position: int): #lock the datatypes?
        self.name = name
        self.position = position

class Go(Space):
        def __init__(self, name: str, position: int):
            super().__init__(name, position)

class Property(Space):
        def __init__(self, name: str, position: int, price: int, colour: str):
            super().__init__(name, position)
            self.price = price
            self.colour = colour
            self.rent = price #change later ?
            self.owner = None
        def get_rent(self):
            return self.price
        




            
