def numumSquare(num):
    sum = 0
    while (num):
        ch = num %10
        sum = sum + (ch*ch)
        num = num //10
    return sum

def isHappynumumber(num):
    st = set()
    while(1):
        num = numumSquare(num)
        if num ==1:
            return True
        if num in st:
            return False
        st.add(num)


print(isHappynumumber(19))