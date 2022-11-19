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
    shape = canvas.create_arc(x,y,x+SIZE,y+SIZE,start =0, extent =270, outline = "black",fill=SNAKE_COLOR)
    snake.shape.insert(0,shape)

    if x==food.coordinates[0] and y ==food.coordinates[1]:
        global score
        score += 1 
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.shape[-1])
        del snake.shape[-1]

    if check(snake):
        over()
    
    else:
        window.after(SPEED, turn, snake, food)

def direction(new_direction):
    global directions

    if new_direction == "left":
       if directions != "right":
            directions = new_direction
    elif new_direction == "right":
       if directions != "left":
            directions = new_direction   
    elif new_direction == "up":
       if directions != "down":
            directions = new_direction     
    elif new_direction == "down":
       if directions != "up":
            directions = new_direction  



def check(snake):
    x,y = snake.coordinates[0]
    if x<0 or x>= WINDOW_WIDTH:
        print ("GAME OVER")
        return True
    if y<0 or y>= WINDOW_HEIGHT:
        print ("GAME OVER")
        return True
    for body_part in snake.coordinates [1:]:
        if x==body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True
    return False

def exit_program():
    window.destroy()

def over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("Comic Sans MS",50), text= "GAME OVER", fill="white", tag="gameover")
    



window = Tk()
window.title("Snake Pasensya")
window.resizable(False, False)

score = 0
directions = "down"


label = Label (window, text = "Controls \n left arrow - left | right arrow - right \n up arrow - up   | down arrow -down", font=("Comic Sans MS", 15) )
label.pack()
btn = Button(window, text="Exit", command=exit_program)
btn.pack()

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

window.bind('<Left>', lambda event : direction('left'))
window.bind('<Right>', lambda event : direction('right'))
window.bind('<Up>', lambda event : direction('up'))
window.bind('<Down>', lambda event : direction('down'))

snake = Snake()
food = Food()

turn(snake,food)

window.mainloop()