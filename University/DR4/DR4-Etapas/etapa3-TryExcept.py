import os


''' Validações: 
    - melhor forma: montar um modulo para tratar somente essas exceções do seu programa. 
    -
LINKS: 
    - https://pythonhelp.wordpress.com/2012/09/14/tratamento-de-excecoes/
'''

''' Dicas sobre EXCEÇÕES:
    1.  Não faça exceções demais! É melhor criar validações consistentes para evitar erros. ex.: Mascaras de formulários.
    2.  Não tratar quando você não sabe oq fazer. Não adianta encher o codigo de TryExcept se tudo q seu tratamento faz é imprimir a msg na tela.
    3.  Conhecer as exceções da biblioteca padrão.  
        - https://docs.python.org/3/library/exceptions.html
'''

# while True:
#     try:
#         x = int(input("Entre com um número: "))
#         break
#     except ValueError:  # ERRO EXPECIFICO
#         print("Valor inválido. Tente novamente.")
#     except Exception:   # ERRO GERAL
#         print("Houve um problema com o numero obtido. Try Again!")
# print("\n ==>  "
#         "1% de", x, "é:", x/100, end='\n\n')


homeFolder = os.environ['HOMEPATH']
def TryCreateFolder(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print("Arquivo já existente:", path)
    except FileNotFoundError:
        print("O sistema não pode encontrar o caminho especificado:", path)
    except:
        print("Erro")


#ERRO exato
def TryCreateFolder2(path):
    try:
        os.mkdir(path)        
    except Exception as e:
        print(str(e))
        # >>> [WinError 183] Cannot create a file when that file already exists: '\\Users\\alex.silva'


TryCreateFolder(homeFolder)