import os
from glob import glob

folder_name = 'test'

PATH = '.'
# >>> 'C:\\Users\\aarka\\Desktop'
user_desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
os.chdir(user_desktop)
# empty list se não encotrar.
result = [y for x in os.walk(PATH)
          for y in glob(os.path.join(x[0], folder_name))]

folder_paths = [os.path.join(user_desktop, x[2:]) for x in result]
dir_itens_list = [os.listdir(x) for x in folder_paths]
# delete dirs
i_dir = 0
for dir_itens in dir_itens_list:
    os.chdir(folder_paths[i_dir])    
    dir_itens_list[i_dir] = [item for item in dir_itens if not os.path.isdir(item)]
    i_dir += 1


'''
dict = {
    'path':[files, file2, ...],
    'path2':[files, file2, ...]
}'''
retorno = dict((k, dir_itens_list[folder_paths.index(k)]) for k in folder_paths)
input()
