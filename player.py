class Player:
    def __init__(self,name: str):
        self.name = name
        self.money = 16    
        self.position = 0  
        self.properties = []

    @property
    def bankrupt(self) -> bool:
        return self.money < 0

    def __str__(self):
        propertyNames = [p.name for p in self.properties]
        return f"Player:{self.name} has balance = {self.money}, is in position = {self.position}\n owned properties={propertyNames})"