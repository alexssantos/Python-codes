''' # AT-DR4
    4. Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso. Exemplo:
        arquivo.txt
            'Bom dia
             Você pode falar agora?'
        Resultado na tela:
            '?aroga ralaf edop êcoV
             aid moB'
    resumo: inverta a ordem das linhas e inverda o testo de cada linha.
'''
import os


file_name = input('\nDigite o nome de arquivo .txt na sua Desktop. \n>>> ')
print(file_name)

# file_name = 'astroboy.txt'   # TESTANDO

os.chdir(os.path.join(os.environ['USERPROFILE'], 'Desktop'))

if os.path.isfile(file_name):
    file_data = open(file_name, 'r')
    lines_invt = file_data.readlines()[::-1]
    file_data.close()
    # writing file
    file_existis = True
    count = 1
    while True:
        parts = file_name.split('.')
        f_name = f'{parts[0]}_{count}.{parts[1]}'
        if not os.path.exists(f_name):
            new_file = open(f_name, "w")
            lines_invt = [x[::-1] for x in lines_invt]
            new_file.writelines(lines_invt)
            new_file.close()
            break
        else:
            count += 1

