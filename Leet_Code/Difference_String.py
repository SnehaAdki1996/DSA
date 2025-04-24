def findTheDifference(str1: str, target: str) -> str:
    sum_s,sum_t = 0,0
    for ss in str1:
        sum_s += ord(ss)

    for tt in target:
        sum_t += ord(tt)

    return chr(sum_t - sum_s)
    # dif = ""
    # for each in target:
    #     if str1.find(each) < 0:
    #         dif = dif + each

    # print(dif)


print(findTheDifference('aa','aaa'))