from typing import Optional, List
from games.tictactoe.action import TicTacToeAction
from games.tictactoe.result import TicTacToeResult
from games.state import State

class TicTacToeState(State):
    EMPTY_CELL = -1

    def __init__(self):
        super().__init__()
        self.__num_rows = 3
        self.__num_cols = 3
        self.__grid = [[TicTacToeState.EMPTY_CELL for _ in range(self.__num_cols)] for _ in range(self.__num_rows)]
        self.__turns_count = 0
        self.__acting_player = 0
        self.__has_winner = False

    def __check_winner(self):
        # Check all win conditions for Tic-Tac-Toe
        lines = []

        # Rows, columns, and diagonals
        lines.extend(self.__grid)  # Rows
        lines.extend([[self.__grid[r][c] for r in range(self.__num_rows)] for c in range(self.__num_cols)])  # Columns
        lines.append([self.__grid[i][i] for i in range(self.__num_rows)])  # Diagonal \
        lines.append([self.__grid[i][self.__num_rows-i-1] for i in range(self.__num_rows)])  # Diagonal /

        for line in lines:
            if all(cell == self.__acting_player for cell in line):
                return True
        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: TicTacToeAction) -> bool:
        row, col = action.get_row(), action.get_col()
        return 0 <= row < self.__num_rows and 0 <= col < self.__num_cols and self.__grid[row][col] == TicTacToeState.EMPTY_CELL

    def update(self, action: TicTacToeAction):
        row, col = action.get_row(), action.get_col()
        if self.validate_action(action):
            self.__grid[row][col] = self.__acting_player
            self.__has_winner = self.__check_winner()
            self.__acting_player = 1 if self.__acting_player == 0 else 0
            self.__turns_count += 1

    def __display_cell(self, row, col):
        print({
                  0: 'X',
                  1: 'O',
                  TicTacToeState.EMPTY_CELL: ' '
              }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__num_cols):
            if col < 10:
                print(' ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__num_cols):
            print("--", end="")
        print("-")

    def display(self):
        print("\n------ New Board State ------\n")
        for row in self.__grid:
            print(' | ' + ' | '.join([' ' if cell == TicTacToeState.EMPTY_CELL else 'X' if cell == 0 else 'O' for cell in row]) + ' |')
        print("\n----------------------------\n")

    def __is_full(self):
        return self.__turns_count > (self.__num_cols * self.__num_rows)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__turns_count == self.__num_rows * self.__num_cols
        # TICTACTOE TRADICIONAL TEM DE TER WINNER OU BOARD CHEIA, DA PRA GANHAR ANTES DE ACABAR


    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = TicTacToeState()
        cloned_state.__grid = [row[:] for row in self.__grid]
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        return cloned_state

    def get_result(self, pos) -> Optional[TicTacToeResult]:
        if self.__has_winner:
            # If the game has ended with a win, the player who just moved is the winner.
            winning_player = 1 if self.__acting_player == 0 else 0
            return TicTacToeResult.WIN if pos == winning_player else TicTacToeResult.LOOSE
        elif self.__turns_count == self.__num_rows * self.__num_cols:
            return TicTacToeResult.DRAW
        return None

    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols

    def before_results(self):
        pass

    def get_possible_actions(self) -> List[TicTacToeAction]:
        actions = []
        for row in range(self.__num_rows):
            for col in range(self.__num_cols):
                if self.__grid[row][col] == TicTacToeState.EMPTY_CELL:
                    actions.append(TicTacToeAction(row, col))
        return actions

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
