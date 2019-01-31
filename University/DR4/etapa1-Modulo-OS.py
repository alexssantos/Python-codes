import os
# DOC Modulo OS: https://docs.python.org/3.1/library/os.html
# ! Nem todas as funções estão disponíveis para Windows.

# nome do tipo do SO // posix = Linux,Mac, nt =Windows, java
osName = os.name


# == INFORMAÇÕES DO SISTEMA ==
#   - NOME DE USUARIO LOGADO.
print(os.getlogin())

#   - VARIAVEIS DE AMBIENTE DO SISTEMA
''' Uma variável de ambiente:
    é um valor nomeado DINAMICAMENTE que pode afetar o modo como os processos em execução
    irão se comportar em um computador. 
    -  https://pt.wikipedia.org/wiki/Vari%C3%A1vel_de_ambiente
'''
print(os.environ)  # Dict   CHAVE=NOME_DA_VARIAVEL

#   - DISCO E HOME PATH DO USUARIO
print(os.environ['HOMEDRIVE'])    # Disco
pathUser = os.environ['HOMEPATH']     # Pasta do Usuario
print(os.environ['HOMEPATH'])     # Pasta do Usuario

#   - PATH CAMINHO ATUAL (completo)
print(os.getcwd())

#   - PID (Process ID) do  processo em execução.
print(os.getpid())


# == ARQUIVOS E DIRETORIOS ==
''' Links anexos:
        - http://professores.dcc.ufla.br/~bruno/aulas/arquivos-e-diretorios.html
        - https://docs.python.org/3/library/os.html#os-file-dir
'''

#   - ATUAL PATH (COMPLETO)
fullPath = os.getcwd()     # STR com CONTRA-BARRA
print(fullPath)  # caminho completo

#   - CRIANDO PASTA A APRTIR DO DIRETORIO ATUAL
# os.mkdir(path, dir_fd=None)  # parametros (Li/U)nux: (path, mode=0o777, *, dir_fd=none)
# os.mkdir( "diretorio_exemplo")  # Pasta Exemplo.

#   - RENOMEAR DIRETÓRIO
# os.rename("diretorio_exemplo", "diretorio_exemplo2" )

#   - LISTAR ITENS DE UM DIRETORIO
dir_C = 'c:\\users\\'   # path independe de LowerCase ou UpperCase
listDir = os.listdir(dir_C)  # list<str>
print(listDir)
# // listDir(), listDir('.') = diretorio atual.   // '..' = diretorio 'acima'
print(os.listdir('..'))

#   - MUDAR DE DIRETORIO
# os.chdir('..')  # Go to Dir above

#   - CAMINHAR PELOS DIRETORIOS
for dirpath, dirnames, filenames in os.walk(fullPath):
    print('Current path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

