from jsonLoader import loadBoard, loadPlayers
from Spaces import Go, Property
from player import Player


def print_board():
    board = loadBoard() ## loads the board
    players = loadPlayers() ## loads pre determined 4 players

    for space in board:
        if isinstance(space, Go):
            print(f"Go: name={space.name}, position={space.position}")
        elif isinstance(space, Property):
            print(
                f"Property: name={space.name}, position={space.position}, "
                f"price={space.price}, rent={space.rent}, colour={space.colour}"
            )

if __name__ == "__main__":
    print_board()
