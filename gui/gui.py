import tkinter as tk
import tkinter.scrolledtext as tkst

from ressources import chessboard


class GUI():
    def __init__(self, board):
        self.root = tk.Tk()
        self.root.title("python chess")
        self.root.configure(background="#e403c5")
        self.canvasdict = {}
        self.colors = {"white": "#b4b4b4", "black": "#4b4b4b",
                       "whiteGreen": "#509750", "blackGreen": "#84cc84",
                       "whiteRed": "#cc8484", "blackRed": "#975050"}
        self.sprites = {"bK": "blackKing", "bQ": "blackQueen",
                        "bR": "blackRook", "bB": "blackBishop",
                        "bN": "blackKnight", "bP": "blackPawn",
                        "wK": "whiteKing", "wQ": "whiteQueen",
                        "wR": "whiteRook", "wB": "whiteBishop",
                        "wN": "whiteKnight", "wP": "whitePawn"}

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
        self.drawSprites(board)
        self.root.mainloop()

    def getInput(self, event):
        self.history.insert(tk.END, (str(event.widget.get())) + "\n")

    def colorNormal(self, event):
        square = event.widget
        color = self.colors["white"] if (
            square.file + square.rank) % 2 == 0 else self.colors["black"]
        square.configure(background=color)

    def drawSprites(self, board):
        for obj in board.piecedict.values():
            sprite = self.sprites[f"{obj.short}"]
            square = self.canvasdict[f"{obj.position}"]
            square.img = tk.PhotoImage(file=f"ressources/sprites/{sprite}.png")
            square.create_image(50, 50, image=square.img)
            print(f"DRAWN {sprite} at {obj.position}")
            # square.img = tk.PhotoImage(file="ressources/sprites/blackKing.png")
            # square.create_image(50, 50, image=square.img)

    def colorGreen(self, event):
        square = event.widget
        color = self.colors["whiteGreen"] if (
            square.file + square.rank) % 2 == 0 else self.colors["blackGreen"]
        square.configure(background=color)

    def colorRed(self, event):
        square = event.widget
        color = self.colors["whiteRed"] if (
            square.file + square.rank) % 2 == 0 else self.colors["blackRed"]
        square.configure(background=color)

    def initCanvases(self, board):
        for i in range(board.height):
            for j in range(board.width):
                color = self.colors["white"] if (
                    i + j) % 2 == 0 else self.colors["black"]
                self.x = tk.Canvas(self.canvasArea, width=100, height=100,
                                   background=color, highlightthickness=0)
                self.x.create_text(8, 92, fill="#ffffff",
                                   font="FiraMono 8 bold",
                                   text=f"{board.files[i]}{board.ranks[j]}")
                self.x.grid(row=board.width-j,column=i)
                self.x.bind("<Button-1>", self.colorGreen)
                self.x.bind("<Button-2>", self.colorRed)
                self.x.bind("<Button-3>", self.colorNormal)
                self.x.name = f"{board.files[i]}{board.ranks[j]}"
                self.x.file = i
                self.x.rank = j
                self.canvasdict[self.x.name] = self.x


if __name__ == '__main__':
    chessboard = chessboard.Chessboard(8, 8)  # dummyboard
    chessboard.initPieces()
    GUI(chessboard)
