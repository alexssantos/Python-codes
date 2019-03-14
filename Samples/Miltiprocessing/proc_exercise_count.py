import multiprocessing
import time
import random
import threading


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
    
    t_fim = float(time.time())  # Captura tempo final
    # Imprime o resultado e o tempo de execução
    print("Soma:", soma)
    print("Tempo total:", t_fim - t_inicio)


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

    Nthreads = 4 # Número de threads a ser criado

    # Vetor para salvar a soma parcial de cada thread
    soma_parcial = Nthreads * [0]
    lista_threads = []

    for i in range(Nthreads):
        ini = i * int(N/Nthreads) # início do intervalo da lista
        fim = (i + 1) * int(N/Nthreads) # fim do intervalo da lista
        
        t = threading.Thread(target=somaThread, args=(lista[ini:fim],soma_parcial, i))
        t.start() # inicia thread
        
        lista_threads.append(t) # guarda a thread

    for t in lista_threads:
        t.join() # Espera as threads terminarem
        soma = 0
        for i in soma_parcial:
            soma = soma + i

    # Captura tempo final
    t_fim = float(time.time())

    # Imprime o resultado e o tempo de execução
    print("Soma:", soma)
    print(f"Tempo total: {round(t_fim - t_inicio, 2)}s")


count_by_threadings()