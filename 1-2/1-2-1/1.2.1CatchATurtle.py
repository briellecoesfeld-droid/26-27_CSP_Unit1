# a121_catch_a_turtle.py
#-----import statements-----

import turtle as t

#-----game configuration----

t.shapesize(2)
t.shape("circle")
t.fillcolor("red")
t.spot_color = "pink"

#-----initialize turtle-----

t.Turtle()

#-----game functions--------

def spot_clicked(x, y):
   print("Spot was clicked!")

t.onclick(spot_clicked)
#-----events----------------



# create screen object and make it persist
wn = t.Screen()
wn.mainloop()