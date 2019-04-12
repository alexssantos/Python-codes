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
====================================
N 10.000.000
====================================
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
Nproc = 1
------------------------
Tempo total: 6.47 s
Nproc = 2
----------------------
Tempo total: 6.58 s
Nproc = 4
----------------------
Tempo total: 6.56 s
Nproc = 8

====================================
N 10.000.000
====================================
Tempo total: 35.06 s
Nproc = 1
------------------------
Tempo total:
Nproc = 2
----------------------
Tempo total:
Nproc = 4
----------------------
Tempo total:
Nproc = 8

====================================

'''

# C) PROCESSOS
import time
import random
import multiprocessing


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
    return fat


def array_fat_calc(q1, q2):
    lista = q1.get()
    soma_parcial = []
    for n in lista:
        fat = fatorial(n)
        soma_parcial.append(fat)
    q2.put(soma_parcial)


if __name__ == "__main__":
    N = 1000
    Nproc = 4
    lista = [random.randint(30, 50) for i in range(N)]

    # Vetor para salvar a soma parcial de cada thread
    t_inicio = float(time.time())
    q_in = multiprocessing.Queue()
    q_out = multiprocessing.Queue()

    lista_proc = []
    for i in range(Nproc):
        ini = i * int(N/Nproc)  # início do intervalo da lista
        fim = (i + 1) * int(N/Nproc)  # fim do intervalo da lista
        q_in.put(lista[ini:fim])
        p = multiprocessing.Process(
            target=array_fat_calc,
            args=(q_in, q_out))
        p.start()
        lista_proc.append(p)

    for p in lista_proc:
        p.join()  # Espera as threads terminarem

    soma_parcial = []
    for i in range(0, Nproc):
        soma_parcial.extend(q_out.get())

    print(f'''
    +===========================
    | N = {N}
    | Nproc = {Nproc}
    | Tempo: {gap_time(t_inicio)} s.
    +===========================
    ''')
