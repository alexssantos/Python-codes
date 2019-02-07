import os, os.path
import subprocess
import psutil





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

#4 caminho RELATIVO de um DIRETORIO que tem caminho RELATIVO
    # NAO È ESSE: print( os.getcwd())
