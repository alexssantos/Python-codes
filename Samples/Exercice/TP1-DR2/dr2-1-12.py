import turtle

raio = int(input("Digite o valor [20 ~ 50]  do Raio:  "))
turtle.penup()           # mover do centro pro raio
turtle.setheading(0)
turtle.fd(raio*5)
turtle.setheading(90)
turtle.pendown()
turtle.circle(raio*5)

turtle.Screen().mainloop()