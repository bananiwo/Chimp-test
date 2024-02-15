import numpy as np

class Tile:

    is_hidden = True

    def __init__(self, x, y):
        self.position = np.array([x, y], dtype=int)

