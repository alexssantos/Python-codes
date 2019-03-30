n = int(input("Calcular o Fatorial de: "))

if n < 0:
    print(n, "é menor que 0. Namos calcular: ", -n, "!")
    n = abs(n)  # somente positivo

result = 1
count = 1
while count <= n:
    result *= count
    print(count, " x ", end=' ')
    count += 1

print(end='\n')
print(n, "! = ", result)