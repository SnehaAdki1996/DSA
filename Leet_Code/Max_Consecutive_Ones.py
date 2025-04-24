def max_Ones(arr):
    max_ones = 0
    max_counter = 0

    for ele in arr:
        if ele == 1:
            max_ones +=1
        elif ele ==0:
            if max_counter < max_ones:
                max_counter = max_ones
            max_ones = 0

    print(max(max_counter,max_ones))


arr = [1,0,1,1,0,1]
max_Ones(arr)

