import turtle

lado = int(input("Lado do Triangulo: "))

turtle.speed('slowest')

for x in range(1, 4):
    turtle.forward(lado)
    turtle.setheading(120*x)

turtle.Screen().mainloop()