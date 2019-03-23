import os

desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
print('Desktop: ', desktop_path)
print('Pasta atual: ', os.getcwd())

file_name = input('Digite o nome do arquivo.txt:\n>> ')

if os.path.exists(file_name):
    print(file_name, '- Existe!')
    program = "notepad"
    try:
        # os.system(f"{program}.exe {file_name}")   // PROCESSO ESPERA O PROGRAMA FECHAR PRA CONTINUAR
        os.startfile(file_name)
    except Exception as e:
        print('ERRO: ', e, '\n -----------------')
else:
    print(file_name, '- Não existe!')
