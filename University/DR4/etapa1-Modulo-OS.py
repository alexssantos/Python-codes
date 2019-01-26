import os 
# DOC Modulo OS: https://docs.python.org/3.1/library/os.html
#! Nem todas as funções estão disponíveis para Windows.

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
print( os.environ) #Dict   CHAVE=NOME_DA_VARIAVEL

#   - DISCO E HOME PATH DO USUARIO
print( os.environ['HOMEDRIVE'] )    # Disco
pathUser = os.environ['HOMEPATH']     # Pasta do Usuario
print( os.environ['HOMEPATH'] )     # Pasta do Usuario

#   - PATH CAMINHO ATUAL (completo)
print( os.getcwd() )    

#   - PID (Process ID) do  processo em execução.
print( os.getpid() )


# == INFORMAÇÕES DE ARQUIVOS E DIRETORIOS ==
''' Links anexos:
        - http://professores.dcc.ufla.br/~bruno/aulas/arquivos-e-diretorios.html
        - https://docs.python.org/3/library/os.html#os-file-dir
'''

#   - ATUAL PATH (COMPLETO)
fullPath =  os.getcwd()     # STR com CONTRA-BARRA
print(fullPath) # caminho completo

#   - CRIANDO PASTA A APRTIR DO DIRETORIO ATUAL
#os.mkdir(path, dir_fd=None)  # parametros (Li/U)nux: (path, mode=0o777, *, dir_fd=none)
#os.mkdir( "diretorio_exemplo")  # Pasta Exemplo.

#   - RENOMEAR DIRETÓRIO
#os.rename("diretorio_exemplo", "diretorio_exemplo2" )

#   - LISTAR ITENS DE UM DIRETORIO
dir_C = 'c:\\users\\'   # path independe de LowerCase ou UpperCase
listDir = os.listdir(dir_C) # list<str>
print(listDir)
print(os.listdir('..'))    # // listDir(), listDir('.') = diretorio atual.   // '..' = diretorio 'acima'

#   - MUDAR DE DIRETORIO
#os.chdir('..')  # Go to Dir above


# == MODULO OS.PATH ==
''' Def.: 
    Com esse módulo é possivel manipular o nome e caminho (ABSOLUTO ou TELATIVO) de um arquivo ou diretorio'''

#   - EXISTENCIA
p = 'diretorio_exemplo'
if os.path.exists(p):
    print(p, '- Existe!')
else:
    print(p, '- Não existe!')

#   - TIPO ARQUIVO OU PASTA
arquivo = 'arq_texto.txt'
if os.path.isfile(arquivo):
    print(arquivo, 'é um arquivo!')
else:
    print(arquivo, 'não é um arquivo!')


p = 'diretorio_exemplo2'
if os.path.isfile(p):
    print(p, 'é um diretorio!')
else:
    print(p, 'não é um diretório!')

# CAMINHO ABSOLUTO - ARQUVO OU PASTA
print(os.path.abspath('arq_texto.txt')) # caminho absoluto

# NOME - PASTA OU ARQUIVO
print(os.path.basename(fullPath))

# SEPARAR PATH EM PARTES
pastasList = os.path.split(fullPath)
print(pastasList)


# LSITA DE PASTAS DO ABS PATH
fileName = os.path.abspath('arq_texto.txt')
t = os.path.split(fileName) # separa em duas partes
p0 = t[0] # parte 0
p1 = t[1] # parte 1

lista_dir = []
while p1: # fazer enquanto houver parte 1
    lista_dir.append(p1) # adiciona à lista a parte 1
    t = os.path.split(p0) # agora, separa p0
    p0 = t[0]   # NOVO full path, menos o ultimo diretorio.
    p1 = t[1]   # NOVO ultimo diretorio
lista_dir.append(p0) # Colocar último
lista_dir.reverse() # Para reverter a lista, pois ela estava ao contrário
print(lista_dir) # imprime a lista

# FULL PATH - JUNTANDO PASTAS
print(os.path.join("C:", "Users", "Teste", "arq_texto.txt"))
print(os.path.join(os.getcwd(), 'arq_texto.txt'))