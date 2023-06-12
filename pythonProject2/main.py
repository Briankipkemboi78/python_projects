import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('blue')

colors = ["cornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
          "wheat", "SlateGray", "SeaGreen"]
timmy.pensize(10)
timmy.speed("fast")


directions = [ 0, 90, 180, 270]
for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))










screen = Screen()
screen.exitonclick()
