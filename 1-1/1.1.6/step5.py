# CODE TO ADD
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
painter.pensize(40)

# create spider body
painter.circle(20)

# number of legs
legs = 8

# configure legs
length_of_legs = 70
leg_angle = 360 / legs -20
painter.pensize(5)

# draw legs 1-4
n = 0
while (n < legs):
  painter.goto(0,20)
  if n<= 3:
    painter.setheading(leg_angle*n-45)
  if n> 3:
    painter.setheading(leg_angle*n+45)
  painter.forward(length_of_legs)
  n = n + 1

# configure and draw eyes
painter.pensize(6)
painter.color("red")

#moving to first eye
painter.penup()
painter.goto(-5,50)
painter.pendown()

# draw first eyue
painter.circle(5)

# move to second eye
painter.penup()
painter.goto(5,50)
painter.pendown()

painter.circle(5)

painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()