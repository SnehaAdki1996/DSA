
def minJumps(arr):
    jump = 0
    curr_jump_end = 0
    max_jump = 0
    
    if arr[0] == 0:
        return -1
    for i in range(0, len(arr) - 1):
        
        max_jump = max(max_jump, i + arr[i])
        if i == curr_jump_end and max_jump != 0:
            jump += 1
            curr_jump_end = max_jump
            if curr_jump_end >= len(arr) - 1:
                return jump
    if i >= max_jump:
        return -1
        
    return -1


# arr=[0,10,20]
arr = [1,3,5,8,9,2,6,7,6,8,9]
print(minJumps(arr))