n=3
for i in range(1,(n*2)):
    stars = i

    if i > n :
        stars = 2*n-i

    for j in range(0,stars):
        print("*",end="")

    print("")


