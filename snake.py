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

class Snake:
    pass

class Food:
     def __init__(self):
        x = random.radint(0, (WINDOW_WIDTH/SIZE)-1) * SIZE
        y = random.radint(0, (WINDOW_HEIGHT/SIZE)-1) * SIZE
        
        self.coordinates =[x,y]

def turn():
    pass

def direction(new_direction):
    pass

def check():
    pass

def over():
    pass


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

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height =window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()

window.mainloop()