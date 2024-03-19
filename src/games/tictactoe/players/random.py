from random import choice
from games.tictactoe.action import TicTacToeAction
from games.tictactoe.player import TicTacToePlayer
from games.tictactoe.state import TicTacToeState
from games.state import State

class RandomTicTacToePlayer(TicTacToePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TicTacToeState) -> TicTacToeAction:
        # Get all possible actions (i.e., all empty cells)
        possible_actions = state.get_possible_actions()
        # Select a random action from the list of possible actions
        return choice(possible_actions) if possible_actions else None

    def event_action(self, pos: int, action: TicTacToeAction, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
