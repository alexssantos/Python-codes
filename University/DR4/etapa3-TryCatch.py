
''' Validações: 
    - melhor forma: montar um modulo para tratar somente essas exceções do seu programa. 

'''

while True:
    try:
        x = int(input("Entre com um número: "))
        break
    except ValueError:  # ERRO EXPECIFICO
        print("Valor inválido. Tente novamente.")
    except Exception:   # ERRO GERAL
        print("Houve um problema com o numero obtido. Try Again!")
print("\n ==>  "
        "1% de", x, "é:", x/100, end='\n\n')
