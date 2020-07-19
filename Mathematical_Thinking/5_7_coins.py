def change(amount):
    if amount == 24:
        return [5, 5, 7, 7]

    if amount == 25:
        return [5, 5, 5, 5, 5]

    if amount == 26:
        return [5, 7, 7, 7]

    if amount == 27:
        return [5, 5, 5, 5, 7]

    if amount == 28:
        return [7, 7, 7, 7]

    coins = change(amount - 5)
    coins.append(5)
    return coins


for i in range(24, 1000):

    if i != sum(change(i)):
        print(i)


