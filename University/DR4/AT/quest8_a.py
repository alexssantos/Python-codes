''' # DR4-AT
    8. Escreva 3 programas em Python que resolva o seguinte problema: 
    Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B.        
        
Para calcular o fatorial, utilize a seguinte função:
---------------------
def fatorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)
---------------------

        Os modos de desenvolver seu programa devem ser:
        a) sequencialmente (sem concorrência);
        b) usando o módulo threading com 4 threads;
        c) usando o módulo multiprocessing com 4 processos.

RESULTADOS:

-----------------------------
Tempo total: 637.58 s
N = 10.000.000
-----------------------------
Tempo total: 322.74 s
N = 5.000.000
-----------------------------
Tempo total: 61.97 s
N = 1.000.000
=============================

-----------------------------
Tempo total: 184.54 s
N = 10.000.000
-----------------------------
Tempo total: 18.31 s
N = 1.000.000
-----------------------------
Tempo total: 2.2 s
N = 100.000
-----------------------------
Tempo total: 1.94 s
N = 10.000


'''

# A) SEQUENCIAL
import time
import random


def print_final_result(t_inicio):
    # Captura tempo final
    t_fim = float(time.time())
    t_total = round(t_fim - t_inicio, 2)
    # Imprime o resultado e o tempo de execução
    print(f"Tempo total: {t_total} s")


def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):         # range(start, stop, step)
        fat = fat * i
    return(fat)


N = 10000000
# Captura tempo inicial
t_inicio = float(time.time())       #timestamp
# Gera lista com valores aleatórios
vetA = []
# Add valores entre -50 e 50
for i in range(N):
    vetA.append(random.randint(30, 50))
# Faz o cálculo da soma dos valores do vetor/lista
vetB = []
for i in vetA:
    vetB.append(fatorial(i))
print_final_result(t_inicio)
print(f'N = {N}')