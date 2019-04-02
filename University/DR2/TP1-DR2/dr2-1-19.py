import turtle

numb = int(input("Number of laps: "))
numb *= 4
turtle.speed(0)     # fastest

i = 0
while i < numb:
    turtle.forward(i)
    turtle.right(90)
    i += 1

turtle.Screen().mainloop()
