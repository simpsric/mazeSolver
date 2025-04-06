from .point_and_line import *

class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        if self._win is not None:
            self._background_color = self._win.canvas["background"]
        else:
            self._background_color = "white"
        self._walls = {"top": True, "right": True, "bottom": True, "left": True}
        self._visited = False
        
    def has_been_visited(self):
        return self._visited
    
    def visit(self):
        self._visited = True
        
    def un_visit(self):
        self._visited = False
        
    def draw(self, x1, y1, x2, y2):
        # Set new x1, y1, x2, y2
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self._win is not None:
            if self._walls["top"]:
                self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
            else:
                self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), self._background_color)
            if self._walls["right"]:
                self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
            else:
                self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), self._background_color)
            if self._walls["bottom"]:
                self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
            else:
                self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), self._background_color)
            if self._walls["left"]:
                self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
            else:
                self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), self._background_color)
        else:
            print("No window to draw on")
        
    def draw_move(self, to_cell, undo=False):
        if self._win is not None:
            if undo:
                # Draw a line between the centers of the two cells
                self._win.draw_line(Line(Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2), 
                                       Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)), "red")
            else:
                self._win.draw_line(Line(Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2), 
                                       Point((to_cell._x1 + to_cell._x2) // 2, (to_cell._y1 + to_cell._y2) // 2)), "sky blue")
            
        