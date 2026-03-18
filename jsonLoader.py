
from Spaces import Space, Go, Property
from typing import List
from player import Player
import json

def loadBoard() -> List[Space]:

    boardSpaces = []

    with open("board.json", "r",encoding="utf-8") as f:
        spaceString = f.read()

    spaceList = json.loads(spaceString)

    for current, space in enumerate(spaceList):
        spaceType = space["type"]
        if spaceType == "property":
            boardSpaces.append(
                Property(
                    name = space["name"],
                    position = current,
                    price = space["price"],
                    rent = space["price"],#changer later?
                    colour = space["colour"]
                )
            )
        elif spaceType == "go":
            boardSpaces.append(Go(name=space["name"], position = current))#hard code?
        else:
            raise ValueError(f"space error {spaceType}")

    return boardSpaces

def loadRolls() -> List[int]:
    rolls = []

    with open("rolls_1", "r",encoding="utf-8") as f:
        rollString = f.read()

    rolls = json.loads(rollString)

    return rolls


def createPlayers() -> List[Player]:
    players = []
    players.append(Player("Peter"))
    players.append(Player("Billy"))
    players.append(Player("Charlotte"))
    players.append(Player("Sweedal"))
    return players
    







