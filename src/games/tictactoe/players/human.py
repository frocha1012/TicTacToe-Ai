from games.tictactoe.action import TicTacToeAction
from games.tictactoe.player import TicTacToePlayer
from games.tictactoe.state import TicTacToeState
from games.tictactoe.result import TicTacToeResult


class HumanTicTacToePlayer(TicTacToePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TicTacToeState):
        state.display()
        while True:
            try:
                row = int(input("Choose a row (0-2): "))
                col = int(input("Choose a column (0-2): "))
                action = TicTacToeAction(row, col)
                if state.validate_action(action):
                    return action
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter numbers only.")

    def event_action(self, pos: int, action: TicTacToeAction, new_state: TicTacToeState):
        # This method can be used to notify the player of actions taken in the game.
        # For a human player, this might not be necessary unless you want to log moves or provide commentary.
        pass

    def event_end_game(self, final_state: TicTacToeState):
        # This could be a good place to show the final board and announce the game result.
        final_state.display()
        print("Game over!")
        if final_state.get_result(self.get_current_pos()) == TicTacToeResult.WIN:
            print("You win!")
        elif final_state.get_result((self.get_current_pos() + 1) % 2) == TicTacToeResult.WIN:
            print("You lose.")
        else:
            print("It's a draw.")
