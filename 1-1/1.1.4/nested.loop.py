import turtle as trtl

# define the color variables
color1 = "orange"
color2 = "purple"

# define the screen
wn = trtl.Screen()
width = 400
height = 300

# define the turtle
painter = trtl.Turtle()

# defining how fast turtle goes
painter.speed(0)

#turtle color
painter.color(color1)

# start assuming we will draw
answer = "y"
# loop until the user is bored
while (answer == "y"):
    #erase what is on current window
    wn.clearscreen()
    # start in the middle
    painter.goto(0, 0)

    # set up the space counter
    space = 1

    #asking user for angle
    angle = int(input("angle:"))
    seg = int(360 / angle)

    while painter.ycor() < height:
        if space % 100 == 0:
            painter.fillcolor(color2)
            painter.color(color2)
        if space % 200 == 0:
            painter.fillcolor(color1)
            painter.color(color1)

        painter.right(angle)
        painter.forward(2 * space + 10)  # experiment
        painter.begin_fill()
        painter.circle(3)
        painter.end_fill()
        space = space + 1

    answer = input("again?")

wn.bye()

#   a114_nested_loops_4.py
import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

x = -200
y = 0
move_x = 1
move_y = 1
while (x < 0):

    while (y < 100):
        x = x + move_x
        y = y + move_y
        painter.goto(x, y)
    move_y = -1
