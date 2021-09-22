from pysat.solvers import Minisat22
from convertToInput import convertToInputMain
from convertBack import convertBack
from modalClauses import constructModalClause


s0 = []
def modal_sat_main(X0):
    global s0
    s0 = Minisat22()
    for phi in X0:
        if phi == [True] or phi == [False]:
            s0.add_clause(phi)
        elif "[]" not in phi.cluaseInModalContent \
                and "<>" not in phi.cluaseInModalContent \
                and phi.boxDepth == 0:
            s0.add_clause(convertToInputMain(phi.cluaseInModalContent))
    r = modalSat(X0, [], s0, 0)
    if r == False:
        print("UNSAT")
    else:
        print("SAT")
    return

def modalSat(X, A, s, box_depth):
    global s0
    r0 = s.solve(assumptions = A)
    if r0 == False: # r0 = Yes(A')
        Aprime = s.get_core()
        return True, Aprime
    else:   # r0 = No(M)
        M = s.get_model()
        for k0 in X:
            if k0 == [True] or k0 == [False]:
                continue
            if "<>" in k0.cluaseInModalContent and \
                    convertToInputMain([k0.cluaseInModalContent[0]])[0] in M and \
                    k0.boxDepth == box_depth:
                s1 = Minisat22()
                B = convertToInputMain(k0.cluaseInModalContent[1:k0.cluaseInModalContent.index('<>')])
                for k1 in X:
                    if k1 == [True] or k1 == [False]:
                        continue
                    if "[]" in k1.cluaseInModalContent and \
                            convertToInputMain([k1.cluaseInModalContent[0]])[0] in M and \
                            k1.boxDepth == box_depth:
                        B = B + convertToInputMain(k1.cluaseInModalContent[1:k1.cluaseInModalContent.index('[]')])
                for k2 in X:
                    if k2 == [True] or k2 == [False]:
                        continue
                    if "[]" not in k2.cluaseInModalContent and \
                            "<>" not in k2.cluaseInModalContent and \
                            k2.boxDepth == box_depth+1:
                        s1.add_clause(convertToInputMain(k2.cluaseInModalContent))
                #print("B",B)
                r1 = modalSat(X, B, s1, box_depth + 1)
                #print(r1)
                if r1:
                    phi = []
                    z = convertToInputMain(k0.cluaseInModalContent[1:k0.cluaseInModalContent.index("<>")])[0]
                    y = convertToInputMain([k0.cluaseInModalContent[0]])[0]
                    if r1[1]:
                        if z in r1[1] and y in M:
                            #print(k0.clause)
                            phi.append(-y)
                    for k1 in X:
                        if k1 == [True] or k1 == [False]:
                            continue
                        if "[]" in k1.cluaseInModalContent and k1.boxDepth == box_depth:
                            z = convertToInputMain(k1.cluaseInModalContent[1:k1.cluaseInModalContent.index("[]")])[0]
                            y = convertToInputMain([k1.cluaseInModalContent[0]])[0]
                            if r1[1]:
                                if z in r1[1] and y in M:
                                    # print(k1.clause)
                                    phi.append(-y)
                    # print("M:",M)
                    # print("A':",r1[1])
                    # print("phi:",phi)
                    if box_depth == 0:
                        s0.add_clause(phi)
                    print(phi)
                    phi = convertBack(phi)
                    if phi:
                        for i in range(box_depth):
                            phi = phi + ["[]"]
                        phi = constructModalClause([phi])
                        X = X + phi
                    r2 = modalSat(X, [], s0, 0)
                    return r2
    return False




