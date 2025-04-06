from tkinter import Tk, BOTH, Canvas
from .point_and_line import Line
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver 9000")
        self.__root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.__root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running_window = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.running_window = True
        while self.running_window:
            self.redraw()
        self.__root.destroy()
        
    def close(self):
        self.running_window = False
        
    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.canvas, fill_color)
        self.canvas.pack(fill=BOTH, expand=1)
