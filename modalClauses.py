from convertNNF import convertNNFMain

class modalClause:
    def __init__(self):
        self.clause = []     # clause
        self.boxDepth = 0     # modal depth
        self.clauseInModalContent = []

def popModalContext(phi):
    arg = phi[-1]
    if arg != "[]":
        return phi
    else:
        return popModalContext(phi[:-1])

def calDepth(clause):
    box_depth = 0
    for arg in clause[::-1]:
        if arg != "[]":
            return box_depth
        else:
            box_depth = box_depth + 1
    return box_depth

def constructModalClause(X):
    res = []
    if X:
        for clause in X:
            tmp = popModalContext(clause)
            if "[]" not in tmp and "<>" not in tmp:
                clause = convertNNFMain(clause)
                tmp = convertNNFMain(tmp)
            new = modalClause()
            new.clause = clause
            new.boxDepth = calDepth(clause)
            new.clauseInModalContent = tmp
            res.append(new)
    return res
