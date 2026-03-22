from core.jsonLoader import loadBoard, loadRolls, createPlayers
from core.game import Game


def runGame(roll_file):
    print("\n-------------------------------------------------------")
    print("Running Game with rolls from roll file:", roll_file)
    print("-------------------------------------------------------")

    board = loadBoard()
    rolls = loadRolls(roll_file)
    players = createPlayers()

    game = Game(players, board)
    game.playGame(rolls)
    game.printResults()


if __name__ == "__main__":
    print("GAME START")
    runGame("data/rolls_1.json")
    runGame("data/rolls_2.json")