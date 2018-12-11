import turtle

lado = int(input("Digite o tamanho [50 ~ 500] do lado do quadrado: "))
turtle.speed('slowest')

# square on the center
turtle.penup()
turtle.goto(-lado/2, lado/2)
turtle.pendown()


def make_squad(lado):
    for x in range(4):
        turtle.fd(lado)
        turtle.right(90)
    turtle.penup()
    turtle.fd(lado/2)
    turtle.right(90)
    turtle.fd(lado/2)
    turtle.pendown()
    turtle.left(90)
    lado *= 0.4
    make_squad(lado)


make_squad(lado)
turtle.Screen().mainloop()
