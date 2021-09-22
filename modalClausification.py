from convertNNF import convertNNFMain

counts = 0
def getNewAtom():
    global counts
    new_atom = 'p' + str(counts)
    counts = counts + 1
    return new_atom

phi = []
List = []
def modal_clausification(box_depth = 0):
    global List
    global phi
    opreators = ["[]", "<>", "&", "|"]
    if phi:
        arg = phi.pop()
    else:
        return
    if arg not in opreators:
        if arg == "-":
            new_arg = phi.pop()
            res = [new_arg, "-"]
        else:
            res = [arg]
        for i in range(box_depth):
            res = res + ["[]"]
        return res

    if arg == "[]":
        new_arg = phi[-1]
        # if new_arg not in opreators or new_arg == "[]":
        #     tmp = modal_clausification(box_depth + 1)
        #     return tmp
        if new_arg not in opreators:
            new_atom = getNewAtom()
            t = [new_atom]
            tmp = modal_clausification()
            tmp = [new_atom] + tmp + ["[]", ">>"]
            for i in range(box_depth):
                t = t + ["[]"]
                tmp = tmp + ["[]"]
            List.append(tmp)
        else:
            new_atom = getNewAtom()
            t = [new_atom]
            tmp = modal_clausification(box_depth + 1)
            if type(tmp[0]) != list:
                if len(tmp) != box_depth + 2:
                    new_name = getNewAtom()
                    res = [new_atom, new_name, "[]", ">>"]
                    res1 = [new_name] + tmp[:-(box_depth + 1)] + [">>", "[]"]
                    for i in range(box_depth):
                        t = t + ["[]"]
                        res = res + ["[]"]
                        res1 = res1 + ["[]"]
                    List.append(res)
                    List.append(res1)
                else:
                    res = [new_atom, tmp[0], "[]", ">>"]
                    for i in range(box_depth):
                        t = t + ["[]"]
                        res = res + ["[]"]
                    List.append(res)
            else:
                new_name = getNewAtom()
                res = [new_atom, new_name, "[]", ">>"]
                for i in tmp:
                    if len(i) == box_depth + 2:
                        res1 = [new_name, "-", i[0], "|", "[]"]
                    else:
                        res1 = [new_name] + i[:-(box_depth + 1)] + [">>", "[]"]
                    for i in range(box_depth):
                        res1 = res1 + ["[]"]
                    List.append(res1)
                for i in range(box_depth):
                    t = t + ["[]"]
                    res = res + ["[]"]
                List.append(res)
        return t
    elif arg == "<>":
        new_arg = phi[-1]
        new_atom = getNewAtom()
        t = [new_atom]
        if new_arg not in opreators:
            tmp = modal_clausification()
            tmp = [new_atom] + tmp + ["<>", ">>"]
            for i in range(box_depth):
                t = t + ["[]"]
                tmp = tmp + ["[]"]
            List.append(tmp)
        else:
            tmp = modal_clausification(box_depth + 1)
            if type(tmp[0]) != list:
                if len(tmp) != box_depth + 2:
                    new_name = getNewAtom()
                    res = [new_atom, new_name, "<>", ">>"]
                    res1 = [new_name] + tmp[:-(box_depth + 1)] + [">>", "[]"]
                    for i in range(box_depth):
                        t = t + ["[]"]
                        res = res + ["[]"]
                        res1 = res1 + ["[]"]
                    List.append(res)
                    List.append(res1)
                else:
                    res = [new_atom, tmp[0], "<>", ">>"]
                    for i in range(box_depth):
                        t = t + ["[]"]
                        res = res + ["[]"]
                    List.append(res)
            else:
                new_name = getNewAtom()
                res = [new_atom, new_name, "<>", ">>"]
                for i in tmp:
                    if len(i) == box_depth + 2:
                        res1 = [new_name, "-", i[0], "|", "[]"]
                    else:
                        res1 = [new_name] + i[:-(box_depth + 1)] + [">>", "[]"]
                    for i in range(box_depth):
                        res1 = res1 + ["[]"]
                    List.append(res1)
                for i in range(box_depth):
                    t = t + ["[]"]
                    res = res + ["[]"]
                List.append(res)
        return t
    elif arg == "|":
        tmp = modal_clausification(box_depth)
        tmp1 = modal_clausification(box_depth)
        res = []
        if type(tmp[0]) != list and type(tmp1[0]) != list:
            if box_depth>0:
                res = tmp[:-box_depth] + tmp1[:-box_depth] + ["|"]
            else:
                res = tmp + tmp1 + ["|"]
            for i in range(box_depth):
                res = res + ["[]"]
        elif type(tmp[0]) == list and type(tmp1[0]) != list:
            for i in tmp:
                if box_depth > 0:
                    result = i[:-box_depth] + tmp1[:-box_depth] + ["|"]
                else:
                    result = i + tmp1 + ["|"]
                for j in range(box_depth):
                    result = result + ["[]"]
                res.append(result)
        elif type(tmp[0]) != list and type(tmp1[0]) == list:
            for i in tmp1:
                if box_depth > 0:
                    result = i[:-box_depth] + tmp[:-box_depth] + ["|"]
                else:
                    result = i + tmp + ["|"]
                for j in range(box_depth):
                    result = result + ["[]"]
                res.append(result)
        else:
            for i in tmp:
                for j in tmp1:
                    if box_depth > 0:
                        result = i[:-box_depth] + j[:-box_depth] + ["|"]
                    else:
                        result = i + j + ["|"]
                    for m in range(box_depth):
                        result = result + ["[]"]
                    res.append(result)
        return res
    elif arg == "&":
        res = []
        tmp = modal_clausification(box_depth)
        if type(tmp[0]) == list:
            res = res + tmp
        else:
            res.append(tmp)
        tmp1 = modal_clausification(box_depth)
        if type(tmp1[0]) == list:
            res = res + tmp1
        else:
            res.append(tmp1)
        return res

def modal_clausification_main(X):
    global phi
    phi = X.copy()
    res = modal_clausification()
    if type(res[0]) == list:
        return res + List
    else:
        List.append(res)
        return List
