a = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

ta = []

# r*c

for i in range(0,len(a)):
    sub_Arr = []
    for j in range(0,len(a)):
        sub_Arr.append(a[j][i])
    # print(sub_Arr)
    ta.append(sub_Arr)

print(ta)