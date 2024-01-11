import tkinter as tk
import main


class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = tk.Label(text="Rock Paper Scissors game")
        self.title.pack()
        self.frame = SetUpFrame()
        self.frame.pack()
        self.frame = GameFrame()
        self.frame.pack()
        self.frame = ResultsFrame()
        self.frame.pack()


class SetUpFrame(tk.Frame):
    def __init__(self):
        super().__init__()
        self.player_1 = tk.StringVar()
        self.player_2 = tk.StringVar()
        self.name_1 = tk.StringVar()
        self.name_2 = tk.StringVar()
        self.max_rounds = tk.IntVar()
        self.game_mode = tk.StringVar()
        self.player_1.set("human")
        self.player_2.set("computer")
        self.max_rounds.set(3)
        self.game_mode.set("rps")
        self.name_1.set("Player1")
        self.name_2.set("Computer")
        self.max_rounds_title = tk.Label(self, text="Maximum rounds:")
        self.player_1_title = tk.Label(self, text="Player 1:")
        self.player_2_title = tk.Label(self, text="Player 2:")
        self.mode_title = tk.Label(self, text="Mode")
        self.player_type1 = [tk.Radiobutton(self, text=typ,
                                            value=typ)
                             for typ in ["computer", "human"]]
        self.player_type2 = [tk.Radiobutton(self, text=typ,
                                            variable=self.player_2,
                                            value=typ)
                             for typ in ["computer", "human"]]
        self.mode = [tk.Radiobutton(self, text=typ,
                                    variable=self.game_mode,
                                    value=typ)
                     for typ in ["rps", "rpsls"]]
        self.get_name_1 = tk.Entry(self, textvariable=self.name_1)
        self.get_name_2 = tk.Entry(self, textvariable=self.name_2)
        self.max_rounds = tk.Scale(self, from_=1, to=10, orient="horizontal", variable=self.max_rounds,
                                   length=200)
        self.play_button = tk.Button(self, text="Play!", bg="powder blue")
        self.place_widgets()

    def place_widgets(self):
        self.max_rounds_title.grid(row=0, column=0)
        self.max_rounds.grid(row=0, column=1, columnspan=3)
        self.player_1_title.grid(row=1, column=0)
        self.player_2_title.grid(row=2, column=0)
        self.mode_title.grid(row=3, column=0)
        for i in range(len(self.player_type1)):
            self.player_type1[i].grid(row=1, column=i + 1)
            self.player_type2[i].grid(row=2, column=i + 1)
        self.get_name_1.grid(row=1, column=3, padx=5)
        self.get_name_2.grid(row=2, column=3, padx=5)
        self.play_button.grid(row=3, column=3)
        for i in range(2):
            self.mode[i].grid(row=3, column=i + 1)


class GameFrame(tk.Frame):
    def __init__(self):
        super().__init__()

    def place_widgets(self):
        pass


class ResultsFrame(tk.Frame):
    def __init__(self):
        super().__init__()

    def place_widgets(self):
        pass


if __name__ == "__main__":
    app = Game()
    app.mainloop()
