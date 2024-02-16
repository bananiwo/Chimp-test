import numpy as np

from Tile import Tile, State


class Board:
    current_level: int = 5
    successes_int_current_level: int = 0

    def __init__(self, canvas, size=5):
        self.tiles = np.full((size, size), False, dtype=bool)
        self.size = size
        self.tile_size_px = canvas.CanvasSize[0] / size
        self.values = np.arange(1, self.size ** 2 + 1, dtype=int)
        np.random.shuffle(self.values)
        self.tiles = []
        for i in range(size):
            for j in range(size):
                tile = Tile(i * self.tile_size_px, j * self.tile_size_px, canvas,
                            self.tile_size_px, self.values[i * size + j])
                self.tiles.append(tile)
        self.tiles.sort(key=lambda t: t.number)
        self.set_state_value()

    def set_state_value(self):
        for i in range(self.current_level + 1):
            for tile in self.tiles:
                if tile.number == i:
                    tile.state = State.VALUE
        self.draw()

    def set_state_on(self):
        for i in range(self.current_level + 1):
            for tile in self.tiles:
                if tile.number == i:
                    tile.state = State.ON

    def shuffle_values(self):
        np.random.shuffle(self.values)
        for value, tile in zip(self.values, self.tiles):
            tile.number = value

    def select_tile(self, mouse_x, mouse_y):
        tile = self.get_tile(mouse_x, mouse_y)
        if self.current_level > 0 and tile.state == State.OFF:
            return
        expected_value = self.successes_int_current_level + 1
        if tile.state == State.ON and tile.number != expected_value:
            return "YOU LOST"
        if tile.number == 1:
            self.set_state_on()
        self.successes_int_current_level += 1
        tile.state = State.OFF
        tile.draw()
        if self.successes_int_current_level == self.current_level:
            self.successes_int_current_level = 0
            self.current_level += 1
            self.hide_all_tiles()
            self.shuffle_values()
            self.set_state_value()
            self.draw()
            return "NEXT ROUND"

    def get_tile(self, mouse_x, mouse_y):
        for tile in self.tiles:
            if tile.right_bottom[0] > mouse_x > tile.left_top[0] and tile.left_top[1] < mouse_y < tile.right_bottom[1]:
                return tile
        raise ValueError("Tile not found")

    def draw(self):
        for tile in self.tiles:
            tile.draw()

    def hide_all_tiles(self):
        for tile in self.tiles:
            tile.state = State.OFF
        self.draw()
