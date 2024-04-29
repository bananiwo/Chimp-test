import PySimpleGUI as sg

from Board import Board

WINDOW_NAME = "Chimpanzee test"
WIN_MESSAGE = "YOU WON\nPLAY AGAIN"
LOST_MESSAGE = "YOU LOST\nTRY AGAIN"

size = 10

def main(canvas_size):
    layout = [
        [sg.HSep(), sg.B("RESTART", k="-RESTART-"), sg.HSep()],
        [sg.G((canvas_size, canvas_size), (0, 0), (canvas_size, canvas_size), enable_events=True,
              k="-GRAPH-")]
    ]
    window = sg.Window(WINDOW_NAME, layout, finalize=True)
    graph = window["-GRAPH-"]
    board = Board(graph, size)
    board.draw()
    while True:
        event, values = window.read()
        graph.erase()
        if event == "-GRAPH-":
            mouse_x, mouse_y = values["-GRAPH-"]
            round = board.select_tile(mouse_x, mouse_y)
            board.draw()
            if round == "YOU WON":
                sg.popup_ok(WIN_MESSAGE)
                board = Board(graph, size)
            elif round == "YOU LOST":
                sg.popup_ok(LOST_MESSAGE)
                board = Board(graph, size)

        if event == "-RESTART-":
            board = Board(graph, size)
        if event in ("Exit", sg.WIN_CLOSED):
            break
    window.close()


if __name__ == "__main__":
    sg.theme("dark grey")
    w, h = sg.Window.get_screen_size()
    main(h - 200)
