import math
from games.tictactoe.player import TicTacToePlayer
from games.tictactoe.action import TicTacToeAction
from games.tictactoe.result import TicTacToeResult
from games.tictactoe.state import TicTacToeState

class MinimaxTicTacToePlayer(TicTacToePlayer):
    def __init__(self, name):
        super().__init__(name)


    def __heuristic(self, state: TicTacToeState):
        score = 0
        lines = []

        # Add all possible lines (rows, columns, diagonals) into the list
        for row in range(state.get_num_rows()):
            lines.append(state.get_grid()[row])  # rows
        for col in range(state.get_num_cols()):
            lines.append([state.get_grid()[row][col] for row in range(state.get_num_rows())])  # columns
        lines.append([state.get_grid()[i][i] for i in range(state.get_num_rows())])  # main diagonal
        lines.append([state.get_grid()[i][state.get_num_rows() - 1 - i] for i in range(state.get_num_rows())])  # secondary diagonal

        # Evaluate each line
        for line in lines:
            if line.count(self.get_current_pos()) == 2 and line.count(TicTacToeState.EMPTY_CELL) == 1:
                score += 1  # Favorable setup: two in a row with a chance to win
            if line.count((self.get_current_pos() + 1) % 2) == 2 and line.count(TicTacToeState.EMPTY_CELL) == 1:
                score -= 1  # Defensive move needed: opponent has two in a row

        return score


    def minimax(self, state: TicTacToeState, depth: int, is_maximizing: bool):
        if state.is_finished():
            if state.get_result(self.get_current_pos()) == TicTacToeResult.WIN:
                return 10 - depth
            elif state.get_result((self.get_current_pos() + 1) % 2) == TicTacToeResult.WIN:
                return depth - 10
            else:
                return 0

        if depth == 0:
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for action in state.get_possible_actions():
                new_state = state.clone()
                new_state.update(action)
                eval = self.minimax(new_state, depth - 1, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = math.inf
            for action in state.get_possible_actions():
                new_state = state.clone()
                new_state.update(action)
                eval = self.minimax(new_state, depth - 1, True)
                min_eval = min(min_eval, eval)
            return min_eval

    def get_action(self, state: TicTacToeState):
        #state.display()
        best_score = -math.inf
        best_action = None
        for action in state.get_possible_actions():
            new_state = state.clone()
            new_state.update(action)
            score = self.minimax(new_state, 3, False)  # You can adjust the depth as needed
            if score > best_score:
                best_score = score
                best_action = action
        return best_action

    def event_action(self, pos: int, action: TicTacToeAction, new_state: TicTacToeState):
        pass

    def event_end_game(self, final_state: TicTacToeState):
        pass
