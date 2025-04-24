def maximumGain(org_val,x,y):
    # x = 'ab' 4
    # y='ba' 5
    stackx =[]
    count = 0
    if y > x:
        count,stackx= get_count(stackx,org_val,y,count,'ba')
    else:
        count,stackx= get_count(stackx,org_val,x,count,'ab')
    print(stackx,count)
    stacky =[]
    if y > x :
        count,stacky= get_count(stacky,stackx,x,count,'ab')
    else:  
        count,stacky= get_count(stacky,stackx,y,count,'ba')

    print(count)


def get_count (stackx,org_val,y,count,cmp):
    for i in org_val:
        if i == cmp[-1] and len(stackx)!=0 and stackx[-1] ==cmp[0]: #check for ba
            count+=y
            stackx.pop()
        else:
            stackx.append(i)
    return count,stackx

maximumGain("aabbaaxybbaabb",5,4)