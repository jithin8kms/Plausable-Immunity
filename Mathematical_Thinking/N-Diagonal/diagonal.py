# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 09:38:11 2020

@author: jithi
"""
import math
from copy import deepcopy

def print_diagonal(array):
    mapping = {0: " ", 1: "\\", -1: "/"}
    for i in range(0, len(array)):
        print(*[mapping[el] for el in array[i]])
    print("\n\n")


def generate_permutation(array, i, j, filled_diagonals, tot_diagonals, n):

    if filled_diagonals == tot_diagonals:
        print_diagonal(array)
        return

    no_of_cells_remaining = (math.pow(n, 2) - (n * i) - j)

    if no_of_cells_remaining < tot_diagonals - filled_diagonals:
        return

    if j == n - 1:
        j_nxt = 0
        i_nxt = i + 1

    else:
        j_nxt = j + 1
        i_nxt = i

    generate_permutation(array=[x[:] for x in array], i=i_nxt, j=j_nxt, filled_diagonals=filled_diagonals, tot_diagonals=tot_diagonals, n=n)

    if isExtendable(array, i, j, -1, n):
        array[i][j] = -1
        generate_permutation(array=[x[:] for x in array], i=i_nxt, j=j_nxt, filled_diagonals=filled_diagonals+1, tot_diagonals=tot_diagonals, n=n)

    if isExtendable(array, i, j, 1, n):
        array[i][j] = 1
        generate_permutation(array=[x[:] for x in array], i=i_nxt, j=j_nxt, filled_diagonals=filled_diagonals+1, tot_diagonals=tot_diagonals, n=n)


def isExtendable(array, i, j, fill, n):

    if i != 0:
        if array[i - 1][j] == -fill:
            return False

    if j != 0:
        if array[i][j - 1] == -fill:
            return False

    if fill != 1 and j != n-1 and i != 0:
        if array[i - 1][j + 1] == fill:
            return False

    if fill != -1 and j != 0 and i != 0:
        if array[i - 1][j - 1] == fill:
            return False

    return True

nnn = 5

grid = [[0 for i in range(nnn)] for j in range(nnn)]
generate_permutation(array=[x[:] for x in grid], i=0, j=0, filled_diagonals=0, tot_diagonals=16, n=nnn)
