import os
import os.path
from datetime import datetime

# while True:
#     fileName11 = input('Digite o nome do Arquivo: ')
#     if os.path.exists(fileName11) and os.path.isfile(fileName11):
#         os.execl('notepad', fileName11)
#         break
#     else:
#         print('Arquivo não encontrado!')


def run(program, *args):
    # find executable
    for path in str.split(os.environ["PATH"], os.pathsep):
        file = os.path.join(path, program) + ".exe"
        try:
            return os.spawnv(os.P_WAIT, file, (file,) + args)
        except os.error:
            pass
    raise (os.error)


run("notepad", "text.txt")
