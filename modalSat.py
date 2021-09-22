from pysat.solvers import Minisat22
from convertToInput import convertToInputMain

def ModalSatMain(X0):
    global s0
    s0 = Minisat22()    # s0 <- newSolver()
    # add all atoms and constraints which box depth is 0
    for phi in X0:
        if "[]" not in phi.clause and "<>" not in phi.clause:
            s0.add_clause(convertToInputMain(phi.clause))
            # print (convertToInputMain(phi.clause))
    r = ModalSat(X0, [], s0, 0)
    if r == False:
        return "SAT"
    else:
        return "UNSAT"

def ModalSat(X, A, s, boxDepth):
    r0 = s.solve(A) # r0 <- satProve(s, A)
    sub_A = s.get_core() # A'
    M = s.get_model()
    # print("r0", r0)
    # print("M", M)
    # print("A'", sub_A)
    if r0 == False:
        return True, sub_A
    else:
        for k0 in X:
            if k0.boxDepth == boxDepth and "<>" in k0.clauseInModalContent:
                # print(k0.boxDepth)
                # print("k0",k0.clause)
                # print(boxDepth)

                a = convertToInputMain([k0.clauseInModalContent[0]])[0]
                d = convertToInputMain(k0.clauseInModalContent[1:k0.clauseInModalContent.index('<>')])[0]
                if a in M:
                    s1 = Minisat22()
                    B = [d]
                    for k1 in X:
                        if k1.boxDepth == boxDepth and "[]" in k1.clauseInModalContent:
                            b = convertToInputMain([k1.clauseInModalContent[0]])[0]
                            e = convertToInputMain(k1.clauseInModalContent[1:k1.clauseInModalContent.index('[]')])[0]
                            if b in M:
                                B.append(e)
                    for k2 in X:
                        if k2.boxDepth == boxDepth + 1 and "[]" not in k2.clauseInModalContent and "<>" not in k2.clauseInModalContent:
                            # print("k2",k2.clause)
                            s1.add_clause(convertToInputMain(k2.clauseInModalContent))
                    # print("B", B)
                    r1 = ModalSat(X, B, s1, boxDepth + 1)
                    # print("r1",r1)
                    if r1:
                        sub_A1 = r1[1]
                        if sub_A1:
                            phi = []
                            z = convertToInputMain(k0.clauseInModalContent[1:k0.clauseInModalContent.index("<>")])[0]
                            y = convertToInputMain([k0.clauseInModalContent[0]])[0]
                            if z in sub_A1 and y in M:
                                phi.append(-y)
                            for k1 in X:
                                if "[]" in k1.clauseInModalContent and k1.boxDepth == boxDepth:
                                    z = convertToInputMain(k1.clauseInModalContent[1:k1.clauseInModalContent.index("[]")])[0]
                                    y = convertToInputMain([k1.clauseInModalContent[0]])[0]
                                    if z in sub_A1 and y in M:
                                        # print(k1.clause)
                                        phi.append(-y)
                            # print(k0.clause)
                            # print("M",M)
                            # print("sub_A1",sub_A1)
                            # print("phi", phi)
                            s.add_clause(phi)
                            r2 = ModalSat(X, A, s, boxDepth)
                            # print("r2",r2)
                            return r2
                        else:
                            return True, None
    return False
