def canChange(start: str, target: str):
    start = list(start)
    target = list(target)
    for i in range(0,len(start)) :
        if start[i] != target[i] and start[i] == 'L' and target[i] == '_':
            start[i-1] = 'L'
            start[i] = '_'
        elif start[i] != target[i] and start[i] == 'R' and target[i] == '_':
            start[i+1] = 'R'
            start[i] = '_'
    print(start)
    print(target)

start = "_L__R__R_" 
target = "L______RR"
canChange(start,target)