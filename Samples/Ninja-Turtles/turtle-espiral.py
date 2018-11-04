import turtle

N = int(input("Entre com o valor N: "))
count = 0

while count <= N:
    count += 1
    turtle.forward(count)
    turtle.left(89)

input()
