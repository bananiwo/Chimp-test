import PySimpleGUI as sg

from Board import Board


def main(size, canvas_size):
    layout = [
        [sg.HSep(), sg.B("RESTART", k="-RESTART-"), sg.HSep()],
        [sg.G((canvas_size, canvas_size), (0, 0), (canvas_size, canvas_size), enable_events=True,
              k="-GRAPH-")]
    ]
    window = sg.Window("Chimpanzee game", layout, finalize=True)
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
                sg.popup_ok("YOU WON\nPLAY AGAIN")
                board = Board(graph, size)
            elif round == "YOU LOST":
                sg.popup_ok("YOU LOST\nTRY AGAIN")
                board = Board(graph, size)

        if event == "-RESTART-":
            board = Board(graph, size)
        if event in ("Exit", sg.WIN_CLOSED):
            break
    window.close()


def difficulty_window():
    layout = [[sg.T("Select difficulty")],
              [sg.B("EASY"), sg.B("HARD")]
              ]
    window = sg.Window("Chimpanzee game", layout, finalize=True)
    while True:
        event, values = window.read()
        if event in ("Exit", sg.WIN_CLOSED):
            break
        if event == "EASY":
            size = 5
        elif event == "HARD":
            size = 7
        return size
    window.close()


if __name__ == "__main__":
    sg.theme("dark grey")
    size = difficulty_window()
    w, h = sg.Window.get_screen_size()
    if size is not None:
        main(size, h - 200)
