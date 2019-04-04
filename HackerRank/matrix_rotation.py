'''
Desc:
    You are given a 2D matrix, a, of dimension MxN and a positive integer R. You have to rotate the matrix R
    times and print the resultant matrix. Rotation should be in anti-clockwise direction.
    Rotation of a 4x5 matrix is represented by the following figure. Note that in one rotation, you have to shift
    elements by one step only (refer sample tests for more clarity).
obs: 
    1. sub-rotações tbm na mesma direção.
    2. rotação é posicionar o elemento N em N+1

M=i -> linhas
N=j -: colunas
R= n° vezes pra rodar(positivo inteiro)


==============================
- CONSTANTES:
===============================
2 <= M, N <= 300                                    //Menor valor de M ou N é 2.
1 <= R <= 10^9                                      //R é pelo menos 1 pra cima.
min(M, N) % 2 == 0                                  //Menor entre M e N sempre é PAR
1 <= a(i,j) <= 10^8 , where i ∈ [1..M] & j ∈ [1..N]


- EXEMPLO, R=2:
========================================
Start         First           Second
1  2 3 4       2  3  4  5      3  4  5  6
12 1 2 5  ->   1  2  3  6  ->  2  3  4  7
11 4 3 6      12  1  4  7      1  2  1  8
10 9 8 7      11 10  9  8     12 11 10  9

Exemplo Real 1:
=======================
# Input

4 4 2           **(m n r)
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16

#Output

3   4   8   12
2   11  10  16
1   7   6   15
5   9   13  14

#Explanation

 1  2  3  4      2  3  4  8      3  4  8 12
 5  6  7  8      1  7 11 12      2 11 10 16
 9 10 11 12  ->  5  6 10 16  ->  1  7  6 15
13 14 15 16      9 13 14 15      5  9 13 14

Exemplo Real 2:
=======================
# Input

5  4  7         **(m n r)
1  2  3  4
7  8  9  10
13 14 15 16
19 20 21 22
25 26 27 28

#Output

28  27  26  25
22  9   15  19
16  8   21  13
10  14  20  7
4   3   2   1

#Explanation

1  2  3  4      2  3  4 10    3  4 10 16    4 10 16 22
7  8  9 10      1  9 15 16    2 15 21 22    3 21 20 28
13 14 15 16 ->  7  8 21 22 -> 1  9 20 28 -> 2 15 14 27 ->
19 20 21 22    13 14 20 28    7  8 14 27    1  9  8 26
25 26 27 28    19 25 26 27    13 19 25 26   7 13 19 25

10 16 22 28    16 22 28 27    22 28 27 26    28 27 26 25
 4 20 14 27    10 14  8 26    16  8  9 25    22  9 15 19
 3 21  8 26 ->  4 20  9 25 -> 10 14 15 19 -> 16  8 21 13
 2 15  9 25     3 21 15 19     4 20 21 13    10 14 20  7
 1  7 13 19     2  1  7 13     3  2  1  7     4  3  2  1

'''