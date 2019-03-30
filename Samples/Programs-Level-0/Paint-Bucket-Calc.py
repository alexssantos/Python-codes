area = int(input("Qual a quantidade de m² a ser pintado? "))


# 1L = 3m²
litros = area // 3      # divisão INTEIRA

if (litros % 3 > 0):    # se restar area, completar com mais 1L
    litros += 1

print("litros de tinta: ", litros, "L")
latas = litros//18

if litros % 18 > 0:
    latas += 1

print("Latas de tinta: ", latas)

preco = latas * 80
print("valor: R$", preco)