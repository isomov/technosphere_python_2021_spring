"""
    Checking game_xo module.
"""

import unittest
import unittest.mock
from io import StringIO
from game_xo import *

class TestGameMethods(unittest.TestCase):

    @unittest.mock.patch('builtins.input', side_effect=['0 0', '0 1', '1 1', '2 1', '2 2'])
    def test_start_game_x_wins(self, mock_input):
        self.game = TicTacGame()
        with unittest.mock.patch('sys.stdout', new=StringIO()) as fake_output:
            self.game.start_game()
            value = fake_output.getvalue().strip()
            self.assertEqual(value.split('\n')[-1], 'x wins!')

    @unittest.mock.patch('builtins.input', side_effect=['2 0', '0 1', '1 1', '0 0', '1 0', '0 2'])
    def test_start_game_o_wins(self, mock_input):
        game = TicTacGame()
        with unittest.mock.patch('sys.stdout', new=StringIO()) as fake_output:
            game.start_game()
            value = fake_output.getvalue().strip()
            self.assertEqual(value.split('\n')[-1], 'o wins!')

    @unittest.mock.patch('builtins.input', side_effect=['2 0', '2 1', '1 1', '0 0', '1 0', '1 2', '2 2', '0 2', '1 1'])
    def test_start_game_draw(self, mock_input):
        game = TicTacGame()
        with unittest.mock.patch('sys.stdout', new=StringIO()) as fake_output:
            game.start_game()
            value = fake_output.getvalue().strip()
            self.assertEqual(value.split('\n')[-1], 'it is a draw!')

    def test_check_winner(self):
        game = TicTacGame()
        game.board = [['o', 'x', '_'],
                      ['x', 'o', '_'],
                      ['_', 'x', 'o']]
        self.assertTrue(game.check_winner())

        game.board = [['o', 'o', 'o'],
                      ['_', 'x', '_'],
                      ['x', 'x', '_']]
        self.assertTrue(game.check_winner())

        game.board = [['_', 'x', 'o'],
                      ['x', 'o', '_'],
                      ['_', 'x', 'o']]
        self.assertFalse(game.check_winner())

        game.board = [['_', '_', '_'],
                      ['_', 'o', '_'],
                      ['_', 'x', 'o']]
        self.assertFalse(game.check_winner())

        game.board = [['x', 'o', 'x'],
                      ['x', 'o', '_'],
                      ['o', 'x', 'o']]
        self.assertIsNone(game.check_winner())

    def test_validate_and_process_input(self):
        game = TicTacGame()
        try:
            game.validate_and_process_input('dfghjklxcvbnm')
        except Exception as inst:
            self.assertTrue(isinstance(inst, UnknownInputError))

        try:
            game.validate_and_process_input('2 rr')
        except Exception as inst:
            self.assertTrue(isinstance(inst, ValueError))

        try:
            game.validate_and_process_input('2 3')
        except Exception as inst:
            self.assertTrue(isinstance(inst, InputRangeError))

        game.board = [['x', 'x', 'o'],
                      ['x', 'o', '_'],
                      ['_', 'x', 'o']]
        try:
            game.validate_and_process_input('0 0')
        except Exception as inst:
            self.assertTrue(isinstance(inst, IllegalTurnError))

    def test_show_board(self):
        game = TicTacGame()
        with unittest.mock.patch('sys.stdout', new=StringIO()) as fake_output:
            game.board = [['_', 'x', 'o'],
                          ['x', 'o', '_'],
                          ['_', 'x', 'o']]
            game.show_board()
            value = fake_output.getvalue().strip()
            self.assertEqual(value, '_ x o\nx o _\n_ x o')

if __name__ == '__main__':
    unittest.main()
