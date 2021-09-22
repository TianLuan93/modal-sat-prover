counts = 1
def getNewAtom(atom):
    global counts
    new_atom = atom + str(counts)
    counts = counts + 1
    return new_atom

def convertAtoms1(X):
    operators = ["|", "-", "[]", "<>", ">>","&"]
    res = []
    d = {}
    for i in range(0, len(X)):
        if X[i] in operators or X[i] == True or X[i] == False:
            continue
        else:
            if X[i] not in d:
                new_atom = getNewAtom('v')
                d[X[i]] = new_atom
                X[i] = new_atom
            else:
                X[i] = d[X[i]]
    return X

def convertAtoms(phi):
    operators = ["|", "-", "[]", "<>", ">>"]
    res = []
    d = {}
    for i in phi:
        if i == [True] or i == [False]:
            tmp = i
        else:
            tmp = []
            for j in i:
                if j in operators or j == True or j == False:
                    tmp.append(j)
                else:
                    if j not in d:
                        new_atom = getNewAtom('x')
                        tmp.append(new_atom)
                        d[j] = new_atom
                    else:
                        tmp.append(d[j])

        res.append(tmp)
    return res

def convertTrueAndFalse(X):
    for i in range(0, len(X)):
        if X[i] ==["true"] or X[i] == ["false","-"]:
            X[i] = [True]
        elif X[i] ==["false"] or X[i] == ["true","-"]:
            X[i] = [False]
    return X

