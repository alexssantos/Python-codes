import turtle

lado = int(input("Digite o tamanho do lado do quadrado: "))
turtle.speed(1)     # slowest

for x in range(4):
    turtle.forward(lado)
    turtle.right(90)

turtle.Screen().mainloop()