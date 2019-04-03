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
import time
import random
import multiprocessing


def print_final_result(t_inicio, soma):
    # Captura tempo final
    t_fim = float(time.time())
    t_total = round(t_fim - t_inicio, 2)
    # Imprime o resultado e o tempo de execução
    print(f"Soma: {soma}")
    print(f"Tempo total: {t_total}")
    return (soma, t_total)


def somaProc(q1, q2):
    lista = q1.get()
    soma = 0
    for i in lista:
        soma = soma + i
    q2.put(soma)


def fatorial(n):
    fat = n
    for i in range(n-1, 1, -1):
        fat = fat * i
    return(fat)


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


if __name__ == "__main__":
    count_by_processing()
