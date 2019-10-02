#Implement a function that meets the specifications below.
def f(i):
    return i + 1
def g(i):
    return i > 5

L = [0, -10, 3, 2, -4]

def applyF_filterG(L, f, g):
    to_remove = []
    for s in L:
        if not g(f(s)):
            to_remove.append(s)
    for s in to_remove:
        L.remove(s)
    return max(L) if L != [] else -1

print(applyF_filterG(L, f, g))
print(L)
