

import itertools as it

count = 0
def generate_permutation(perm, n):
    if len(perm) == n:
        global count
        count = count +1
        print(perm)
        #exit()


    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_it_be_extended(perm):
                generate_permutation(perm, n)

            perm.pop()


def can_it_be_extended(perm):
    j = len(perm) - 1
    for i in range(len(perm) - 1):
        if j - i == abs(perm[i] - perm[j]):
            return False

    return True



generate_permutation(perm=[], n=8)
print(count)