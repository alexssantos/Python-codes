
'''Exercício 1: 
    Escrever uma função em Python que verifica se um arquivo está ou não no diretório. A função deve receber o DIRETÓRIO e o NOME_DO_ARQUIVO
    a ser buscado e deve retornar True ou False. Escrever também um programa que obtenha do usuário o nome do arquivo a 
    ser procurado e o diretório de busca e chame a função para realizar a busca e indicar se encontrou ou não o arquivo em questão.
    
    Ajuda:
        Usar os.listdir() para listar todos os arquivos no diretório e os.path.isfile() para saber se é um arquivo.
        Para cada arquivo, verificar se é igual ao nome do arquivo.
'''
'''Exercício 2 (Nível Avançado): 
    Escreva uma função semelhante a do Exercício 1 para buscar um arquivo recursivamente a partir de um diretório. Faça, agora, a 
    função retornar uma lista de diretórios que contém o arquivo. Se a lista estiver vazia, indica que não encontrou. Escreva também 
    um programa que obtenha do usuário o nome do arquivo e do diretório e chame a função para buscar o arquivo no diretório em questão. 
    Quando terminar, indique em que diretórios o arquivo foi encontrado.
    
    Ajuda:
        Use duas listas, uma para guardar os diretórios que devem ser ainda buscados e outra de resposta, para guardar os diretórios em que achou o arquivo.
        A primeira lista deve guardar inicialmente o diretório de partida (entrada do usuário).
        Enquanto esta lista tiver algum elemento, obtenha seu primeiro elemento e gera uma lista de arquivos e diretórios dela através de os.listdir().
        Para cada elemento desta lista, verifique se é um arquivo ou um diretório.
        Se for arquivo, verifique se é o arquivo a ser buscado e insira na lista de respostas caso sejam iguais.
        Se for um diretório, insira-o (concatenado com o diretório anterior) na primeira lista.
'''
'''Exercício 3: 
    Escreva uma função em Python que indique todos processos que estão usando a memória residente (RSS) acima de um percentual acima 
    da média aritmética de uso memória de todos os processos correntes. A função deve receber dois parâmetros: a lista de todos os 
    processos e um percentual que indica o quanto acima da média deve estar o nível de memória. A função deve retornar uma lista de 
    dicionários contendo o PID, nome, memória residente (RSS) e memória virtual (VMS) do processo. Escreva também um programa que 
    chame esta função e imprima o seu resultado.
    
    Exemplo: 
        se a média é 1000 KB e o percentual é 70%, então os processos que têm a memória residente acima de 1000 + 70%*1000 = 1700 KB, devem ser retornados na lista de resposta.
    
    Ajuda:
        Calcule primeiro a média em uma repetição e, depois, em outra, cheque os processos que estão sobre a média. Lembre-se: só é possível usar o valor da média depois que ela é calculada sobre todos os valores.
        Use a função psutil.process_iter() para obter o objeto do processo Process, pois ela é melhor para se trabalhar com repetições (ao invés de psutil.pids()).
        Para percorrer os processos na lista retornada por psutil.process_iter(), use a função as_dict (para converter para dicionário) de um processo como no exemplo abaixo:
    
    {
        for p in lista_processos:
            try:
                pinfo = p.as_dict(attrs=['pid', 'name', 'memory_info'])
            except psutil.NoSuchProcess:
                pass
    } 

        Note que também foi usada a diretiva try-except para verificar se o processo ainda existe, já que ele pode já ter terminado no meio do processamento. A exceção de nome psutil.NoSuchProcess é usada neste caso.
        Gere um outro dicionário para desmembrar memory_info e para ser incluído na lista resposta da função.
'''

import os, os.path


# 1) 

while True:
    fileName = input('Nome do arquivo:')
    folderName = input('Nome da pasta:')
    run(fileName, folderName)   


def run(file, folder):
    # folder exists and get Files
    if os.path.isdir(folder):
        listFiles = os.listdir(folder)
    else: 
        return print('Folder not exists')
    
    # find file
    for fileItem in listFiles:
        file = os.path.join(path, program) + ".exe"
        try:
            return os.spawnv(os.P_WAIT, file, (file,) + args) # needs to be atuple to allow concat
        except os.error:
            pass
    raise (os.error)




