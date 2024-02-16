from enum import Enum


class State(Enum):
    OFF = 0
    ON = 1
    VALUE = 2


class Tile:
    is_hidden = True

    def __init__(self, left_top_x, left_top_y, canvas, size_px, number):
        self.left_top = (left_top_x, left_top_y)
        self.right_bottom = (left_top_x + size_px, left_top_y + size_px)
        self.center = (left_top_x + size_px / 2, left_top_y + size_px / 2)
        self.font_size_px = int(size_px * 0.6)
        self.canvas = canvas
        self.number = number
        self.state = State.OFF

    def draw(self):
        color = 'white' if self.state is State.ON else 'black'
        self.canvas.draw_rectangle(self.left_top, self.right_bottom, line_color="black",
                                   fill_color=color, line_width=2)

        if self.state is State.VALUE:
            self.canvas.draw_text(self.number, self.center, font="Any " + str(self.font_size_px), color="white")
