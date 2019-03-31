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
'''

import threading
import random


def somaThread(lista, soma_parcial, id):
    soma = 0
    for i in lista:
        soma = soma + i
    soma_parcial[id] = soma


N = 10000

# Captura tempo inicial
t_inicio = float(time.time())

# Gera lista com valores aleatórios
lista = []

for i in range(N):
    lista.append(random.randint(-50, 51))

Nthreads = 4  # Número de threads a ser criado

# Vetor para salvar a soma parcial de cada thread
soma_parcial = Nthreads * [0]
lista_threads = []

for i in range(Nthreads):
    ini = i * int(N/Nthreads)  # início do intervalo da lista
    fim = (i + 1) * int(N/Nthreads)  # fim do intervalo da lista

t = threading.Thread(
    target=somaThread,
    args=(lista[ini:fim], soma_parcial, i))
t.start()  # inicia thread

lista_threads.append(t)  # guarda a thread

for t in lista_threads:
t.join()  # Espera as threads terminarem


print_final_result(t_inicio, soma)
