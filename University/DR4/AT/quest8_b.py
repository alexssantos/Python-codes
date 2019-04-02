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
Threads = 4
N = 10.000.000
Tempo total: 90.32 s
-----------------------------
Threads = 4
N = 1.000.000
Tempo total: 9.4 s
-----------------------------
Threads = 4
N = 100.000
Tempo total: 1.15 s
-----------------------------
Threads = 4
N = 10.000
Tempo total: 0.13 s

'''

# A) SEQUENCIAL
import time
import random
import threading


def print_final_result(t_inicio):
    # Captura tempo final
    t_fim = float(time.time())
    t_total = round(t_fim - t_inicio, 2)
    # Imprime o resultado e o tempo de execução
    print(f"Tempo total: {t_total} s")


def somaThread(lista, soma_parcial, id):
    soma = 0
    for i in lista:
        soma = soma + i
    soma_parcial[id] = soma
    print(f'Thread-T{id} | START\n')
    print(f'Soma: {soma}')


def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):         # range(start, stop, step)
        fat = fat * i
    return(fat)


def array_fat_calc(lista, soma_parcial, id):
    soma_parcial[id] = []
    for n in lista:        
        soma_parcial[id].append(fatorial(n))
    print(f'FINISH --- T-{id}')
    print(lista)


t_inicio = float(time.time())
N = 100
Nthreads = 1  # Número de threads a ser criado
# Gera lista com valores aleatórios
lista = [15 for i in range(N)]

# for i in range(N):
#     lista.append(50)       # random.randint(30, 51))

# Vetor para salvar a soma parcial de cada thread
soma_parcial = Nthreads * [0]   # Lista de 'Nthreads' itens
lista_threads = []

for i in range(Nthreads):
    ini = i * int(N/Nthreads)  # início do intervalo da lista
    fim = (i + 1) * int(N/Nthreads)  # fim do intervalo da lista

    print(f' --- start Thread T-{i} ---')
    t = threading.Thread(
        target=array_fat_calc,
        args=(lista[ini:fim], soma_parcial, i))
    t.start()  # inicia thread
lista_threads.append(t)  # guarda a thread

for t in lista_threads:    
    t.join()  # Espera as threads terminarem
print_final_result(t_inicio)
print(f'N = {N}')
print(f'Nthreads = {Nthreads}')
