import tkinter as tk
import main


class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.max_rounds = tk.IntVar()
        self.player_1 = tk.StringVar()
        self.player_2 = tk.StringVar()
        self.name_1 = tk.StringVar()
        self.name_2 = tk.StringVar()
        self.game_mode = tk.StringVar()
        self.max_rounds.set(3)
        self.player_1.set("human")
        self.player_2.set("computer")
        self.game_mode.set("rps")
        self.name_1.set("Player1")
        self.name_2.set("Computer")
        self.title = tk.Label(text="Rock Paper Scissors game")
        self.get_settings()

    def get_settings(self):
        try:
            self.frame.pack_forget()
        except:
            pass
        self.frame = SetUpFrame(self)
        self.frame.pack()

    def start_game(self):
        self.frame.pack_forget()
        self.frame = GameFrame(self)
        self.frame.pack()

    def end_game(self):
        self.frame.pack_forget()
        self.frame = ResultsFrame(self)
        self.frame.pack()

class SetUpFrame(tk.Frame):
    def __init__(self, master: Game):
        super().__init__()
        self.master = master
        self.max_rounds_title = tk.Label(self, text="Maximum rounds:")
        self.player_1_title = tk.Label(self, text="Player 1:")
        self.player_2_title = tk.Label(self, text="Player 2:")
        self.mode_title = tk.Label(self, text="Mode")
        self.player_type1 = [tk.Radiobutton(self, text=typ,
                                            value=typ)
                             for typ in ["computer", "human"]]
        self.player_type2 = [tk.Radiobutton(self, text=typ,
                                            variable=self.master.player_2,
                                            value=typ)
                             for typ in ["computer", "human"]]
        self.mode = [tk.Radiobutton(self, text=typ,
                                    variable=self.master.game_mode,
                                    value=typ)
                     for typ in ["rps", "rpsls"]]
        self.get_name_1 = tk.Entry(self, textvariable=self.master.name_1)
        self.get_name_2 = tk.Entry(self, textvariable=self.master.name_2)
        self.max_rounds = tk.Scale(self, from_=1, to=10, orient="horizontal", variable=self.master.max_rounds,
                                   length=200)
        self.play_button = tk.Button(self, text="Play!", bg="powder blue", command=self.master.start_game)
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
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.select_choice_txt = tk.StringVar()
        self.round_num = tk.IntVar()
        self.select_choice_txt.set("Option")
        self.round_num.set(1)
        self.player_1_title = tk.Label(self, text="Player 1")
        self.player_2_title = tk.Label(self, text="Player 2")
        self.type_1 = "human"
        self.type_2 = "computer"
        self.choices = ["rock", "paper", "scissors"]
        self.score = tk.Label(self, text="1:0")
        self.round_message = tk.Label(self, text=f"round {self.round_num.get()} of {self.master.max_rounds.get()}")
        self.submit = tk.Button(self, text="submit", bg="powder blue", command=self.next_round)
        if self.type_1 == "human":
            self.choice1 = tk.OptionMenu(self, self.select_choice_txt, *self.choices)
        else:
            self.choice2 = tk.Label(self, text="Computer choice")
        if self.type_2 == "human":
            self.choice2 = tk.OptionMenu(self, self.select_choice_txt, *self.choices)
        else:
            self.choice2 = tk.Label(self, text="Computer choice")
        self.place_widgets()

    def next_round(self):
        if self.round_num.get() == self.master.max_rounds.get():
            self.master.end_game()
        else:
            self.round_num.set(self.round_num.get()+1)
            self.round_message = tk.Label(self, text=f"round {self.round_num.get()} of {self.master.max_rounds.get()}")
            self.place_widgets()
    def place_widgets(self):
        self.player_1_title.grid(row=0, column=0)
        self.player_2_title.grid(row=0, column=2)
        self.score.grid(row=0, column=1)
        self.choice1.grid(row=1, column=0)
        self.choice2.grid(row=1, column=2)
        self.submit.grid(row=2, column=1)
        self.round_message.grid(row=3, column=1)


class ResultsFrame(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.player_names = tk.Label(self, text=f"{self.master.name_1.get()} vs. {self.master.name_2.get()}")
        self.score = tk.Label(self, text="0:1   The winner is player 2")
        self.play_again = tk.Label(self, text=f"Play again?")
        self.yes_button = tk.Button(self, text="yes", bg="powder blue", command=self.master.start_game)
        self.no_button = tk.Button(self, text="no", bg="powder blue", command=self.master.get_settings)
        self.place_widgets()

    def place_widgets(self):
        self.player_names.grid(row=0, column=0)
        self.score.grid(row=1, column=0)
        self.play_again.grid(row=2, column=0)
        self.yes_button.grid(row=2, column=1)
        self.no_button.grid(row=2, column=2)


if __name__ == "__main__":
    app = Game()
    app.mainloop()
