# a121_catch_a_turtle.py
#-----import statements-----

import turtle as trtl

import random as rand

#-----game configuration----

trtl.bgcolor("light blue")
spot_size = 2
spot_shape = "circle"
spot_color = "pink"
starter_size = 2
starter_shape = "circle"
starter_color = "red"
score = 0
font_setup = ("Ariel", 20, "normal")
#-----countdown variables-----
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
has_started = False

#-----initialize turtle-----

spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(200, 200)

counter =  trtl.Turtle()
counter.penup()
counter.hideturtle()
counter.goto(200, 150)

starter_turtle = trtl.Turtle()
starter_turtle.penup()
starter_turtle.goto(200, 100)
starter_turtle.shape(starter_shape)
starter_turtle.shapesize(starter_size)
starter_turtle.fillcolor(starter_color)

#-----game functions--------

def start_game(x, y):
    global has_started
    has_started = True
    wn.ontimer(countdown, counter_interval)

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def change_position():
   new_xpos = rand.randint(-200, 200)
   new_ypos = rand.randint(-150, 150)
   spot.penup()
   spot.hideturtle()
   spot.goto(new_xpos, new_ypos)
   spot.pendown()
   spot.showturtle()

def spot_clicked(x, y):
   global timer_up
   global has_started
   if timer_up== False and has_started == True:
       change_position()
       update_score()
   else:
       spot.hideturtle()

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)


#-----events----------------

starter_turtle.onclick(start_game)

spot.onclick(spot_clicked)

wn = trtl.Screen()

# create screen object and make it persist

wn.mainloop()