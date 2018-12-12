import turtle

# lado = int(input("Digite o tamanho [50 ~ 500] do lado do quadrado: "))
# ladoFirstSquad = 500
lado = 300
turtle.speed('slowest')

# Go To Center


def makeCircle(wall):
    raio = (wall*0.8)/2
    # mover do centro pro raio
    turtle.penup()
    turtle.setheading(0)
    turtle.fd(raio)
    turtle.setheading(90)
    turtle.pendown()
    # desenhar
    turtle.circle(raio)
    # mover para centro
    # mover para o centro


def makeSquad(wall):
    lado = wall*0.8

    turtle.penup()
    turtle.setheading(0)
    turtle.fd(lado/2)
    turtle.setheading(270)
    turtle.fd(lado/2)
    turtle.setheading(180)
    turtle.pendown()
    drawSquad(lado)


def drawSquad(lado):
    for x in range(4):
        turtle.fd(lado)
        turtle.right(90)


def centerNextDraw(wall, time, center: list):
    # precisa estar no centro
    turtle.penup()
    if time == 1:
        turtle.setheading(180)
        turtle.fd(wall/2)
        turtle.setheading(90)
        turtle.fd(wall/2)

    elif time == 2:
        turtle.setheading(0)
        turtle.fd(wall/2)
        turtle.setheading(90)
        turtle.fd(wall/2)

    elif time == 3:
        turtle.setheading(0)
        turtle.fd(wall/2)
        turtle.setheading(-90)
        turtle.fd(wall/2)

    elif time == 4:
        turtle.setheading(180)
        turtle.fd(wall/2)
        turtle.setheading(270)
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


center = [0, 0]
main(lado, center)

turtle.Screen().mainloop()


# def getQuadrant(center):
#     x = center[0]
#     y = center[1]
#     if x == 0 and y == 0:
#         return 0
#     if x > 0 and y > 0:
#         return 1
#     if x < 0 and y > 0:
#         return 2
#     if x < 0 and y < 0:
#         return 3
#     if x > 0 and y < 0:
#         return 4
