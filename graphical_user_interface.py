import tkinter as tk
import main


class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = tk.Label(text="Rock Paper Scissors game")
        self.title.pack()
        self.frame = SetUpFrame()
        self.frame.pack()


class SetUpFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        self.max_rounds_title = tk.Label(self, text="Maximum rounds:")
        self.max_rounds = tk.Scale(self, from_=0, to=10, orient="horizontal")
        self.place_widgets()
        self.config(bg='yellow')

    def place_widgets(self):
        # self.max_rounds_title.grid(row=0, column=0)
        # self.max_rounds.grid(row=0, column=1)
        self.max_rounds_title.pack()


if __name__ == "__main__":
    app = Game()
    app.mainloop()
