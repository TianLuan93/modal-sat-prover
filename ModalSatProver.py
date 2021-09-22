from ConvertTestFormat import convert_format
from shuntingYard import shunting_yard
from convertNNF import convertNNFMain
from convertAtoms import convertAtoms_x, convertAtoms_v
from modalClausification import modal_clausification_main
from modalClauses import constructModalClause
from modalSat import ModalSatMain

def Prove(formula):
    formula = convert_format(formula)
    formula = "-("+formula+")"
    # print("formula", formula)
    parsing_fml = shunting_yard(formula)
    # print("parsing",parsing_fml)
    nnf_fml = convertAtoms_v(convertNNFMain(parsing_fml))
    # print("negation normal form", nnf_fml)
    if True in nnf_fml:
        modal_clauses = convertAtoms_x(modal_clausification_main(nnf_fml),True)
    else:
        modal_clauses = convertAtoms_x(modal_clausification_main(nnf_fml))
    # print("modal clauses", modal_clauses)
    input_clauses = constructModalClause(modal_clauses)
    res = ModalSatMain(input_clauses)
    if res == "UNSAT":
        return "Provable"
    else:
        return "Not Provable"





