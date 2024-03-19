from random import choice
from games.tictactoe.action import TicTacToeAction
from games.tictactoe.result import TicTacToeResult  # Ensure this import is present
from games.tictactoe.player import TicTacToePlayer
from games.tictactoe.state import TicTacToeState
from games.state import State

class OffensiveGreedyTicTacToePlayer(TicTacToePlayer):
    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TicTacToeState) -> TicTacToeAction:
        possible_actions = state.get_possible_actions()
        best_action = None
        best_score = -1

        for action in possible_actions:
            new_state = state.clone()
            new_state.update(action)
            score = self.evaluate_action(new_state, action)

            if score > best_score:
                best_action = action
                best_score = score

        return best_action if best_action is not None else choice(possible_actions)

    def evaluate_action(self, state: TicTacToeState, action: TicTacToeAction) -> int:
        if state.is_finished():
            if state.get_result(self.get_current_pos()) == TicTacToeResult.WIN:
                return 10  # Prioritize winning moves
        return 1  # Slightly favor moves that don't immediately lead to a win but progress the game

    def event_action(self, pos: int, action: TicTacToeAction, new_state: State):
        pass

    def event_end_game(self, final_state: State):
        pass
