import tkinter as tk
import tkinter.scrolledtext as tkst
from string import ascii_uppercase


class board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.files = ascii_uppercase[:self.width]
        self.ranks = range(1, self.height + 1)


class Example():
    def __init__(self, board):
        self.root = tk.Tk()
        self.root.title("python chess")
        self.root.configure(background="#e403c5")

        # build top level frames
        self.canvasArea = tk.Frame(self.root, height=150, width=150,
                                   bg="#efefef")
        self.canvasArea.grid(row=0, column=0)
        self.rightArea = tk.Frame(self.root, height=150, width=150,
                                  bg="#0e0e0e")
        self.rightArea.grid(row=0, column=1)

        # fill canvasArea

        def clickCanvas(event):
            self.history.insert(tk.END, event.widget.name + "\n")

        highlightlist = ["A1", "B4", "E7"]

        def applyHighlightcolor(event, highlightlist=highlightlist):
            highlightcolor = "#e036f1"
            for canvas in canvaslist:
                if canvas.name in highlightlist:
                    canvas.configure(background=highlightcolor)

        canvaslist = []
        for i in range(board.height):
            for j in range(board.width):
                color = "#343434" if (i + j) % 2 == 0 else "#ababab"

                self.x = tk.Canvas(self.canvasArea, width=40, height=40,
                                   background=color, highlightthickness=0)
                self.x.create_text(32, 32, fill="gray", font="FiraMono 8 bold",
                                   text=f"{board.files[i]}{board.ranks[j]}")
                self.x.grid(row=board.height - i, column=j)
                # self.x.bind("<Button-1>", clickCanvas)
                self.x.bind("<Button-1>", applyHighlightcolor)
                self.x.name = f"{board.files[i]}{board.ranks[j]}"
                canvaslist.append(self.x)

        # fill rightArea

        self.history = tkst.ScrolledText(self.rightArea, height=15, width=30)
        self.history.grid()
        self.history.insert(tk.END, "Test\n\n\n\ndsfsdfsd\n")

        # # create a Text widget with a Scrollbar attached
        # self.txt = tk.scrolledtext(self.root, undo=True)
        # self.txt.insert(tk.END, "tetss")
        # self.txt.pack(expand=True, fill='both')
        self.root.mainloop()


if __name__ == '__main__':
    chessboard = board(8, 8)
    Example(chessboard)
