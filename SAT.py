from ModalSatProver import Prove
import sys

def main():
    if len(sys.argv)>1:
        formula = sys.argv[1]
        res = Prove(formula)  
        print("Input Formula is " + res)
    else:
        print("Error: No Input")

if __name__ == "__main__":
    main()
