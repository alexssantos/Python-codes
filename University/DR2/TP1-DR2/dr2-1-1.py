N = int(input("valor de N: "))
N = abs(N)


for numb in range(1, N+1):
    if numb % 2 != 0:
        print(numb, " é impar!")
