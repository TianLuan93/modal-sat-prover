def ConvertFormat(X):
    X = X.replace("box","[]")
    X = X.replace("dia","<>")
    X = X.replace("~", "-")
    X = X.replace("->", ">>")
    X = X.replace("v", "|")
    return X
