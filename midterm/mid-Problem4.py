listA = [1, 2, 3]
listB = [4, 5, 6]

def dotProduct(listA, listB):
    w = 0
    for i in range(0, len(listA)):
        w += listA[i]*listB[i]
    return w

print(dotProduct(listA, listB))


