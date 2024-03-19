from random import choice
from games.tictactoe.action import TicTacToeAction
from games.tictactoe.result import TicTacToeResult  # Ensure this import is present
from games.tictactoe.player import TicTacToePlayer
from games.tictactoe.state import TicTacToeState
from games.state import State

class DefensiveGreedyTicTacToePlayer(TicTacToePlayer):
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
        opponent_pos = 1 if self.get_current_pos() == 0 else 0
        if state.get_result(opponent_pos) == TicTacToeResult.WIN:
            return 10  # Highly prioritize blocking the opponent's winning moves
        return 1  # Neutral towards moves that don't immediately prevent a win

    def event_action(self, pos: int, action: TicTacToeAction, new_state: State):
        pass

    def event_end_game(self, final_state: State):
        pass
