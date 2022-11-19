# Snake Game inspired from the game "Snake Xenzia" on Nokia Phones
# reference: https://www.youtube.com/watch?v=bfRwxS5d0SI

from tkinter import *
import random 

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
SPEED = 75
SIZE = 25
BODY = 3
SNAKE_COLOR = "#964B00"
FOOD_COLOR= "#FA8128"
BACKGROUND = "#A9BA9D"


window = Tk()
window.title("Snake Pasensya")
window.resizable(False, False)

score = 0
directions = "down"

label = Label (window, text = "Highest Score:{}".format(score), font=("Comic Sans MS", 15) )
label.pack()
label = Label (window, text = "Score:{}".format(score), font=("Comic Sans MS", 25) )
label.pack()

canvas = Canvas(window, bg=BACKGROUND, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
canvas.pack()


window.mainloop()