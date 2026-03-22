import json
from typing import List
from core.Spaces import Space, Go, Property
from core.player import Player

"""
loads the preset board and the rolls from their respective files
"""
def loadBoard() -> List[Space]:
    boardSpaces = []

    with open("data/board.json", "r", encoding="utf-8") as f:
        spaceString = f.read()

    spaceList = json.loads(spaceString)

    for current, space in enumerate(spaceList):
        spaceType = space["type"]

        if spaceType == "property":
            boardSpaces.append(
                Property(
                    name=space["name"],
                    position=current,
                    price=space["price"],
                    colour=space["colour"]
                )
            )
        elif spaceType == "go":
            boardSpaces.append(
                Go(name=space["name"], position=current)
            )
        else:
            raise ValueError(f"space error {spaceType}")

    return boardSpaces


def loadRolls(filename: str) -> List[int]:
    with open(filename, "r", encoding="utf-8") as f:
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