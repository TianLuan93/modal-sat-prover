phi = []
def convertToInput():
    global phi
    operators = ["|", "-"]
    if phi:
        arg = phi.pop()
    else:
        return
    if arg == True or arg == False:
        return [arg]
    if arg not in operators:
        return [int(arg[1:])]
    elif arg == "|":
        tmp1 = convertToInput()
        tmp2 = convertToInput()
        if type(tmp1) == list and type(tmp2) == list:
            res = []
            for i in tmp1:
                res.append(i)
            for i in tmp2:
                res.append(i)
            return res
        elif type(tmp1) != list and type(tmp2) == list:
            res = []
            res.append(tmp1)
            for i in tmp2:
                res.append(i)
            return res
        elif type(tmp1) == list and type(tmp2) != list:
            res = []
            for i in tmp1:
                res.append(i)
            res.append(tmp2)
            return res
        else:
            return [tmp1 , tmp2]
    elif arg == "-":
        new_arg = phi.pop()
        return [-int(new_arg[1:])]

def convertToInputMain(X):
    global phi
    phi = X.copy()
    return convertToInput()