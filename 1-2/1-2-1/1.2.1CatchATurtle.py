# a121_catch_a_turtle.py
#-----import statements-----

import turtle as trtl

import random as rand

#-----game configuration----

spot_size = 2
spot_shape = "circle"
spot_color = "pink"

#-----initialize turtle-----

spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

#-----game functions--------

def spot_clicked(x, y):
   print("Spot was clicked!")

#-----events----------------

spot.onclick(spot_clicked)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()