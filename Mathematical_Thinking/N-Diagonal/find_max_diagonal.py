# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 09:38:11 2020

@author: jithi
"""
import math
from copy import deepcopy

total_possible_diagonals = 0
estimate_global  = 0
def generate_permutation(array, i, j, filled_diagonals, estimate, n):

    global total_possible_diagonals
    global estimate_global
    no_of_cells_remaining = (math.pow(n, 2) - (n * i) - j)
    if total_possible_diagonals < filled_diagonals:
        total_possible_diagonals = filled_diagonals
        estimate_global = total_possible_diagonals + no_of_cells_remaining

    estimate = filled_diagonals + no_of_cells_remaining
    if estimate <= estimate_global:
        return

    if no_of_cells_remaining < total_possible_diagonals - filled_diagonals:
        return

    if i == n:
        return

    if j == n - 1:
        j_nxt = 0
        i_nxt = i + 1

    else:
        j_nxt = j + 1
        i_nxt = i

    generate_permutation(array=deepcopy(array), i=i_nxt, j=j_nxt, filled_diagonals=filled_diagonals, estimate=estimate, n=n)

    if isExtendable(array, i, j, -1, n):
        array[i][j] = -1
        generate_permutation(array=deepcopy(array), i=i_nxt, j=j_nxt, filled_diagonals=filled_diagonals+1, estimate=estimate, n=n)

    if isExtendable(array, i, j, 1, n):
        array[i][j] = 1
        generate_permutation(array=deepcopy(array), i=i_nxt, j=j_nxt, filled_diagonals=filled_diagonals+1, estimate=estimate, n=n)


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
generate_permutation(array=deepcopy(grid), i=0, j=0, filled_diagonals=0, estimate=0, n=nnn)
print(total_possible_diagonals)


