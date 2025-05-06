import unittest

from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_cell_initialization(self):
        num_cols = 3
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Check if each cell is initialized correctly
        for i in range(num_cols):
            for j in range(num_rows):
                cell = m1._cells[i][j]
                self.assertIsInstance(cell, Cell)
                self.assertTrue(hasattr(cell, 'has_left_wall'))
                self.assertTrue(hasattr(cell, 'has_right_wall'))
                self.assertTrue(hasattr(cell, 'has_top_wall'))
                self.assertTrue(hasattr(cell, 'has_bottom_wall'))

    def test_maze_cell_count(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(50, 50, num_rows, num_cols, 20, 20)
    
        # Ensure that the maze has the expected number of rows and columns
        self.assertEqual(len(m1._cells), num_cols)  # Should have 5 columns
        self.assertEqual(len(m1._cells[0]), num_rows)  # Each column should have 5 rows


    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

if __name__ == "__main__":
    unittest.main()
