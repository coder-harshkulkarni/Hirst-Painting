import colorgram
import random
import turtle as t

color_list = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    color_list.append(rgb)

timmy = t.Turtle()
timmy.penup()
timmy.hideturtle()
timmy.sety(-350)
timmy.speed("fastest")
t.colormode(255)
for _ in range(15):
    timmy.setx(-400)
    for _ in range(15):
        timmy.forward(50)
        timmy.dot(20, random.choice(color_list))
    timmy.sety(timmy.ycor() + 50)

sc = t.Screen()
sc.exitonclick()
