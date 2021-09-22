---------------------------- SATbased Prover ---------------------------  
This is a SAT-based Theorem Prover for Modal Logic K written by Tian   
Luan.  
---------------------------------------------------------------------------  
----------------------------- Environments ------------------------------  
This prover is based on Python 3.8.5 and the only additional library is  
PySat, to run the solver you need to intall it first, this can be  
installed by following command:  
$ pip install python-sat  
---------------------------------------------------------------------------  
------------------------------- Usage ------------------------------------  
python SAT.py "fml"  
This SAT-based Prover will read one parameter (required) as a modal  
logic formula, then it  
will return whether this formula is provable (valid) or not. The whole  
process behind it  
is first negate the input and then determine whether the negation is  
satisfiable.  
The prover accepts formuae in the following syntax:  
fml ::= '(' fml ')' ( parentheses )  
| 'true' ( truth )  
| 'false' ( falsehood )  
| '-' fml ( negation )  
| '<>' fml ( diamonds )  
| '[]' fml ( boxes )  
| fml '&' fml ( conjunction )  
| fml '|' fml ( disjunction )  
| fml '->' fml ( implication )  
| fml '<->' fml ( equivalence )  
| a | b | c | .... ( classical literals )  
-------------------------------------------------------------------------  
---------------------------- Using Example ----------------------------  
$ python SAT.py "[](p->q)->([]p->[]q)"  
This will return: Input Formula is Provable  
-------------------------------------------------------------------------  
------------------------------ Authors ---------------------------------  
Tian Luan  
-------------------------------------------------------------------------  
---------------------------- Acknowledgement ------------------------  
Professor Rajeev Gore  
-------------------------------------------------------------------------  