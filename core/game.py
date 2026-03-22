from core.player import Player
from core.Spaces import Space, Go, Property


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

        player.position = new_position

    def hasMonopoly(self, owner, colour):
        colour_properties = []

        for space in self.board:
            if isinstance(space, Property) and space.colour == colour:
                colour_properties.append(space)

        for property_space in colour_properties:
            if property_space.owner != owner:
                return False

        return True

    def landed(self, player):
        space = self.board[player.position]

        if isinstance(space, Go):
            print(player.name, "landed on GO")

        elif isinstance(space, Property):
            if space.owner is None:
                print(player.name, "is buying", space.name)
                space.owner = player
                player.money -= space.price
                player.properties.append(space)

            elif space.owner == player:
                print(player.name, "landed on their own property", space.name)

            else:
                rent_to_pay = space.rent

                if self.hasMonopoly(space.owner, space.colour):
                    rent_to_pay = rent_to_pay * 2

                print(player.name, "needs to pay rent to", space.owner.name)
                print("Rent is", rent_to_pay)

                player.money -= rent_to_pay
                space.owner.money += rent_to_pay

    def takeTurn(self, player, roll):
        print("\n---", player.name, "rolls", roll, "---")
        self.movePlayer(player, roll)
        print(player.name, "moved to", self.board[player.position].name)
        self.landed(player)

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

            if player.money <= 0:
                print(player.name, "is bankrupt")
                self.gameActive = False
                break

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

        winner = self.getWinner()
        print("\nWINNER:", winner.name)

    def getWinner(self):
        winner = self.players[0]

        for player in self.players:
            if player.money > winner.money:
                winner = player

        return winner