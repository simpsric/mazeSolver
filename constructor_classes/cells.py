from .point_and_line import *

class Cell:
    def __init__(self, x1, y1, x2, y2, window):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = window
        self.__walls = {"top": True, "right": True, "bottom": True, "left": True}
        
    def draw(self):
        if self.__walls["top"]:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)))
        if self.__walls["right"]:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)))
        if self.__walls["bottom"]:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)))
        if self.__walls["left"]:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)))
        