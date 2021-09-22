counts_v = 1
def getNewAtom_v(atom):
    global counts_v
    new_atom = atom + str(counts_v)
    counts_v = counts_v + 1
    return new_atom

counts_x = 1
def getNewAtom_x(atom, bool = False):
    global counts_x
    new_atom = atom + str(counts_x)
    counts_x = counts_x + 1
    return new_atom

def convertAtoms_v(X):
    operators = ["|", "-", "[]", "<>", ">>","&"]
    d = {}
    for i in range(0, len(X)):
        if X[i] in operators or X[i] == True or X[i] == False:
            continue
        else:
            if X[i] not in d:
                new_atom = getNewAtom_v('v')
                d[X[i]] = new_atom
                X[i] = new_atom
            else:
                X[i] = d[X[i]]
    return X

def convertAtoms_x(phi, bool = False):
    global counts_x
    if bool:
        counts_x = 2
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
                        new_atom = getNewAtom_x('x')
                        tmp.append(new_atom)
                        d[j] = new_atom
                    else:
                        tmp.append(d[j])

        res.append(tmp)
    return res

