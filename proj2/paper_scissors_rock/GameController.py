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
        total_score = [0] * (number_of_games + 1)
        player1_win = [0] * (number_of_games + 1)
        player2_win = [0] * (number_of_games + 1)
        player1_wr = [0] * (number_of_games + 1)
        player2_wr = [0] * (number_of_games + 1)
        for i in range(1, number_of_games):
            total_score[i + 1] = total_score[i] + results[i]
            total_score[i] = total_score[i] / i
            player1_win[i + 1] = player1_win[i]
            player2_win[i + 1] = player2_win[i]
            if results[i] == 1:
                player1_win[i + 1] += 1
            elif results[i] == -1:
                player2_win[i + 1] += 1
            total_wins = player1_win[i + 1] + player2_win[i + 1]
            if total_wins > 0:
                player1_wr[i + 1] = player1_win[i + 1] / total_wins
                player2_wr[i + 1] = player2_win[i + 1] / total_wins
        total_score[-1] = total_score[-1] / number_of_games

        return ([total_score, player1_wr], [[-a for a in total_score], player2_wr],)
    
    def _plot_results(self, player1_results: [[float]], player2_results: [[float]]) -> None:
        assert len(player1_results) == len(player2_results)
        labels = ["Score", "Win rate"]
        h = []
        for r1, r2, i in zip(player1_results, player2_results, range(len(player1_results))):
            p1, = plt.plot(r1, label="Player 1 %s" % labels[i])
            p2, = plt.plot(r2, label="Player 2 %s" % labels[i])
            h.append(p1)
            h.append(p2)
        plt.legend(handles=h)
        plt.xlabel("games")
        plt.ylabel("score")
        plt.show()
