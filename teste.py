import os
from glob import glob

file_name = 'test.txt'
folder_name = 'test'

user_desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
# >>> 'C:\\Users\\aarka\\Desktop'
print('LOG user_desktop', user_desktop)
os.chdir(user_desktop)
print(os.getcwdb())

folder_list = []

for x in os.walk('.'):
    #print('walk x:', x)
    if folder_name in x[1]:
        folder_list.append(os.path.join(x[0], folder_name))
    for y in glob(os.path.join(x[0], folder_name)):
        print('glob y: ', y)

print('folder list', folder_list)

# file_path = os.path.join(user_desktop, result[0][1:])
# file_path = result[0]
# file_data = os.stat(file_path)
# clean_path = result[0][1:]
# full_parh = os.path.join(user_desktop, clean_path)
# print('full_parh: ', full_parh)
