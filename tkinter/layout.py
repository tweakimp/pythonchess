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
        self.board = board
        self.root = tk.Tk()
        self.root.title("python chess")
        self.root.configure(background="#e403c5")
        self.canvaslist = []
        self.colors = {"white": "#b4b4b4", "black": "#4b4b4b",
                       "whiteAllowed": "#509750", "blackALlowed": "#84cc84",
                       "whiteRestricted": "#cc8484", "blackRestricted": "#975050"}

        # build top level frames
        self.canvasArea = tk.Frame(self.root, height=150, width=150,
                                   bg="#efefef")
        self.canvasArea.grid(row=0, column=0)
        self.rightArea = tk.Frame(self.root, height=150, width=150,
                                  bg="#0e0e0e")
        self.rightArea.grid(row=0, column=1)
        # fill canvasArea
        self.initCanvases(board)
        # fill rightArea
        self.history = tkst.ScrolledText(self.rightArea, height=15, width=30)
        self.history.grid(row=0, column=0)
        self.history.insert(tk.END, "LETS PLAY CHESS!\n")
        self.inputwindow = tk.Entry(self.rightArea)
        self.inputwindow.grid(row=1, column=0)
        self.inputwindow.bind("<Return>", self.getInput)

        # # create a Text widget with a Scrollbar attached
        # self.txt = tk.scrolledtext(self.root, undo=True)
        # self.txt.insert(tk.END, "tetss")
        # self.txt.pack(expand=True, fill='both')
        self.root.mainloop()

    def getInput(self, event):
        self.history.insert(tk.END, (str(event.widget.get()))+"\n")

    def colorNormal(self, event):
        square = event
        color = self.colors["white"] if (
            square.widget.file + square.widget.rank) % 2 == 0 else self.colors["black"]
        square.widget.configure(background=color)
        square.widget.img = tk.PhotoImage(file="sprites\whiteQueen100.png")
        square.widget.create_image(50, 50, image=square.widget.img)
        # square.widget.create_image(
        #     50, 50, image=tk.PhotoImage(file="whiteQueen50.png"))

    def colorAllowed(self, event):
        square = event
        color = self.colors["whiteAllowed"] if (
            square.widget.file + square.widget.rank) % 2 == 0 else self.colors["blackALlowed"]
        square.widget.configure(background=color)

    def colorRestricted(self, event):
        square = event
        color = self.colors["whiteRestricted"] if (
            square.widget.file + square.widget.rank) % 2 == 0 else self.colors["blackRestricted"]
        square.widget.configure(background=color)

    def initCanvases(self, board):
        for i in range(board.height):
            for j in range(board.width):
                color = self.colors["white"] if (
                    i + j) % 2 == 0 else self.colors["black"]
                self.x = tk.Canvas(self.canvasArea, width=100, height=100,
                                   background=color, highlightthickness=0)
                self.x.create_text(8, 92, fill="#ffffff", font="FiraMono 8 bold",
                                   text=f"{board.files[i]}{board.ranks[j]}")
                self.x.grid(row=self.board.height - i, column=j)
                self.x.bind("<Button-1>", self.colorAllowed)
                self.x.bind("<Button-2>", self.colorRestricted)
                self.x.bind("<Button-3>", self.colorNormal)
                self.x.name = f"{board.files[i]}{board.ranks[j]}"
                self.x.file = i
                self.x.rank = j
                self.canvaslist.append(self.x)


if __name__ == '__main__':
    chessboard = board(8, 8)
    Example(chessboard)
