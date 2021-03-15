"""
    Tic Tac Toe game.
"""

class UnknownInputError(Exception):
    """
        Unidentifed input exception class.
    """
    def __init__(self, text,
                 message='You should input have exactly two numbers delimited by space.'):
        self.text = text
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return '{} -> {}'.format(self.text, self.message)

class InputRangeError(Exception):
    """
        Illegal input coordinates exception class.
    """
    def __init__(self, inputs, message='Inputs should be between 0 and 2'):
        self.inputs = inputs
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return '{},{} -> {}'.format(*self.inputs, self.message)

class IllegalTurnError(Exception):
    """
        Illegal tic tac toe turn exception class.
    """
    def __init__(self, i, j, message='The cell has already been filled.'):
        self.inputs = (i, j)
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return 'Cell: ({},{}) -> {}'.format(*self.inputs, self.message)


class TicTacGame:
    """
        Class for Tic Tac Toe terminal game.
    """
    def __init__(self):
        self.board = [['_', '_', '_'] for _ in range(3)]
        self.pos_to_check = [[(0, 0), (0, 1), (0, 2)],
                             [(1, 0), (1, 1), (1, 2)],
                             [(2, 0), (2, 1), (2, 2)],
                             [(0, 0), (1, 0), (2, 0)],
                             [(0, 1), (1, 1), (2, 1)],
                             [(0, 2), (1, 2), (2, 2)],
                             [(0, 0), (1, 1), (2, 2)],
                             [(0, 2), (1, 1), (2, 0)],]
        self.turn_x = True

    def show_board(self):
        """
            Print current Tic Tac Toe board.
        """
        for i in range(3):
            print(' '.join(self.board[i]))

    def validate_and_process_input(self, text):
        """
            Function throws exceptions whenever input is wrong. Returns int coords.
        """
        inputs = text.split()
        if len(inputs) != 2:
            raise UnknownInputError(text)
        i, j = int(inputs[0]), int(inputs[1])
        if not 0 <= i <= 2 or not 0 <= j <= 2:
            raise InputRangeError([i, j])
        if self.board[i][j] != '_':
            raise IllegalTurnError(i, j)
        return i, j

    def start_game(self):
        """
            Managing terminal tic tac toe game.
        """
        while True:
            self.show_board()
            text = input()
            try:
                i, j = self.validate_and_process_input(text)
            except UnknownInputError as inst:
                print(inst)
                continue
            except ValueError:
                print('One of arguments is not an integer number.')
                continue
            except InputRangeError as inst:
                print(inst)
                continue
            except IllegalTurnError as inst:
                print(inst)
                continue
            self.board[i][j] = 'x' if self.turn_x else 'o'
            state = self.check_winner()
            if state is None:
                print('it is a draw!')
                return
            if state:
                print('{} wins!'.format('x' if self.turn_x else 'o'))
                return
            self.turn_x = not self.turn_x

    def check_winner(self):
        """
            Checking is there a winner on the board.
        """
        draw_condition = True
        for pos in self.pos_to_check:
            x_1 = self.board[pos[0][0]][pos[0][1]]
            x_2 = self.board[pos[1][0]][pos[1][1]]
            x_3 = self.board[pos[2][0]][pos[2][1]]
            line = {x_1, x_2, x_3}
            if len(line) == 1 and not '_' in line:
                return True
            draw_condition = draw_condition and 'x' in line and 'o' in line
        if draw_condition:
            return None
        return False

if __name__ == '__main__':
    TicTacGame().start_game()
