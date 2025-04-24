import functools
def romanToInt(s: str):
    dict ={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
    }

    sum = 0

    values = []
    for index,val in enumerate(s):
        if len(values) and values[len(values)-1] < dict[val]:
                values[len(values)-1] = -abs(values[len(values)-1])
                values.append(dict[val])
        else:
            values.append(dict[val])
            
    return functools.reduce(lambda a,b : a+b,values)

print(romanToInt("IV"))
