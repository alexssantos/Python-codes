import turtle

turtle.speed(1)
turtle.title("Utilizando nossas Funções! Q - Quadrado | T - triângulo | C - Círculo")


def quadrada():
    for x in range(4):
        turtle.forward(200)
        turtle.right(90)


def triangulo():
    for x in range(1, 4):
        turtle.forward(200)
        turtle.setheading(120*x)


def circulo():
    turtle.circle(50)


turtle.listen()

turtle.onkey(quadrada, 'q')
turtle.onkey(triangulo, 't')
turtle.onkey(circulo, 'c')

turtle.Screen().mainloop()
