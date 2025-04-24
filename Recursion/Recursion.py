def recur(ele):
    if ele == 6:
        return ele
    if ele == 8:
        return ele

    return recur(ele-1)



print(recur(10))
pass