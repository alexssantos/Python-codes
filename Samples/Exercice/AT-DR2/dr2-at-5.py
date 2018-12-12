import turtle

# lado = int(input("Digite o tamanho [50 ~ 500] do lado do quadrado: "))

lado = 300
center = [0, 0]
turtle.speed('slowest')


def makeCircle(wall):
    radius = (wall*0.8)/2

    turtle.penup()           # mover do centro pro raio
    turtle.setheading(0)
    turtle.fd(radius)
    turtle.setheading(90)
    turtle.pendown()
    drawCircle(radius)


def drawCircle(radius):
    turtle.circle(radius)


def makeSquad(wall):
    side = wall*0.8

    turtle.penup()          # mover do centro pro raio
    turtle.setheading(0)
    turtle.fd(side/2)
    turtle.setheading(270)
    turtle.fd(side/2)
    turtle.setheading(180)
    turtle.pendown()
    drawSquad(side)


def drawSquad(side):
    for x in range(4):
        turtle.fd(side)
        turtle.right(90)


def centerNextDraw(wall, time, center: list):
    # precisa estar no centro
    turtle.penup()
    if time == 1 or time == 4:
        turtle.setheading(180)
        turtle.fd(wall/2)
        if time == 1:
            turtle.setheading(90)
        else:
            turtle.setheading(270)
        turtle.fd(wall/2)

    elif time == 2 or time == 3:
        turtle.setheading(0)
        turtle.fd(wall/2)
        if time == 2:
            turtle.setheading(90)
        else:
            turtle.setheading(-90)
        turtle.fd(wall/2)

    turtle.pendown()


def GoTO(pos: list):
    turtle.penup()
    turtle.goto(pos[0], pos[1])
    turtle.pendown()


def main(wall, center: list):
    GoTO(center)
    # go to center

    for draw in range(1, 5):
        centerNextDraw(wall, draw, center)
        if draw == 2 or draw == 3:
            makeCircle(wall)
        elif draw == 1 or draw == 4:
            makeSquad(wall)
        GoTO(center)
        if draw == 4:
            centerNextDraw(wall, draw, center)

    x, y = turtle.position()
    center = [x, y]
    wall = wall*0.4
    main(wall, center)
    # end at center4 = next MainCenter


main(lado, center)

turtle.Screen().mainloop()
