import psutil
import time


# TODO: Exercicio1
# 1.a) obter a lista de porcessos executados atualmente
# 1.b) imprimir o NOME e IPD do processo.
# 1.c) imprimir percentual de CPU e uso de MEMORIA do processo.

# AT-DR4
def print_proc(p):
    print('\n---------------------------------------------------')
    # process.exe() já exige privilégios. Impede que imprima outras coisas caso não tenha.
    print("Executável:", p.exe())   # path até o executavel.
    print("Nome:", p.name())
    print("PID: ", p.pid)
    # CPU
    print("Percentual de uso de CPU:", p.cpu_percent(interval=1.0), "%")
    # MEMORY
    perc_mem = '{:.2f}'.format(p.memory_percent())
    print("Percentual de uso de memória:", perc_mem, "%")
    mem = '{:.2f}'.format(p.memory_info().rss/1024/1024)
    print("Uso de memória:", mem, "MB")


def print_proc_info(p):

    print('\n---------------------------------------------------')
    # process.exe() já exige privilégios. Impede que imprima outras coisas caso não tenha.
    print("Executável:", p.exe())
    print("Nome:", p.name())
    print("PID: ", p.pid)
    print("Tempo de criação:", time.ctime(p.create_time()))
    print("Tempo de usuário:", p.cpu_times().user, "s")
    print("Tempo de sistema:", p.cpu_times().system, "s")
    # CPU
    print("Percentual de uso de CPU:", p.cpu_percent(interval=1.0), "%")
    # MEMORY
    perc_mem = '{:.2f}'.format(p.memory_percent())
    print("Percentual de uso de memória:", perc_mem, "%")
    mem = '{:.2f}'.format(p.memory_info().rss/1024/1024)
    print("Uso de memória:", mem, "MB")
    # THREAD
    print("Número de threads:", p.num_threads())
    print('---------------------------------------------------\n')


# Apenas cria um processo (calculadora) para testar //add >>> import subprocess
# pid = subprocess.Popen("calc").pid

pidsList = psutil.pids()

for pid in pidsList:
    # try-except: alguns processos nao podem ser acessados por falta de privilegios do usuario.
    try:
        process = psutil.Process(pid)
        print_proc_info(process)
    except Exception as e:
        print('\nUsuario sem privilégios para acessar as informações do processo.')
        print('Exception: ', e, '\n')
