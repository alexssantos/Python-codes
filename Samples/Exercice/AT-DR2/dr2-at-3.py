numbers = str.split(input(print('Digite a base e o expoente: ')))
numbers = [int(x) for x in numbers]


def potencia(A, B):
    return A**B


result = potencia(numbers[0], numbers[1])
print(result)