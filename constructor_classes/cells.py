from .point_and_line import *

class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = win
        self.__walls = {"top": True, "right": True, "bottom": True, "left": True}
        
    def draw(self, x1, y1, x2, y2):
        if self.__win is not None:
            if self.__walls["top"]:
                self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
            if self.__walls["right"]:
                self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
            if self.__walls["bottom"]:
                self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
            if self.__walls["left"]:
                self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        
    def draw_move(self, to_cell, undo=False):
        if self.__win is not None:
            if undo:
                self.__win.draw_line(Line(Point((self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2), Point((self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2)), "red")
            else:
                self.__win.draw_line(Line(Point((self.__x1 + self.__x2) // 2, (self.__y1 + self.__y2) // 2), Point((to_cell.__x1 + to_cell.__x2) // 2, (to_cell.__y1 + to_cell.__y2) // 2)), "gray")
            
        