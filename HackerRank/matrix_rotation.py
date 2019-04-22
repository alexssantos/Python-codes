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


MATRIZ 5x5
[ 1, 2, 3, 4, 5]
[ 1, 2, 3, 4, 5]
[ 1, 2, 3, 4, 5]
[ 1, 2, 3, 4, 5]
[ 1, 2, 3, 4, 5]
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.


def matrixRotation(matrix, r):
    # mapear todos os aneis da matriz em um lista de tuplas.
    # >> matrix Y1=> [ [x1],[x2],[x3] ],  M=X e N=Y.
    #           Y2=> [ [x1],[x2],[x3] ]...
    x_max_length = len(matrix[0])
    y_max_length = len(matrix)
    matrix_list_laps = []

    x_aux = x_max_length
    y_aux = y_max_length
    ixLap = 0
    # MAP List of Laps
    #FIXME: Laps com (0,0) fixos sempre como se a volta fosse a borda. 
    #FIXME: Mapear de dentro para fora.
    while not x_aux < 2 or not y_aux < 2:
        # GET matrix laps  // MAX LENGTH by LAP = (X*2 + Y*2 - 4)
       
        lap_length = (y_aux*2 + x_aux*2 - 4)    # -4 pq as pontas repetem.
        lap = []

        # LINHA 0
        line = range(ixLap, x_aux - ixLap)    #[(0, x-1) for line in matrix if (matrix.index(line) == 0) for x in line]
        firstLine = [(ixLap, x) for x in line]
        if len(firstLine) != (x_aux): 
            print(f"ERRO Linha 0 - MATRIZ {x_aux}x{y_aux}")
            break
        lap.extend(firstLine)

        # Ultima Coluna
        column = range(ixLap, y_aux)
        lastColumn = [(y - ixLap, x_aux-1 + ixLap) for y in column if(column.index(y) != 0 and column.index(y) != y_aux-1)]
        if len(lastColumn) != (y_aux-2): 
            print(f"ERRO Coluna {x_aux} - MATRIZ {x_aux}x{y_aux}")
            break
        lap.extend(lastColumn)
        
        # Ultima Linha
        revLine = range(x_aux)[::-1]    
        lastLine = [(y_aux-1 + ixLap, x - ixLap) for x in revLine]  # run last X reverse
        if len(lastLine) != (x_aux): 
            print(f"ERRO Linha {y_aux} - MATRIZ {x_aux}x{y_aux}")
            break
        lap.extend(lastLine)

        # Coluna 0
        revColumn = range(y_aux)[::-1]
        firstColumn = [(y, 0) for y in revColumn if(revColumn.index(y) != 0 and revColumn.index(y) != y_aux-1)]
        if len(firstColumn) != (y_aux-2): 
            print(f"ERRO Coluna 0 - MATRIZ {x_aux}x{y_aux}")
            break
        lap.extend(firstColumn)

        matrix_list_laps.append(lap)
        if len(lap) == lap_length:
            print(f"MATRIZ {x_aux}x{y_aux} - OK")       
        
        ixLap += 1
        x_aux -= 2
        y_aux -= 2
    
    # ALL INDEX (Y(X)) got caught
    # >> matrix_list_laps, listas ordenadas por ordem decrescente do tamanho da lap da matriz.
    matrixNew = []    
    matrixNew.extend([[0 for x in range(x_max_length)] for x in range(y_max_length)])  # Matrix com Listas vazias. 

    for lapYXPosList in matrix_list_laps:
        # pegar os valores de acordo com as pos da LapList
        ValuesOlsPos = []
        for yx in lapYXPosList:
            ValuesOlsPos.append(matrix[yx[0]][yx[1]])
        
        # get real index 0 after rotate.
        posListLength = len(lapYXPosList)        
        if r > posListLength:
            ix = (lapYXPosList % r)
        else:
            ix = r
        
        # Realocar valores na lista // contar R posições e realocar o primeiro item nessa posição e os seguintes. 
        ixList = [x for x in range(ix, posListLength)]
        ixList.extend([x for x in range(0, ix)])
        ValuesNewList = []
        n = 0
        # quem estava no ix =0 vai para ix = i
        for i in ixList:
            ValuesNewList.insert(i, ValuesOlsPos[n])
            n += 1        
        # Map valores na matrixNew com map 'lapYXPosList' e valores 'ValuesNewPos'
        n = 0
        for xy in lapYXPosList:     # xy -> (item, index)
            matrixNew[xy[0]][xy[1]] = ValuesNewList[n]
            n += 1
    for lineList in matrixNew:
        print(lineList)
    input("<<  FINISH  >> ")

    
if __name__ == '__main__':
    mnr = input("DIGITE a Matriz (m n r) \n >>>").rstrip().split()

    m = int(mnr[0])
    n = int(mnr[1])
    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
