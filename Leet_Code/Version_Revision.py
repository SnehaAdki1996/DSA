def compareVersion(version1: str, version2: str):
    v1_arr = version1.split('.')
    v2_arr = version2.split('.')
    
    if len(v1_arr) > len(v2_arr):
        sub_arr = [0 for i in range(0,len(v1_arr)-len(v2_arr))]
        v2_arr += sub_arr
    elif len(v1_arr) < len(v2_arr):
        sub_arr = [0 for i in range(0,len(v2_arr)-len(v1_arr))]
        v1_arr += sub_arr

    for i in range(0,max(len(v1_arr),len(v2_arr))):
        if int(v1_arr[i]) < int(v2_arr[i]):
            return -1
        elif int(v1_arr[i]) > int(v2_arr[i]):
            return 1
        
    return 0




print(compareVersion('1.0.1','1'))