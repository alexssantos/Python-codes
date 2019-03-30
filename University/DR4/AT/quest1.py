'''# AT-DR4
    1. Escreva um programa em Python que:
        1.a) obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu programa manipula suas informações;
        2.b) imprima o nome do processo e seu PID;
        3.c) imprima também o percentual de uso de CPU e de uso de memória.
'''

import psutil


def print_proc(p):
    if psutil.pid_exists(p.pid):
        try:
            print('\n---------------------------------------------------')
            # process.exe() já exige privilégios. Impede que imprima outras coisas caso não tenha.
            print("Executável:", p.exe())   # path até o executavel.
            print("Nome:", p.name())
            print("PID: ", p.pid)
            # CPU
            print("Percentual de uso de CPU:", p.cpu_percent(), "%")
            # MEMORY
            perc_mem = '{:.2f}'.format(p.memory_percent())
            print("Percentual de uso de memória:", perc_mem, "%")
            mem = '{:.2f}'.format(p.memory_info().rss/1024/1024)
            print("Uso de memória:", mem, "MB")
        except (psutil.ZombieProcess, psutil.NoSuchProcess) as e:
            print(f'''
            ===================================
            {p} Não está mais Ativo. ;(
            Exception: {e}
            ===================================
                ''')
            return 1
        except psutil.AccessDenied as e:
            print(f'\nUsuario sem privilégios para acessar as informações do processo: {p.name()}')
            print('Exception: ', e, '\n')

        return 0


# Apenas cria um processo (calculadora) para testar //add >>> import subprocess
# pid = subprocess.Popen("calc").pid
pidsList = psutil.pids()
nao_existe = 0
print(f'Quantidade de Processos: {len(pidsList)}')
for pid in pidsList:
    # try-except: alguns processos nao podem ser acessados por falta de privilegios do usuario.
    process = psutil.Process(pid)
    nao_existe += print_proc(process)

print(f'''\
==============================================     
{len(pidsList)} - Quantidade de Processos
{nao_existe} - Processos Antigos
==============================================     
''')
