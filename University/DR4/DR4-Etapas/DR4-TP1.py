import os, os.path, time, subprocess, psutil
from datetime import datetime





''' Questões (e obs):

20 Questoes

3) em Windows, só o PID. (tem uma rubrica que no linux requer 2 instruções)
4) 1. Qual é o método // 2. uma chamada do metodo com os parametros necessarios
5) 1. Verificar a exitencia // 2. checar se realmente é arquivo
6) pegar extensão do arquivo
7) Pegaar caminho absoluto
8) pegar os KB (PRECISA DE CONVERSAO pq é entregue em bytes).
9) duvida do Roger
10) Igor falou na aula
11) 

14) Copiar e colar do roteiro que tem uma explicação direta logo no começo. 
15) Cuidado se for pedir do usuario. 
    Duas opções: 
    1. Listar os IPD's e o usuario escolhe.
    2. Usuario dar o nome ou PID e VALIDAR pra mostrar as info.
16) Especifico. Existe pegar a CPU Total e CPU por Nucleo. 

18) tem no trimestre passado
19) tem no trimestre passado (instalação do sistema)
20) (Partiçaõ atual)

'''

#1  imprima o nome de Usuario => Variaveis de Ambiente
print( os.environ['USERNAME'])

#2 Variaveis de Ambiente
    #2-A) O que são ? 


    #2-B) Como elas podem ser obtidas pelo modulo "os" em Python?
    # utilizando o comando 'os.environ' é retornado todos as Variaveis de Ambiente do sistema em relação ao usuario corrente.
# print( os.environ)

    #2-C) Como pode ser obtido o caminho completo do diretório de usuário em Python, através das variáveis de ambiente?
    # Através da variavel de ambiente 'USERPROFILE'
print(os.environ['USERPROFILE'])

#3 PID do proprio processo
print(os.getpid())
# os.getpgrp() => PID de grupo (linux)

#4 caminho ABSOLUTO de um DIRETORIO que tem caminho RELATIVO
    # NAO È ESSE: print( os.getcwd())
path4 = 'folder_name'
print(os.path.expanduser(path4))

# 5) 
fileName5 = input('Digite o nome do Arquivo para verificar se existe: ')
if os.path.exists(fileName5):
    print(fileName5, '- Existe!')
    if os.path.isfile(fileName5):
        print('É um arquivo!')
    else:
        print('Não é um arquivo!')
else:
    print(fileName5, '- Não existe!')

# 6) indique a extensao do arquivo
fileName6 = 'document.txt'
ext = fileName6.split(os.extsep)[1:]

# 7) peagr caminho absoluto de um arquivo.
    #pegar o nome do arquivo
    #ver se existe na pasta
    #imprimir caminho

fileName7 = input('Digite o nome do Arquivo da Pasta atual. ex.: "texto.txt": ')
if os.path.exists(fileName7):
    try:
        print(fileName7, '- Existe!')
        absPath = os.path.abspath(fileName7)
        print(os.path.split(absPath)[0])
    except Exception as e:
        print('ERRO: ', e)        
else:
    print(fileName7, '- Não existe!')

# 8) 
    # pegar os nomes
    # criar Dict {nome: tamanho (em KB)}
listFiles = [x for x in os.listdir() if os.path.isfile(x)]    # // Dir Atual = (),('.')  // Dir Acima = ('..')
for fileItem in listFiles:
    fileSize = os.stat(fileItem).st_size / 1024 
    print(fileItem, ' - size : ', fileSize,' Kb')

# 9) 
# import time
# from datetime import datetime

listFiles = [x for x in os.listdir() if os.path.isfile(x)]
for fileItem in listFiles:
    # tempo de modificação em nanosegundos
    ts1 = os.stat(fileItem).st_mtime
    data1 = datetime.utcfromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S')
    # tempo de criaçao em nanosegundos
    ts2 = os.stat(fileItem).st_ctime
    data2 = datetime.utcfromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
    print(fileItem, ' modification:', data1, ', creation:', data2)

# 10) 

# 11) pegar nome do arquivo e abrir com 'notepad' usando 'os'

#   - pegar nome do arquivo. 
#   - verificar se existe
# while True:
#     fileName11 = input('Digite o nome do Arquivo: ')
#     if os._exists(fileName11) and os.isfile(fileName11):
#         os.exec('notepad', fileName11)
#         break
#     else:
#         print('Arquivo não encontrado!')

def run(program, *args):
    # find executable
    for path in str.split(os.environ["PATH"], os.pathsep):
        file = os.path.join(path, program) + ".exe"
        try:
            return os.spawnv(os.P_WAIT, file, (file,) + args) # needs to be atuple to allow concat
        except os.error:
            pass
    raise (os.error)


run("notepad", "text.txt")

# 12) criar pocesso com 'os' e 'subprocess'

#   12.1) os.spawnv()       **exatamente como o exerc anterior
program = "notepad"
path = 'C:\\WINDOWS\\system32'
file = os.path.join(path, program) + ".exe"
os.spawnv(os.P_WAIT, file, file + 'file.txt')  

#   12.2) subprocess
subprocess.run("notepad")        # import subprocess

# 13)
p = subprocess.Popen("calc")
print("PID do processo criado:", p.pid)

# 14) --------------------- psutil.pids != psutil.process_iter

# 15) dado um PID - nome de user, tempo de criação, e memoria em Kb (usando psutil.Process)
# import datetime, time

while True:        
    pid = int(input('Digite o n° PID:'))
    try:
        p = psutil.Process(pid)
        print(p.username())
        print(time.ctime(p.create_time()))
        print((p.memory_info().rss / 1024), ' Kb')
        print((p.memory_info().rss / (1024*1024)), ' Mb')
        break
    except Exception:
        print('PID não existe!')




# 16) tempo da CPU tempo(seg)/nucle
while True:
    count = 1
    if count > 15:
        break
    print(p.cpu_times().user, " lap:", count)
    time.sleep(1)
    count += 1


# 17) 
# from datetime import datetime
# import psutil
count = 1
while True:
    p = psutil.cpu_percent(interval=1)
    now = datetime.now()
    _time = f'{now.hour}:{now.minute}:{now.second}'
    print(f'CPU: {p}% -- lap {count} -- time: {_time}')
    count += 1
    if count > 20:
        break

# 18) meomria e memoria swap em Gb
#import psutil
memUsedGb = psutil.virtual_memory().used / 1000**3
swapUsedGb = psutil.swap_memory().used / 1000**3
print(f'Memória em uso: {"{:2.2f}".format(memUsedGb)} Gb')
print(f'Memória Swap em uso: {"{:2.2f}".format(swapUsedGb)} Gb')

# 19) 
#import psutil

#get Sistem Partiction path
sysDrivePath = psutil.Process().environ()['SYSTEMDRIVE']
#print disk_usage in Gb
driveUseGb = ("{:2.2f}").format(psutil.disk_usage(sysDrivePath).used / 1000**3)
print(f'Disco do Sistema - Usado: {driveUseGb} Gb')

# 20)
#improt psutil

disks = psutil.disk_partitions()
if disks:
    for disk in disks:
        diskUsage = psutil.disk_usage(disk.device)
        armazDisp = ("{:2.2f}").format(diskUsage.free / 1000**3)
        armazTotal = ("{:2.2f}").format(diskUsage.total / 1000**3)
        print(f'Nome: {disk.device}')
        print(f'Tipo de Sistema de Arquivo: {disk.fstype}')
        print(f'total de Armazenamento: {armazTotal} Gb')
        print(f'Armazenamento disponivel: {armazDisp} Gb')        








