from games.tictactoe.player import TicTacToePlayer
from games.tictactoe.state import TicTacToeState
from games.game_simulator import GameSimulator

class TicTacToeSimulator(GameSimulator):
    def __init__(self, player1: TicTacToePlayer, player2: TicTacToePlayer):
        super().__init__([player1, player2])
        self.__num_rows = 3
        self.__num_cols = 3

    def init_game(self):
        return TicTacToeState()

    def before_end_game(self, state: TicTacToeState):
        pass

    def end_game(self, state: TicTacToeState):
        pass
