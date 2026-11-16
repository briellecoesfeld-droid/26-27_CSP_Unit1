# a121_catch_a_turtle.py
#-----import statements-----

import turtle as trtl

import random as rand

#-----game configuration----

spot_size = 2
spot_shape = "circle"
spot_color = "pink"
score = 0

#-----initialize turtle-----

spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

#-----game functions--------
def update_score():
    global score
    score += 1
    print(score)

def score_writer():

def spot_clicked(x, y):
   change_position()
   update_score()

def change_position():
   new_xpos = rand.randint(-200, 200)
   new_ypos = rand.randint(-150, 150)
   spot.penup()
   spot.hideturtle()
   spot.goto(new_xpos, new_ypos)
   spot.pendown()
   spot.showturtle()

#-----events----------------

spot.onclick(spot_clicked)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()