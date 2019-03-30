import turtle

colors = ()
quest = "ENTER to EXIT or type an color: "
print("COLORS: red, green, yellow, pink, purple, blue, orange, white,.. \n")
color = input(quest)

while color != "":
    colors += (color, )
    color = input(quest)

turtle.bgcolor('black')
turtle.speed('fastest')

angle = 360//len(colors) + 1

for x in range(360):
    turtle.color(colors[x % len(colors)])
    turtle.forward(x)
    turtle.left(angle)
