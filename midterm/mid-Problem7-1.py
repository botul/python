#Implement a function that meets the specifications below.
def f(i):
    return i + 1
def g(i):
    return i > 5

L = []

def applyF_filterG(L, f, g):
    maks = 0
    K = []
    for i in L:
        if not g(f(i)):
            K.append(i)

    for k in K:
        if k in L:
            L.remove(k)
    if len(L)>0:
        maks=max(L)
    else:
        maks=-1

    return maks
print(applyF_filterG(L, f, g))
print(L)

