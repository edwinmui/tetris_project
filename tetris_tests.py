import unittest
from tetris import *


class Test_Grid(unittest.TestCase):
    def test_get_grid_height(self):
        grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]
        self.assertEqual(get_grid_height(grid), 20)

    def test_get_grid_width(self):
        grid = [[(0, 0, 0) for x in range(10)] for x in range(20)]
        self.assertEqual(get_grid_width(grid), 10)

if __name__ == '__main__':
    unittest.main()