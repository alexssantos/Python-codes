import turtle

# numb = int(input("Number of laps: "))
# numb *= 4
turtle.speed(0)     # fastest
quadrants = ((-150, 150), (150, 150), (150, -150), (-150, -150))


def change_place(point):
    turtle.penup()
    turtle.goto(point)
    turtle.pendown()


for point in quadrants:
    change_place(point)

    numb = quadrants.index(point)
    for i in range(200):
        turtle.forward(i)
        turtle.right(80+(numb*4))

turtle.Screen().mainloop()
