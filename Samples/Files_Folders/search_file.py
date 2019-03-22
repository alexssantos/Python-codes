import os
from glob import glob


PATH = '.'
# Walk faz um FOR pra cada DIRETORIO
    # 
# result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.txt'))]
result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], 'list_dir.py'))]
print(*result, sep='\n')


# os.walk >> retorna Uma lista de tuplas de 3 itens.
# Tupla: 
#   item 1: str PATH
#   item 2: list [todos as pastas dessa pasta]
#   item 3: list [todos os arquivos dessa pasta]
result = [x for x in os.walk(PATH)] 
print(*result, sep='\n')