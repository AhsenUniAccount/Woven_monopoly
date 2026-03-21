from jsonLoader import loadBoard, loadRolls, createPlayers
from Spaces import Go, Property
from Game import Game


from jsonLoader import loadBoard, loadRolls, createPlayers
from Game import Game


def runGame(roll_file):
    print("\n------------------")
    print("RUNNING GAME WITH", roll_file)
    print("==========================")

    board = loadBoard()
    rolls = loadRolls(roll_file)
    players = createPlayers()

    game = Game(players, board)
    game.playGame(rolls)
    game.printResults()


if __name__ == "__main__":
    print("_________________\n\n\n\nstart------------")
    runGame("rolls_2.json")