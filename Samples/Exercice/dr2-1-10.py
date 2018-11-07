import turtle

lado = int(input("Digite o tamanho do lado do quadrado: "))
turtle.speed('slowest')

for x in range(4):
    turtle.forward(lado)
    turtle.right(90)
