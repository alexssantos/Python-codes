'''
https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-given-a-list-containing-it-in-python

>>> [1, 1].index(1)
0
>>> [i for i, e in enumerate([1, 2, 1]) if e == 1]
[0, 2]
>>> g = (i for i, e in enumerate([1, 2, 1]) if e == 1)
>>> next(g)
0
>>> next(g)
2
'''

