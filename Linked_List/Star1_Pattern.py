def nStarTriangle(n: int) -> None:
    # Write your code here.
    for i in range(0,n):
        for j in range(0,n-i-1):
            print(" ",end="")

        for j in range(0,2*i+1):
            print("*",end="")
        
        for j in range(0,n-1-i):
            print(" ",end="")

        print("")

nStarTriangle(3)