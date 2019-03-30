a = str.split(input('Digite a BASE: '))
b = str.split(input('Digite o EXPOENTE: '))

base = int(a)
exp = int(b)


def potencia(A, B):
    total = 1
    for i in range(B):
        total *= A
    return total


result = potencia(base, exp)
print(base, "^", exp, ' = ', result)
