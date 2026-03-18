class Player:
    def __init__(self,name):
        self.name = name
        self.money = 0    
        self.position = 0  
        self.properties = []

    def __str__(self):
        propertyNames = [p.name for p in self.properties]
        return f"Player:{self.name} has balance = {self.money}, is in position = {self.position}\n owned properties={propertyNames})"