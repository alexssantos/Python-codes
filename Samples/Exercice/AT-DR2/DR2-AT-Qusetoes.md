
1. Usando o Thonny, escreva um programa em Python que leia uma tupla contendo 3 números inteiros, (n1, n2, n3) e os imprima em ordem crescente.

2. Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive. O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.

3. Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois números inteiros, A e B, e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o resultado da operação. Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.

4. Escreva um programa em Python que leia um vetor de 5 números inteiros e o apresente na ordem inversa. Imprima o vetor no final. Use listas.
Exemplo: se a entrada for [4, 3, 5, 1, 2], o resultado deve ser [2, 1, 5, 3, 4].
**não precisa pegar do usuario

5. Usando a biblioteca ‘turtle’ crie uma função que desenhe a imagem a seguir:


6. Escreva uma função em Python que leia uma tupla contendo números inteiros, retorne uma lista contendo somente os números ímpares e uma nova tupla contendo somente os elementos nas posições pares.
**não precisa pegar do usuario 
**precisa criar a unfão e chamar a função

-------- PyGame ---------------

7. Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta), toda vez que a tecla espaço for pressionada ou o botão direito for clicado.

8. Usando a biblioteca ‘pygame’, escreva um programa que desenha um botão (círculo) com o texto “clique” sobre ele na parte superior da tela. Quando o botão for clicado, ele deve chamar uma função que desenha um retângulo em uma posição aleatória na tela. Caso um retângulo apareça na "mesma posição" (sobreposto e fazer um tratamento) que um já existente, ambos devem ser eliminados.

9. Usando o código anterior, escreva um novo programa que, quando as teclas ‘w’, ‘a’, ‘s’ e ‘d’ forem pressionadas, ele movimente o círculo com o texto “clique” nas direções corretas. Caso colida com algum retângulo, o retângulo que participou da colisão deve desaparecer.

----------- WebScraping ---------

10. Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv
E:
    1. Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega, verifique: No século XXI (a partir de 2001), qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades:
        1. Curling
        2. Patinação no gelo (skating)
        3. Esqui (skiing)
        4. Hóquei sobre o gelo (ice hockey)
    2. Para cada esporte, considere todas as modalidades, tanto no masculino quanto no feminino. Sua resposta deve imprimir um relatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida.

**não usar pandas na captura do csv. 
**Tratamento pode ser feito com Pandas


11. Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv
Obtenha, dentre os jogos do gênero de ação (Action), tiro (Shooter) e plataforma (Platform):
    1. Quais são as três marcas que mais publicaram jogos dos três gêneros combinados? Indique também o total de jogos de cada marca.
    2. Quais são as três marcas que mais venderam os três gêneros combinados? Indique também o total de vendas de cada marca.
    3. Qual é a marca com mais publicações em cada um dos gêneros nos últimos dez anos no Japão? Indique também o número total de jogos dela.
    4. Qual foi a marca que mais vendeu em cada um desses gêneros nos últimos dez anos, no Japão? Indique também o total de vendas dela.

12. Obtenha, usando requests ou urllib, a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html dentro de seu programa em Python e faça:
    1. Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
    2. Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela. O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região.

(em grupo)
13. Obtenha, usando requests ou urllib, o conteúdo sobre as PyLadies no link http://brasil.pyladies.com/about e:
    1. Conte todas as palavras (do idioma) no corpo da página, e indique quais palavras apareceram apenas uma vez.
    2. Conte quantas vezes apareceu a palavra ladies no conteúdo da página
    Caso não consiga acessar o site, baixe o arquivo pagina_exemplo.zip, descompacte-o em algum diretório e use a URL local em seu computador para acessá-la:
        caminho/pagina_exemplo/estadosCentroOeste.html.
    Substitua caminho pelo caminho real do arquivo em seu computador.
    **se não conseguir pegar todas as palavras de acordo com o idioma, pegas as palavras unicas e comentar. 