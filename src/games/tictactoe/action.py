class TicTacToeAction:
    """
    A Tic-Tac-Toe action involves choosing a specific row and column on the board.
    """
    __row: int
    __col: int

    def __init__(self, row: int, col: int):
        self.__row = row
        self.__col = col

    def get_row(self):
        return self.__row

    def get_col(self):
        return self.__col

