from .cells import Cell
import time
import random
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
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._seed = seed if seed is not None else random.randint(0, 10000)
        # Set the seed for the random number generator
        random.seed(self._seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(9, 9)
        self.__reset_cells_visited()
        
    def solve(self):
        return self.__solve_r(0, 0)
    
    def __solve_r(self, c, r):
        self.__animate()
        if c == self._num_cols - 1 and r == self._num_rows - 1:
            return True
        self._cells[c][r].visit()
        # For each direction, if cell available, no wall between cells, and cell not visited
        # Then draw move to that cell, and move to that cell
        
        if c + 1 < self._num_cols and not self._cells[c + 1][r].has_been_visited():
            if not self._cells[c][r]._walls["right"]:
                self._cells[c][r].draw_move(self._cells[c + 1][r])
                if self.__solve_r(c + 1, r):
                    return True
                else:
                    self._cells[c][r].draw_move(self._cells[c + 1][r], undo=True)
        if c - 1 >= 0 and not self._cells[c - 1][r].has_been_visited():
            if not self._cells[c][r]._walls["left"]:
                self._cells[c][r].draw_move(self._cells[c - 1][r])
                if self.__solve_r(c - 1, r):
                    return True
                else:
                    self._cells[c][r].draw_move(self._cells[c - 1][r], undo=True)
        if r + 1 < self._num_rows and not self._cells[c][r + 1].has_been_visited():
            if not self._cells[c][r]._walls["bottom"]:
                self._cells[c][r].draw_move(self._cells[c][r + 1])
                if self.__solve_r(c, r + 1):
                    return True
                else:
                    self._cells[c][r].draw_move(self._cells[c][r + 1], undo=True)
        if r - 1 >= 0 and not self._cells[c][r - 1].has_been_visited():
            if not self._cells[c][r]._walls["top"]:
                self._cells[c][r].draw_move(self._cells[c][r - 1])
                if self.__solve_r(c, r - 1):
                    return True
                else:
                    self._cells[c][r].draw_move(self._cells[c][r - 1], undo=True)
        return False
        
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
        self._cells[col][row].draw(x1, y1, x2, y2)
        self.__animate()
        
    def __animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.01)
            
    def __reset_cells_visited(self):
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._cells[col][row].un_visit()
            
    def __break_walls_r(self, r, c):
        current_cell = self._cells[c][r]
        current_cell.visit()
        while True:
            next_lst = []
            # See if we can move north
            if r - 1 >= 0 and not self._cells[c][r - 1].has_been_visited():
                next_lst.append(("N", c, r - 1))
            # See if we can move south
            if r + 1 < self._num_rows and not self._cells[c][r + 1].has_been_visited():
                next_lst.append(("S", c, r + 1))
            # See if we can move east
            if c + 1 < self._num_cols and not self._cells[c + 1][r].has_been_visited():
                next_lst.append(("E", c + 1, r))
            # See if we can move west
            if c - 1 >= 0 and not self._cells[c - 1][r].has_been_visited():
                next_lst.append(("W", c - 1, r))
            # If there are no more moves, draw cell and return
            if len(next_lst) == 0:
                self.__draw_cell(c, r)
                return
            # Choose a random move
            direction, next_c, next_r = random.choice(next_lst)
            # Knock down the wall between the current cell and the next cell
            if direction == "N":
                current_cell._walls["top"] = False
                self._cells[next_c][next_r]._walls["bottom"] = False
            elif direction == "S":
                current_cell._walls["bottom"] = False
                self._cells[next_c][next_r]._walls["top"] = False
            elif direction == "E":
                current_cell._walls["right"] = False
                self._cells[next_c][next_r]._walls["left"] = False
            elif direction == "W":
                current_cell._walls["left"] = False
                self._cells[next_c][next_r]._walls["right"] = False
            # Move to the next cell
            self.__break_walls_r(next_r, next_c)
            
    def __break_entrance_and_exit(self):
        ent_x = 0
        ent_y = 0
        exit_x = self._num_cols - 1
        exit_y = self._num_rows - 1
        self._cells[ent_x][ent_y]._walls["top"] = False
        self._cells[exit_x][exit_y]._walls["bottom"] = False
        self.__draw_cell(ent_x, ent_y)
        self.__draw_cell(exit_x, exit_y)
        