from turtle import Turtle, Screen
import time
screen= Screen()

user_bet = screen.textinput(title="Level", prompt="choose your level: easy, medium, hard: ")

class Level(Turtle):

    def __init__(self):
        super().__init__()

    def levle():
        if user_bet == "easy":
            time.sleep(0.1)
        elif user_bet == "medium":
            time.sleep(0.08)
        elif user_bet == "hard":
            time.sleep(0.04)
        else:
            time.sleep(0.08)

