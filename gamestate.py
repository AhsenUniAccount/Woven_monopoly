from player import Player
from Spaces import Space, Go, Property



class gamestate:
     def __init__(self, Players, Properites, Turns): #lock the datatypes?
          self.Players = Players
          self.Properties = Properites
          self.Turns = Turns

     def __str__(self):
            return f"{self.Players})"


#function must print each plahyers current postion, show which properties they own, and how much each player owns