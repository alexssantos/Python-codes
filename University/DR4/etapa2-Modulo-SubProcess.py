import subprocess


''' OBS da aula:
    - Usuarios em um sistema operacional: Sempre vem com um usuario Admim e outros usuarios podem ser criados e podem ter 'privilégios até de Admin'.
    - ataque DoS: as portas com serviços ouvindo as portas tem um limite de monitoramento. Se é ultrapassado esse limite de processamento da maquina, 
        algumas portas ou acessos são liberados por "enlouquecimento" do sistema. 
        (DDoS - Distribuido)
        - https://twitter.com/garrows/status/1065217184643768320
    - Python Précompila o codigo/bibliotecas/arquivos etranspormando em microcodigo (pycache). Inclusive há Engines em outras linguas para usar esse microcodigos em outras plataformas, como o 
        IronPython para C#. 
    -       // '''

# print (subprocess.run('calc'))
print( subprocess.py)
# return > CompletedProcess(args='calc', returncode=0)
''' Como ele o modulo subprocess chama um executavel ? 
    - Quando usamos o CMD e digitamos "Path" (é uma EV - environment variable - padrão com uma lista de caminhos de aplicações no sistema operacional) ele mostra
    os caminhos e o modulo dele ser e procurar nessa EV o parametro passado, ex.: subprocess.run('calc').

    obs: Muitas aplicações adicionam o caminho da aplicação no 'Path'    //'''

print( subprocess.run(["notepad", "art_texto.txt"]))    # [ 'programa', 'argumento']   //O argumento do programa 'notepad' é sempre o arquivo a ser aberto no dir atual.


print ()

# TP1-QST: Diferenças entre spawn e exec:  
#   1. De forma geral, um tem mais dominio e outro não. spawn pode tem argumentos de gerenciamento a mais como timeout de processos. 

