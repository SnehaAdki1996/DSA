def addBinary(d1: str, d2: str):
    sum = ""
    carry = 0
    d1,d2 = d1[::-1],d2[::-1]

    for i in range(max(len(d1),len(d2))):
        print(ord(d1[i]))
        digitA = ord(d1[i]) - ord("0") if i < len(d1) else 0
        digitB = ord(d2[i]) - ord("0") if i < len(d2) else 0

        total = digitA + digitB + carry        
        carry = total %2
        sum =sum + str(carry)
        carry = total // 2

    sum =sum + str(carry) if carry else sum
    return sum
    # # print(carry)
    # # print(sum[::-1])
    # print("{} {} is {} ".format(d1[::-1],d2[::-1],sum[::-1]))
    # print("-------------")
    # sum = (sum + str(carry)) if carry else sum

    

addBinary("1010","1010")
addBinary("10","1010")
addBinary("11","11")