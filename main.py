from constructor_classes.window_class import Window
from constructor_classes.maze import Maze

num_cols = 10
num_rows = 10
padding = 50
window_width = 1200
window_height = 1200

def main():
    window = Window(window_width, window_height)
    maze_width = window_width - (2 * padding)
    maze_height = window_height - (2 * padding)
    cell_size_x = maze_width // num_cols
    cell_size_y = maze_height // num_rows
    maze = Maze(padding, padding, num_rows, num_cols, window, cell_size_x, cell_size_y)
    window.wait_for_close()


if __name__ == "__main__":
    main()