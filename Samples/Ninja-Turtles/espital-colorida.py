import turtle

color = ('red', 'purple', 'blue', 'green', 'orange', 'yellow')
turtle.bgcolor('black')
turtle.speed('fastest')
for x in range(360):
    turtle.color(color[x % 3])  # percorre do indice 0 a 2, posiçao 1 a 3
    turtle.forward(x)
    turtle.left(61)
