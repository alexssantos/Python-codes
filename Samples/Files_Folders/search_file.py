import os
from glob import glob

file_name = 'cpu.py'
PATH = '.'
# Walk faz um FOR pra cada DIRETORIO
    # 
# result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.txt'))]
result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], file_name))]
print(*result, sep='\n')

if len(result) != 0:    
    file_path = result[0]
    if file_path and os.path.isfile(file_path):
        print(file_path)
        det_file = os.stat(file_path)
        print(det_file)

# os.walk >> retorna Uma lista de tuplas de 3 itens.
# Tupla: 
#   item 1: str PATH
#   item 2: list [todos as pastas dessa pasta]
#   item 3: list [todos os arquivos dessa pasta]
result = [x for x in os.walk(PATH)] 
print(*result, sep='\n')