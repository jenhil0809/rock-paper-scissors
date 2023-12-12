from random import choice
from pyinputplus import inputMenu

RULES = {"rps": {"rock": ["scissors"],
                 "paper": ["rock"],
                 "scissors": ["paper"],
                 },
         "rpsls": {"rock": ["scissors", "lizard"],
                   "paper": ["rock", "spock"],
                   "scissors": ["paper", "lizard"],
                   "lizard": ["paper", "spock"],
                   "spock": ["rock", "scissors"], }}


class PlayerObject:
    def __init__(self, name, rules=None):
        if rules is None:
            rules = RULES["rps"]
        self.name = name.lower()
        self.rules = rules
        self.allowed_objects = [objct for objct in rules.keys()]

    def __repr__(self):
        return f"PlayerObject({self.name})"

    def __gt__(self, other):
        return other.name in self.rules[self.name]

    def __eq__(self, other):
        return self.name == other.name

    def random_object(self):
        return choice(self.allowed_objects)


class Player:
    def __init__(self, name, player_object: PlayerObject):
        self.name = name.capitalize()
        self.score = 0
        self.current_object = None
        self.player_object = player_object

    def reset_object(self):
        self.current_object = None

    def win_round(self):
        self.score += 1

    def __repr__(self):
        return f"Player({self.name}, {self.score}, {self.current_object})"


class HumanPlayer(Player):
    def __init__(self, name, player_object: PlayerObject):
        super().__init__(name, player_object)

    def choose_object(self):
        self.current_object = inputMenu(self.player_object.allowed_objects, "choice: \n")


class ComputerPlayer(Player):
    def __init__(self, player_object: PlayerObject):
        super().__init__("Computer", player_object)

    def choose_object(self):
        self.current_object = self.player_object.random_object()


class Game:
    def __init__(self, name, rules):
        self.current_round = 1
        self.max_rounds = 3
        self.players = []
        self.round_result = None
        self.round_winner = None
        self.player_object = PlayerObject(name, RULES[rules])

    def add_human_player(self, name):
        x = HumanPlayer(name, self.player_object)
        self.players.append(x)

    def add_computer_player(self):
        x = ComputerPlayer(self.player_object)
        self.players.append(x)

    def set_max_rounds(self, val):
        if val.isinstance(int):
            self.max_rounds = val
        else:
            print("must be an integer")

    def find_winner(self):
        if self.players[0].current_object is not None and self.players[1].current_object is not None:
            if self.players[0].current_object == self.players[1].current_object:
                self.round_result = "Draw"
            elif self.players[0].current_object > self.players[1].current_object:
                self.round_result = "Win"
                self.round_winner = self.players[0].name
                self.players[0].win_round()
            else:
                self.round_result = "Win"
                self.round_winner = self.players[1].name
                self.players[1].win_round()

    def next_round(self):
        self.current_round += 1
        self.round_result, self.round_winner = None, None
        for player in self.players:
            player.reset_object()

    def is_finished(self):
        if self.current_round > int(self.max_rounds):
            return True
        else:
            return False

    def reset(self):
        self.current_round = 1
        for player in self.players:
            player.score = 0

    def report_round(self):
        for player in self.players:
            print(f"{player.name} chose {player.current_object}")
        if self.round_result == "Draw":
            print("It was a draw")
        else:
            print(f"{self.round_winner} won")

    def report_score(self):
        for player in self.players:
            print(f"{player.name} has {player.score} points")

    def report_winner(self):
        if self.players[0].score == self.players[1].score:
            print("The game is a draw")
        elif self.players[0].score > self.players[1].score:
            print(f"{self.players[0].name} won the game")
        else:
            print(f"{self.players[1].name} won the game")


class CLInterface:
    def __init__(self):
        self.mode = inputMenu(["rps", "rpsls"], "rps or rpsls?\n")
        self.game = Game("Game", self.mode)

    def set_up(self):
        for i in range(2):
            typ = inputMenu(["computer", "human"], "Computer/human?\n")
            if typ == "human":
                name = input("Name: ")
                self.game.add_human_player(name)
            else:
                self.game.add_computer_player()
        self.set_max_rounds()

    def set_max_rounds(self):
        val = " "
        while not val.isdecimal():
            val = input("Maximum rounds: ")
        self.game.max_rounds = val

    def get_choices(self):
        for player in self.game.players:
            player.choose_object()

    def run_game(self):
        while not self.game.is_finished():
            self.game.next_round()
            self.get_choices()
            self.game.find_winner()
            self.game.report_round()
            self.game.report_score()
            print("------")
        self.game.report_winner()

    def run_sequence(self):
        while True:
            self.set_up()
            while not (input("Do you want to play again?").lower()[0] == "n"):
                self.run_game()
                self.game.reset()
            print("You have quit the game")


if __name__ == "__main__":
    cli_interface = CLInterface()
    cli_interface.run_sequence()
