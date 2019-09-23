from minesweeper import Minesweeper
import unittest

class MinesweeperTest(unittest.TestCase):
    def setUp(self):
        self.grid_size = 10
        self.number_of_mines = 10
        self.board_id = "1"
        self.minesweeper = Minesweeper(self.grid_size, self.number_of_mines, self.board_id)

    def tearDown(self):
        del self.grid_size
        del self.number_of_mines
        del self.board_id
        del self.minesweeper

   
