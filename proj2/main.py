from paper_scissors_rock import *

if __name__ == "__main__":
    p1 = HistoricPlayer.HistoricPlayer()
    p2 = MostUsedPlayer.MostUsedPlayer()
    gc = GameController.GameController()
    gc.plot_game_series(p1, p2, 1000)
