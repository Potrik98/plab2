from paper_scissors_rock import *

if __name__ == "__main__":
    p1 = HistoricPlayer.HistoricPlayer()
    p2 = MostUsedPlayer.MostUsedPlayer()
    p3 = HistoricPlayer.HistoricPlayer(range=3)
    gc = GameController.GameController()
    gc.plot_game_series(p1, p3, 1000)
