import unittest

from constructor_classes.maze import Maze

class TestMaze(unittest.TestCase):
    def test_maze_creation_cols(self):
        maze = Maze(100, 100, 10, 10)
        self.assertEqual(len(maze._cells), 10)
        
    def test_maze_creation_rows(self):
        maze = Maze(100, 100, 10, 10)
        self.assertEqual(len(maze._cells[0]), 10)
        
    def test_maze_creation_cell_size(self):
        maze = Maze(100, 100, 10, 10)
        self.assertEqual(maze._cell_size_x, 100)
        self.assertEqual(maze._cell_size_y, 100)


if __name__ == "__main__":
    unittest.main()