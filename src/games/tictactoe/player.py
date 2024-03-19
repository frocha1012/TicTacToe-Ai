from abc import ABC
from games.tictactoe.result import TicTacToeResult
from games.player import Player

class TicTacToePlayer(Player, ABC):
    def __init__(self, name):
        super().__init__(name)
        self.__stats = {result: 0 for result in TicTacToeResult}
        self.__num_games = 0

    def print_stats(self):
        num_wins = self.__stats[TicTacToeResult.WIN]
        win_rate = num_wins * 100.0 / self.__num_games if self.__num_games else 0
        print(f"Player {self.get_name()}: {num_wins}/{self.__num_games} wins ({win_rate} win rate)")

    def event_new_game(self):
        self.__num_games += 1

    def event_result(self, pos: int, result: TicTacToeResult):
        if pos == self.get_current_pos():
            self.__stats[result] += 1
