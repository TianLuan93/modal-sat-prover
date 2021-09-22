def convert_format(X):
    X = X.replace("box","[]")
    X = X.replace("dia","<>")
    X = X.replace("~", "-")
    X = X.replace("<->", "*")
    X = X.replace("->", ">>")
    X = X.replace("v", "|")
    return X
def convert_format(X):
    X = X.replace("box","[]")
    X = X.replace("dia","<>")
    X = X.replace("~", "-")
    X = X.replace("<->", "*")
    X = X.replace("->", ">>")
    X = X.replace("v", "|")
    return X
