#making a flower that grows

#make turtle
import turtle as t

#define pen
pen = t.Turtle()

# slow pen speed for I can see growth
pen.speed(2)

#size of pen
t.pensize(2)

#make variables
petals_drawn = 0
max_petals = 8
angle = 360 / max_petals

#draw petals
def draw_petal():
    t.pencolor("purple")
    t.fillcolor("purple")
    t.begin_fill()
    t.circle(100 , 60)
    t.left(100)
    t.circle(100 , 60)
    t.end_fill()

# Petal loop
for i in range(max_petals):
    draw_petal()
    # My if condition - grow the flower by moving outward slightly
    if i % 2 == 0:
        pen.penup()
        pen.goto(-20, -50 - i*2)
        pen.pendown()

# draw a circle
t.pencolor("yellow")
t.fillcolor("yellow")
t.begin_fill()
t.circle(15, 360)
t.end_fill()


# create screen object and make it persist
wn = t.Screen()
wn.mainloop()