import turtle

turtle.setup(500, 500, 0, 0)

gap = 0
flag = True

while flag:
    turtle.setheading(gap)
    turtle.forward(200)
    turtle.forward(-200)
    gap += 15
    if gap > 360:
        flag = False
