from paper_scissors_rock import *

if __name__ == "__main__":
    p1 = RandomPlayer.RandomPlayer()
    p2 = RandomPlayer.RandomPlayer()
    gc = GameController.GameController()
    gc.plot_game_series(p1, p2, 1000)
