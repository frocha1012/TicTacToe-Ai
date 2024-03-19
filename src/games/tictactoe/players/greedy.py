from random import choice
from games.tictactoe.action import TicTacToeAction
from games.tictactoe.result import TicTacToeResult  # Ensure this import is present
from games.tictactoe.player import TicTacToePlayer
from games.tictactoe.state import TicTacToeState
from games.state import State

class GreedyTicTacToePlayer(TicTacToePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TicTacToeState) -> TicTacToeAction:
        # Attempt to win or block the opponent from winning

        possible_actions = state.get_possible_actions()
        best_action = None
        best_score = -1

        for action in possible_actions:
            # Simulate the action
            new_state = state.clone()
            new_state.update(action)
            score = self.evaluate_action(new_state, action)

            if score > best_score:
                best_action = action
                best_score = score
        
        if best_action is not None:
            return best_action
        else:
            # If no "greedy" action found, choose randomly among available actions
            return choice(possible_actions) if possible_actions else None
        

    def evaluate_action(self, state: TicTacToeState, action: TicTacToeAction) -> int:
        """
        Evaluates the action based on a simple heuristic:
        - +10 for a winning move,
        - +1 for blocking an opponent's winning move,
        - 0 otherwise.
        """
        if state.is_finished():
            if state.get_result(self.get_current_pos()) == TicTacToeResult.WIN:
                return 10  # Winning move
            elif state.get_result(self.get_current_pos()) == TicTacToeResult.DRAW:
                return 0  # Neutral move
        else:
            # Check if the move blocks the opponent
            opponent_pos = 1 if self.get_current_pos() == 0 else 0
            if state.get_result(opponent_pos) == TicTacToeResult.WIN:
                return 1  # Blocking move
        return 0  # Neutral move

    def event_action(self, pos: int, action: TicTacToeAction, new_state: State):
        pass

    def event_end_game(self, final_state: State):
        pass
