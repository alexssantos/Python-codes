n = int(input("Calcular o Fatorial de :"))

if n < 0:
    print(n, "é menor que 0. Namos calcular: ", -n, "!")
    n = abs(n)  # somente positivo

result = 1
for numb in range(1, n+1):
    result *= numb
    print(numb, " x ", end=' ')

print(end='\n')
print(n, "! = ", result)
