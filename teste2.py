import os
from glob import glob

PATH = '.'

def get_file(file_name):
    if not file_name or file_name == '':
        return ''



    user_desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    # >>> 'C:\\Users\\aarka\\Desktop'
    os.chdir(user_desktop)

    #teste arquivo
    result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], file_name))]    # empty list se não encotrar. 