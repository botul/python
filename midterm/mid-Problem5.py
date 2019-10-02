d = {1:10, 2:20, 3:30}

def dict_invert(d):
    nowyD = {}
    for item in d:
        if d[item] in nowyD:
            nowyD[d[item]].append(item)
            nowyD[d[item]].sort()
        else:
            nowyK = d[item]
            nowyD[nowyK] = []
            nowyD[nowyK].append(item)
    return nowyD

dict_invert(d)
