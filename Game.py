from player import Player
from Spaces import Space


class Game:
    def __init__(self, players: list[Player], board: list[Space]):
        self.players = players
        self.board = board
        self.currentTurn = 0
        self.gameActive = True

    def movePlayer(self, player, roll):
        old_position = player.position
        board_size = len(self.board)

        new_position = (old_position + roll) % board_size

        if old_position + roll >= board_size:
            player.money += 1
            print(player.name, "passed GO and collected $1")

        player.position = new_position

    def takeTurn(self, player, roll):
        print("\n---", player.name, "rolls", roll, "---")
        self.movePlayer(player, roll)

        current_space = self.board[player.position]
        print(player.name, "moved to", current_space.name)

        print("\nCurrent player stats:")
        for current_player in self.players:
            current_space = self.board[current_player.position]
            print(
                current_player.name,
                "- money:", current_player.money,
                "- position:", current_player.position,
                "- space:", current_space.name
            )

    def playGame(self, rolls):
        for roll in rolls:
            player = self.players[self.currentTurn]
            self.takeTurn(player, roll)

            self.currentTurn = (self.currentTurn + 1) % len(self.players)

    def printResults(self):
        print("\nFINAL RESULTS")

        for player in self.players:
            current_space = self.board[player.position]
            print(
                player.name,
                "- money:", player.money,
                "- position:", player.position,
                "- space:", current_space.name
            )