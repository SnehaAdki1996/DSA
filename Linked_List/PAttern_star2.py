n = 4
num = 4
# Write your solution here.
for i in range(0,n*2-1):
    for j in range(0,n*2-1):
        top = i
        bottom = j
        left = (2*n-2)-i
        right = (2*n-2)-j
        print(n-min(min(left,right),min(top,bottom)),end="")
    print("")