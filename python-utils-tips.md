# Utils Tips for VSCode + Python

## Install Flake8 to run turtle module. 

```
"PS E:\Development\Develop\Python\Python-guthub> 
      py -m pip install -U flake8 --user"
```
or 
```
> PS E:\Development\Develop\Python\Python-guthub> 
      & "folder_python_instaled" 
      -m pip install -U pylint --user""
```

obs:
folder_python_instaled like: "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python36_64/python.exe"


## Autopep8 - extension for Auto Indent code. 

```
""PS E:\Development\Develop\Python\Python-guthub> 
      & C:/Users/aarka/AppData/Local/Programs/Python/Python37-32/python.exe 
      -m pip install -U autopep8 --user
```
OR
```
py -m pip install pep8
```

## Install theme VSCode: 
      1. One Dark Pro theme 
      2. Atom One Dark Theme
to make methods of language with different colors and more clean.


# Install MODULES:

### PyGame
> py -m pip install pygame
### PSUtil
> py -m pip install psutil
### BeautilfulSoup
> py -m pip install BeautilfulSoup
### lxml - Parse para a lib BeautifulSoup
> py -m pip install lxml
### Virtualenv
> py -m pip install virtualenv

---
### Using VirtualEnv

O virtualEnv isola o ambiente para que não haja conflito entre pacotes, versões do python e etc. criando uma parta para o ambiente com sua propria versão do python, pip, .... e vc pode instalar ou desinstalar os modulos que quiser ambiente (Environment)

1. Instale virtualenv modulo
      - pip install virtualenv
2. Crie a pasta para o ambiente virtual
      - abra o terminal e va até o local onde voce quer criar a pasta.
      - comando > virtualenv NomeDaPasta        // pode ser passado um parametro "-p" para especificar a versao do python para o ambiente.
      - será criada a pasta NomeDaPasta e com subdiretorios
2. Execute o ambiente virtual
      - no terminal, va até a partas Scripts dentro da pasta do ambiente virtual
      - no terminal, execute o arquivo 'activate' com o comando > ./activate        // Usar CMD. PowerShell.exe não executa scripts. Nao vai funcionar com ele. 
4. Desativar o ambiente virtual
      - execute o arquivo deactivate com o comando > deactivate

markdown guide:
>https://about.gitlab.com/handbook/product/technical-writing/markdown-guide/