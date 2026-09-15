# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
painter.pensize(5)

# change pensize
size = int(input("What do you want the size of the pen to be?"))
painter.pensize(size)

# move turtle without marking a line
painter.penup()
painter.goto(0, 0)
painter.pendown()

# draw a circle
painter.circle(100, 360)

# make left eye
painter.penup()
painter.goto(-30, 120)
painter.pendown()

# draw small circle for left eye
painter.circle(15, 360)

# make left eye pupil
painter.circle(5, 360)

# fill eye color
fillcolor = "blue"
painter.fillcolor(fillcolor)
painter.penup()

# make right eye
painter.penup()
painter.goto(30, 120)
painter.pendown()

# draw small circle for right eye
painter.circle(15, 360)

# make right eye pupil
painter.circle(5, 360)

# fill eye color
fillcolor = "blue"
painter.fillcolor(fillcolor)
painter.penup()

# move pen to start making smile
painter.penup()
painter.goto(-60, 70)
painter.pendown()

#draw line for mouth
painter.right(90)
painter.circle(60, 180)

#make nose
painter.penup()
painter.goto(0, 90)
painter.right(180)
painter.pendown()
painter.circle(15, 90)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()