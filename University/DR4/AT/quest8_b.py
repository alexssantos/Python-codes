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

====================================
N 100.000
====================================
Tempo total: 6.43 s
Nthreads = 1
------------------------
Tempo total: 6.47 s
Nthreads = 2
----------------------
Tempo total: 6.58 s
Nthreads = 4
----------------------
Tempo total: 6.56 s
Nthreads = 8

====================================
N 10.000.000
====================================
Tempo total: 35.06 s
Nthreads = 1
------------------------
Tempo total: 
Nthreads = 2
----------------------
Tempo total: 
Nthreads = 4
----------------------
Tempo total: 
Nthreads = 8

====================================

'''

# B) THREADS
import time
import random
import threading


def print_final_result(t_inicio):
    # Captura tempo final
    t_fim = float(time.time())
    t_total = round(t_fim - t_inicio, 2)
    # Imprime o resultado e o tempo de execução
    print(f"Tempo: {t_total} s")


def gap_time(t_inicio):
    # Captura tempo final
    t_fim = float(time.time())
    t_total = round(t_fim - t_inicio, 2)
    return t_total


def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):         # range(start, stop, step)
        fat = fat * i
    return(fat)


def array_fat_calc(lista, soma_parcial, id, t_inicio):
    soma_parcial[id] = []
    for n in lista:        
        soma_parcial[id].append(fatorial(n))
    print(f'Thread-{id+6} - FINISH - in {gap_time(t_inicio)}')    
    

N = 1000000
Nthreads = 4
lista = [random.randint(30, 50) for i in range(N)]

# Vetor para salvar a soma parcial de cada thread
t_inicio = float(time.time())
print(f'\nINICIO: {t_inicio}')
soma_parcial = Nthreads * [0]   # Lista de 'Nthreads' itens
lista_threads = []

for i in range(Nthreads):
    ini = i * int(N/Nthreads)  # início do intervalo da lista
    fim = (i + 1) * int(N/Nthreads)  # fim do intervalo da lista
    print(f'Thread-{i+6} - soma_parcial:[{ini}:{fim}]')
    print(f'Thread-{i+6} - STARED in {gap_time(t_inicio)} s\n')

    t = threading.Thread(
        target=array_fat_calc,
        args=(lista[ini:fim], soma_parcial, i, t_inicio))
    
    t.start()  # inicia thread    
    lista_threads.append(t)  # guarda a thread
   

ix = 0
for t in lista_threads:    
    print(f'{t.name} - Dormiu !!!')
    if ix == 0:
        print(f'''
+=========================================================        
|PRIMEIRA THREAD DORMIU in {gap_time(t_inicio)} s.
+=========================================================''')        
    
    if ix == len(lista_threads) -1:
        print(f'''
+==================================================
|ULTIMA THREAD DORMIU in {gap_time(t_inicio)} s.
+==================================================''')
    t.join()  # Espera as threads terminarem
    ix += 1


print(f'''
+===========================
| N = {N}
| Nthreads = {Nthreads}
| Tempo: {gap_time(t_inicio)} s.
+===========================
''')
