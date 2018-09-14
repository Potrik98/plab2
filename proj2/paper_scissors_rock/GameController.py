from paper_scissors_rock.Player import Player
from paper_scissors_rock.RandomPlayer import RandomPlayer
from paper_scissors_rock.SimpleGame import SimpleGame
from paper_scissors_rock.GameSeries import GameSeries
import matplotlib.pyplot as plt

class GameController:
    def __init__(self, recent_score_weight=0.125):
        self._recent_score_weight = recent_score_weight

    def play_single_game(self, player1: Player, player2: Player) -> None:
        game = SimpleGame(player1, player2)
        game.do_game()
        print(game)

    def plot_game_series(self, player1: Player, player2: Player, number_of_games: int) -> None:
        game_series = GameSeries(player1, player2, number_of_games)
        game_series.do_games()
        results = game_series.get_results()
        assert len(results) == number_of_games
        player1_results, player2_results = self._process_results(results)
        self._plot_results(player1_results, player2_results)
    
    def _process_results(self, results: [int]) -> ([[float]], [[float]]):
        number_of_games = len(results)
        player1_total_score = [0] * (number_of_games + 1)
        player2_total_score = [0] * (number_of_games + 1)
        player1_recent_score = [0] * (number_of_games + 1)
        player2_recent_score = [0] * (number_of_games + 1)
        for i in range(number_of_games):
            player1_total_score[i + 1] = (player1_total_score[i] * i + results[i]) / (i + 1)
            player2_total_score[i + 1] = (player2_total_score[i] * i - results[i]) / (i + 1)
            player1_recent_score[i + 1] = player1_recent_score[i] * (1 - self._recent_score_weight) \
                + self._recent_score_weight * results[i]
            player2_recent_score[i + 1] = player2_recent_score[i] * (1 - self._recent_score_weight) \
                - self._recent_score_weight * results[i]
        #return ([player1_total_score, player1_recent_score], [player2_total_score, player2_recent_score])
        return ([player1_total_score], [player2_total_score])
    
    def _plot_results(self, player1_results: [[float]], player2_results: [[float]]) -> None:
        assert len(player1_results) == len(player2_results)
        for r1, r2, i in zip(player1_results, player2_results, range(len(player1_results))):
            p1, = plt.plot(r1, label="Player 1, Series %d" % i)
            p2, = plt.plot(r2, label="Player 2, Series %d" % i)
            plt.legend(handles=[p1, p2])
        plt.xlabel("games")
        plt.ylabel("score")
        plt.show()
