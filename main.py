from constructor_classes.window_class import Window
from constructor_classes.cells import Cell

def main():
    window = Window(800, 600)
    cell = Cell(100, 100, 200, 200, window)
    cell.draw()
    cell2 = Cell(200, 100, 300, 200, window)
    cell2.draw()
    window.wait_for_close()


if __name__ == "__main__":
    main()