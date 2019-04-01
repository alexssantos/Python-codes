import time
import random
import multiprocessing
import threading


def print_final_result(t_inicio, soma):
    # Captura tempo final
    t_fim = float(time.time())
    t_total = round(t_fim - t_inicio, 2)
    # Imprime o resultado e o tempo de execução
    print(f"Soma: {soma}")
    print(f"Tempo total: {t_total}")
    return (soma, t_total)


# Sequencial
def count_sequential():
    N = int(input("Count in Sequential - \nEntre com o tamanho do vetor: "))

    # Captura tempo inicial
    t_inicio = float(time.time())

    # Gera lista com valores aleatórios
    lista = []

    # Add valores entre -50 e 50
    for i in range(N):
        lista.append(random.randint(-50, 51))

    # Faz o cálculo da soma dos valores do vetor/lista
    soma = 0
    for i in lista:
        soma = soma + i

    print_final_result(t_inicio, soma)


def somaThread(lista, soma_parcial, id):
    soma = 0
    for i in lista:
        soma = soma + i
    soma_parcial[id] = soma


def count_by_threadings():    
    N = int(input("Count By Threads - \nEntre com o tamanho do vetor: "))

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
        soma = 0
        for i in soma_parcial:
            soma = soma + i

    print_final_result(t_inicio, soma)


def somaProc(q1, q2):
    lista = q1.get()
    soma = 0
    for i in lista:
        soma = soma + i
    q2.put(soma)


def count_by_processing():
    N = int(input("Multi-Prossessing - Entre com o tamanho do vetor: "))

    # Captura tempo inicial
    t_inicio = float(time.time())

    # Gera lista com valores aleatórios
    lista = []
    for i in range(N):
        lista.append(random.randint(-50, 51))
    NProc = 4  # Número de processos a ser criado
    # Fila de entrada dos processos
    q_entrada = multiprocessing.Queue()
    # Fila de saída dos processos
    q_saida = multiprocessing.Queue()
    lista_proc = []
    for i in range(NProc):
        ini = i * int(N/NProc)  # início do intervalo da lista
        fim = (i + 1) * int(N/NProc)  # fim do intervalo da lista
        q_entrada.put(lista[ini:fim])
        p = multiprocessing.Process(
            target=somaProc, 
            args=(q_entrada, q_saida))        
        p.start()  # inicia processo
        lista_proc.append(p)  # guarda o processo

    for p in lista_proc:
        p.join()  # Espera os processos terminarem

    soma = 0
    for i in range(0, NProc):
        soma = soma + q_saida.get()

    print_final_result(t_inicio, soma)


count_sequential()
count_by_threadings()

if __name__ == "__main__":
    count_by_processing()
