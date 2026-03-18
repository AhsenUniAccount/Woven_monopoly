from player import Player
from Spaces import Space, Go, Property

# goal of class, contains the gamestate and al of the rules which occur and functions involving a turn 


class Game:
     def __init__(self, players: list[Player], board: list[Space], Turns): #lock the datatypes?
          self.Players = Players
          self.Properties = Properites
          self.Turns = Turns
          self.gameActive = True

     def __str__(self):
            return f"{self.Players})"



def turn(self, roll: list[int])-> None:
      """
      for 1 player, executues there turn 
      roll the dice 
      move player from current position to new position 
      did you pass go ?
          -> yes give money
      is property owned?
          yes -> pay rent 
          no -> buy property 

     is any player bankrupt?
          -> if yes end game 
          -> if no, end end the turn
      """




def rentPayment(renter: Player, owner: Player, property: Property):
      renter.money -= property.rent
      owner.money += property.rent


def endGame(self) -> None
     
      """
      out of the players, find the name of the player with the most money
      if multiple players have the same amount of money, the game is a tie 
      """



      
      