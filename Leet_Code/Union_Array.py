def union_array(a1,a2):
    for ele in a2:
        if ele not in a1:
            a1.append(ele)

    print(a1)
    print(a2)
    


a1 = [1,2,3,4,5]
a2 = [2,3,7,8,10,4,5,6,7]
union_array(a1,a2)