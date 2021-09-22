def convertNNFMain(input):
    global phi
    phi = input.copy()
    return convertNNF()

phi = []
def convertNNF():
    global phi
    operators = ["&", "|", "-", ">>", "[]", "<>"]
    if phi:
        arg = phi.pop()
    else:
        return
    if arg not in operators:
        return [arg]

    if arg == ">>":
        tmp = convertNNF() # right arg
        phi = phi + ["-"]
        tmp1 = convertNNF() # left arg
        return tmp + tmp1 + ["|"]
    elif arg == "[]":
        return convertNNF() + ["[]"]
    elif arg == "<>":
        return convertNNF() + ["<>"]
    elif arg == "-":
        new_arg = phi.pop()
        if new_arg not in operators:
            return [new_arg, "-"]
        elif new_arg == "-":
            return convertNNF()
        elif new_arg == "&":
            phi = phi + ["-"]
            tmp = convertNNF()  #r
            phi = phi + ["-"]
            tmp1 = convertNNF() #l
            return tmp1 + tmp + ["|"]
        elif new_arg == "|":
            phi = phi + ["-"]
            tmp = convertNNF()
            phi = phi + ["-"]
            tmp1 = convertNNF()
            return tmp1 + tmp + ["&"]
        elif new_arg == ">>":
            phi = phi + ["-"]
            tmp = convertNNF()
            tmp1 = convertNNF()
            return tmp1 + tmp + ["&"]
        elif new_arg == "[]":
            phi = phi + ["-"]
            return convertNNF() + ["<>"]
        elif new_arg == "<>":
            phi = phi + ["-"]
            return convertNNF() + ["[]"]
    else:
        return convertNNF() + convertNNF() + [arg]
