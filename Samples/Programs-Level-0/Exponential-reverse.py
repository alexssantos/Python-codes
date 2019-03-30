import math

base = int(input("Digite a base: "))
exp = int(input("Digite o expoente: "))


def calcExp(base, exp):
    result = 1

    # base negativa
    if base < 0 and exp % 2 == 0:
        base = abs(base)

    count = abs(exp)
    while count > 0:
        if exp < 0:
            result *= 1/base
        else:
            result *= base
        count -= 1
    return result


result = calcExp(base, exp)
print("Normal: ", base, " ^ ", exp, " = ", float(result))
print("gabarito: ", math.pow(base, exp))
result = calcExp(exp, base)
print("Inverso: ", exp, " ^ ", base, " = ", float(result))
print("gabarito: ", math.pow(exp, base))
