arq = open("sinopse.txt", "r")      # modo reader
for linha in arq:                   # complexidade: O(1)
    print(linha, end="")                # 'end' não pular linha.
arq.close()                         # se tiver como Writer é obrigatorio fechar. Modo leitura nao tem problema.



''' Complexidade 
    **constantes multiplicativas são desconsideradas em questão de complexidade de algoritmos

    cenario 1: leitura de 1.000 linhas = O(1000) = 100.O(1) = O(1)
    cenario 2: leitura de 1.000.000 linhas = O(1000000) = 10000000.O(1) = O(1)
'''

# WRITE x APPEND: WRITE reescreve (novo) o arquivo, o APPEND atualiza o arquivo.
# LOG - melhor forma é usar Append
#   Cuidado para não sujar muito o LOG. Escrita de testes com erros/exception