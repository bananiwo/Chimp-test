class Tile:
    is_hidden = True

    def __init__(self, left_top_x, left_top_y, canvas, size_px, number):
        self.left_top = (left_top_x, left_top_y)
        self.right_bottom = (left_top_x + size_px, left_top_y + size_px)
        self.center = (left_top_x + size_px/2, left_top_y+size_px/2)
        self.font_size_px = int(size_px * 0.7)
        self.canvas = canvas
        self.number = number

    def draw(self):
        color = 'white' if self.is_hidden else 'dark grey'
        self.canvas.draw_rectangle(self.left_top, self.right_bottom, line_color="black",
                                   fill_color=color, line_width=2)
        if not self.is_hidden:
            self.canvas.draw_text(self.number, self.center, font="Any "+str(self.font_size_px), color="white")

