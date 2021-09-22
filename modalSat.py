from pysat.solvers import Minisat22
from convertToInput import convertToInputMain

def ModalSatMain(X0):
    global s0
    s0 = Minisat22()    # s0 <- newSolver()
    for phi in X0:
        if ("[]" not in phi.cluaseInModalContent or "<>" not in phi.cluaseInModalContent) and phi.boxdepth == 0:
            s0.add_clause(convertToInputMain(phi))
    r = ModalSat(X0, [], s0, 0)
    if r == False:
        return "UNSAT"
    else:
        return "SAT"

def ModalSat(X, A, s, boxDepth):
    return