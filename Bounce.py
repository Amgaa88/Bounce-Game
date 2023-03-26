#Creating game canvas
from tkinter import *
import random
import time

#Creating the ball class
# 1-Create a class called Ball that takes parameters for the canvas and the color of the ball we’re going to draw.

# 2-Save the canvas as an object variable because we’ll draw our ball on it.

# 3-Draw a filled circle on the canvas using the value of the color parameter as the fill color.

# 4-Save the identifier that tkinter returns when it draws the circle (oval) because we’re going use this to move the ball around the screen.

# 5-Move the oval to the middle of the canvas.
#Adding some action- We'll make it move, bounce, and change direction
#Making the ball move

class Ball: #Ball class
    def __init__(self, canvas, paddle, color): #Create an initialization function parameters-canvas, colors
        self.canvas=canvas #object variable 'canvas' to the value of the parameter canvas
        self.paddle=paddle #assign paddle parameter to the object variable paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color) #we call the create oval function with five parameters x,y coordinates for the top left corner. x, y for the bottom right corner. the fill color for the oval
        #The create_oval function returns an identifier for the shape that is drawn, which we store in the object variable id. 
        self.canvas.move(self.id, 245, 100) #we move the oval to the middle of the canvas (position 245, 100), and the canvas knows what to move, cuz we use the stored shape identifier(the object variable id)
        starts=[-3,-2,-1,1,2,3] #we create variable starts with a list of six numbers. 
        random.shuffle(starts) #mix them up the list
        self.x=starts[0] #we set the variable x to 0, and then with we set the variable y to -1 #we set the value of x to the first item in the list
        self.y=-3 
        self.canvas_height=self.canvas.winfo_height() #winfo height function returns the current height of the canvas
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False
    def hit_paddle(self, pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
            return False
    def draw(self):
        self.canvas.move(self.id, self.x,self.y) # we call to canvas's move function by passing the object variables x and y. 
        pos=self.canvas.coords(self.id) #we create a variable called 'pos' by calling the canvas function coords. This function returns the current x and y coordinates of anything drawn on the canvas
        #The coords function returns the coordinates as a list of four numbers. The first 2 numbers in the list contain top-left coordinates of the oval (x1, y1), the second 2 are the bottom-right
        #x2, y2 
        if pos[1]<=0: #if the y1 coordinate (that's the top of the ball) is less than or equal to 0. if so, we set the y object to 1. we're saying if you hit the top of the screen, stop subtracting one 
            #from the vertical position, and therefore stop moving up. 
            self.y=3
        if pos[3]>=self.canvas_height: #if the y2 coordinate (that's the bottom of the ball) is greater than or equal to the variable canvas_height
            self.hit_bottom=True # we set the y object variable back to -1. 
        if self.hit_paddle(pos)==True:
            self.y=-3
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
    
class Paddle:
    def __init__(self, canvas, color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id, 200,300)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        elif pos[2]>=self.canvas_width:
            self.x=0
    def turn_left(self, evt):
        self.x=-2
    def turn_right(self, evt):
        self.x=2

#Making the paddle move
#To make the paddle move left and right, we'll use event bindings to bind the left and right arrow keys to the new functions in the Paddle class
#when the player presses the left arrow key, the x variable will be set to -2 (to move left)
#Pressing the right arrow key set the x variable to 2 (to move right)



tk=Tk()
tk.title('Game')
tk.resizable(0,0) # to make the window a fixed size, the parameter 0,0 say the size of the window cannot be changed either horizontally or vertically
tk.wm_attributes('-topmost', 1) #place the window containing our canvas in front of all other windows ('-topmost)

canvas=Canvas(tk, width=500, height=400, bd=0, highlightthickness=0) #canvas object bd=0, no border
canvas.pack() #to size itself according to height and width parameters
tk.update() #tkinter to initialize itself for the animation in our game

#Creating object
paddle=Paddle(canvas, 'blue')
ball=Ball(canvas, paddle, 'red')

#To stop the window from closing immediately we need to add an animation loop, which is called the main loop of our game
while 1:
    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks() #move the ball a little
    tk.update() #redraw the screen with the new position
    time.sleep(0.01) #sleep for a moment














