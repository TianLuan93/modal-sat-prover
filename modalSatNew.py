from pysat.solvers import Minisat22
from convertToInput import convertToInputMain
from convertBack import convertBack

def isAtom(x):
    if len(x) == 1:
        return True
    elif len(x) == 2:
        if x[-1] == "-":
            return True
        return False
    else:
        return False

s0 = []
def modal_sat_main(X0):
    global s0
    s0 = Minisat22()
    for i in X0:
        #if isAtom(i):
        if "[]" not in i and "<>" not in i:
            print(convertToInputMain(i))
            s0.add_clause(convertToInputMain(i))
    r = modalSat(X0, [], s0)
    if r == False:
        print("UNSAT")
    else:
        print("SAT")
    return

def modalSat(X, A, s):
    global s0
    r0 = s.solve(assumptions = A)
    if r0 == False: # r0 = Yes(A')
        return True, s.get_core()
    else:   # r0 = No(M)
        M = s.get_model()
        for k0 in X:
            if "<>" in k0 and convertToInputMain([k0[0]])[0] in M:
                s1 = Minisat22()
                B = convertToInputMain(k0[1:k0.index('<>')])
                for k1 in X:
                    if "[]" in k1 and convertToInputMain([k1[0]])[0] in M:
                        B = B + convertToInputMain(k1[1:k1.index('[]')])
                for k2 in X:
                    if "|" in k2:
                        s1.add_clause(convertToInputMain(k2))
                r1 = modalSat(X, B, s1)
                if r1:
                    phi = []
                    for k1 in X:
                        if "[]" in k1 or "<>" in k1:
                            if "[]" in k1:
                                operator = "[]"
                            else:
                                operator = "<>"
                            z = convertToInputMain(k1[1:k1.index(operator)])
                            y = convertToInputMain([k1[0]])[0]
                            if z in r1[1]:
                                phi.append(-y)
                            s0.add_clause(phi)
                            phi = convertBack(phi)
                            r2 = modalSat(X.append(phi), B, s0)
                            return r2
    return False




