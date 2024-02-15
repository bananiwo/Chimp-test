import math

import numpy as np


class Board:

    def __init__(self, canvas, size=5):
        self.tiles = np.full((size, size), False, dtype=bool)
        self.size_in_tiles = size
        self.tile_size_in_px = canvas.CanvasSize[0] / size
        self.canvas = canvas

    def draw(self):
        for i in range(self.size_in_tiles):
            for j in range(self.size_in_tiles):
                if self.tiles[i][j] == True:
                    color = "red"
                else:
                    color = "blue"
                self.canvas.draw_rectangle((i * self.tile_size_in_px, j * self.tile_size_in_px),
                                           ((i + 1) * self.tile_size_in_px, (j + 1) * self.tile_size_in_px), line_color="white",
                                           fill_color=color)

    def flip_tile(self, mouse_x, mouse_y):
        column = math.floor(mouse_x / self.tile_size_in_px)
        row = math.floor(mouse_y / self.tile_size_in_px)
        self.tiles[column][row] = not self.tiles[column][row]
