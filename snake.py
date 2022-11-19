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
    def __init__ (self):
        self.body_size = BODY
        self.coordinates = []
        self.shape =[]

        for i in range(0, BODY):
            self.coordinates.append([0,0])
        
        for x, y in self.coordinates:
            shape = canvas.create_arc(x,y,x+SIZE,y+SIZE, start =0, extent =270, outline = "black",fill=SNAKE_COLOR, tag ="snake")
            self.shape.append(shape)

class Food:
     def __init__(self):
        x = random.randint(0, (WINDOW_WIDTH/SIZE)-1) * SIZE
        y = random.randint(0, (WINDOW_HEIGHT/SIZE)-1) * SIZE
        
        self.coordinates =[x,y]

        canvas.create_oval(x,y,x+SIZE,y+SIZE, fill=FOOD_COLOR,tag="food")

def turn(snake,food):
    x,y = snake.coordinates[0]
    
    if directions =="up":
        y -= SIZE
    
    elif directions == "down":
        y += SIZE

    elif directions == "left":
        x-= SIZE
    
    elif directions == "right":
        x += SIZE

    snake.coordinates.insert(0, (x,y))
    shape = canvas.create_oval(x,y,x+SIZE,y+SIZE, fill="cyan")
    snake.shape.insert(0,shape)

    del snake.coordinates[-1]
    canvas.delete(snake.shape[-1])

    window.after(SPEED, turn, snake, food)

    del snake.shape[-1]

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

turn(snake,food)

window.mainloop()