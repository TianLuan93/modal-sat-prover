def generateAtom(num):
    if num >= 0:
        return ['x' + str(num)]
    else:
        return ['x' + str(abs(num)), "-"]

def convertBack(X):
    if not X:
        return X
    res = []
    if len(X) == 1:
        res = generateAtom(X[0])
    else:
        res = generateAtom(X[0])
        for i in range(1, len(X)):
            res = res + generateAtom(X[i])
            res.append("|")
    return res
