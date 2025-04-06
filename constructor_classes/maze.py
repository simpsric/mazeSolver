from .cells import Cell
import time
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        win,
        cell_size_x=100,
        cell_size_y=100,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        
    def __create_cells(self):
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__cells.append(
                    Cell(
                        1,
                        1,
                        1,
                        1,
                        self.__win
                    )
                )
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__draw_cell(col, row)
        
    def __draw_cell(self, col, row):
        x1 = self.__x1 + col * self.__cell_size_x
        y1 = self.__y1 + row * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[row * self.__num_cols + col].draw(x1, y1, x2, y2)
        self.__animate()
        
    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
            