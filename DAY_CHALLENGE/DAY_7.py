def convert( s,numRow):
    if numRow == 1:
        return s
    
    res = ""

    for r in range(numRow):
        inc = 2*(numRow-1)
        for i in range(r,len(s),inc):
            res+=s[i]
            if r>0 and r<numRow-1 and i + inc-2 * r < len(s):
                res+=s[i + inc-2 * r ]
    print(res)
        


s = "PAYPALISHIRING"
numRows = 4
convert(s,numRows)