from __future__ import print_function
from pysat.solvers import Solver  # standard way to import the library
from pysat.solvers import Minisat22, Glucose3  # more direct way
from modalClauses import constructModalClause

s = Minisat22()

# s.add_clause([-1])
s.add_clause([-2])
# s.add_clause([-3])
# s.add_clause([4])
# s.add_clause([-5])
# s.add_clause([6])
# s.add_clause([7])
s.add_clause([False])
# s.add_clause([8,9])
#s.add_clause([-2])
#
print(s.solve(assumptions=[]))
print(s.get_model())
print(s.get_core())
print(s.get_status())

from convertNNF1 import convertNNFMain
X = ['false', '<>', '-']
print(convertNNFMain(X))


