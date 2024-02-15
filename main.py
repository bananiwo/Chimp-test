import PySimpleGUI as sg

from Board import Board

canvas_height = 900
canvas_width = 900


def main():
    layout = [
        {sg.G((canvas_width, canvas_height), (0, 0), (canvas_width, canvas_height), enable_events=True,
              background_color="light grey", k="-GRAPH-")}
    ]
    window = sg.Window("Chimpanzee game", layout, finalize=True)
    graph = window["-GRAPH-"]
    board = Board(graph, 5)
    while True:
        event, values = window.read(timeout=16)
        graph.erase()
        board.draw()

        if event == "-GRAPH-":
            mouse_x, mouse_y = values["-GRAPH-"]
            board.flip_tile(mouse_x, mouse_y)

        if event in ("Exit", sg.WIN_CLOSED):
            break
    window.close()


if __name__ == "__main__":
    main()
