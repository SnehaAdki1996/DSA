from collections import deque 
def findTheWinner(n,k):
    arr = deque()

    for i in range(1,n+1):
        arr.append(i)

    while len(arr)>1:
        for i in range(0,k-1):
            arr.append(arr.popleft())

        arr.popleft()

    print(arr[0])

     
findTheWinner(n=6,k=5)