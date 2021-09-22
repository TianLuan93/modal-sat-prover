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
    for phi in X0:
        #if isAtom(i):
        if "[]" not in phi and "<>" not in phi:
            s0.add_clause(convertToInputMain(phi))
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
        Aprime = s.get_core()
        return True, Aprime
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
                    #if "[]" not in k2 and "<>" not in k2:
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
                            z = convertToInputMain(k1[1:k1.index(operator)])[0]
                            y = convertToInputMain([k1[0]])[0]
                            if r1[1]:
                                if z in r1[1]:
                                    phi.append(-y)
                            s0.add_clause(phi)
                            phi = convertBack(phi)
                            X.append(phi)
                            r2 = modalSat(X, B, s0)
                            return r2
    return False




