import math
from games.tictactoe.player import TicTacToePlayer
from games.tictactoe.action import TicTacToeAction
from games.tictactoe.result import TicTacToeResult
from games.tictactoe.state import TicTacToeState

class OffensiveMinimaxTicTacToePlayer(TicTacToePlayer):
    def __init__(self, name):
        super().__init__(name)

    def __get_lines(self, state: TicTacToeState):
        lines = []
        for i in range(state.get_num_rows()):
            lines.append(state.get_grid()[i])  # row
            lines.append([state.get_grid()[j][i] for j in range(state.get_num_cols())])  # column
        # Diagonals
        lines.append([state.get_grid()[i][i] for i in range(state.get_num_rows())])
        lines.append([state.get_grid()[i][state.get_num_rows() - 1 - i] for i in range(state.get_num_rows())])
        return lines

    def __heuristic(self, state: TicTacToeState):
        score = 0
        for line in self.__get_lines(state):
            my_count = line.count(self.get_current_pos())
            if my_count == 2 and line.count(TicTacToeState.EMPTY_CELL) == 1:
                score += 2
            elif my_count == 1 and line.count(TicTacToeState.EMPTY_CELL) == 2:
                score += 1
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
            return self.__heuristic(state)

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
        best_score = -math.inf
        best_action = None
        for action in state.get_possible_actions():
            new_state = state.clone()
            new_state.update(action)
            score = self.minimax(new_state, 3, False)  # Adjust depth as needed
            if score > best_score:
                best_score = score
                best_action = action
        return best_action

    def event_action(self, pos: int, action: TicTacToeAction, new_state: TicTacToeState):
        pass

    def event_end_game(self, final_state: TicTacToeState):
        pass
