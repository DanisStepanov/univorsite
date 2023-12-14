from game import *


def show():
    default_health, health = interface()
    game(default_health, health)

if __name__ == "__main__":
    show()
