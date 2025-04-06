from .cells import Cell
import time
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        win=None,
        cell_size_x=100,
        cell_size_y=100,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self.__create_cells()
        
    def __create_cells(self):
        for col in range(self._num_cols):
            col_list = []
            for row in range(self._num_rows):
                col_list.append(
                    Cell(
                        1,
                        1,
                        1,
                        1,
                        self._win
                    )
                )
            self._cells.append(col_list)
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self.__draw_cell(col, row)
        
    def __draw_cell(self, col, row):
        x1 = self._x1 + col * self._cell_size_x
        y1 = self._y1 + row * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[row][col].draw(x1, y1, x2, y2)
        self.__animate()
        
    def __animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)
            