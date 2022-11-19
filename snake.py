# Snake Game inspired from the game "Snake Xenzia" on Nokia Phones
# reference: https://www.youtube.com/watch?v=bfRwxS5d0SI

from tkinter import *
import random 

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
SPEED = 75
SIZE = 50
BODY = 3
SNAKE_COLOR = "#964B00"
FOOD_COLOR= "#FA8128"
BACKGROUND = "#A9BA9D"


window = Tk()
window.title("Snake Pasensya")
window.resizable(False, False)

