def findRelativeRanks(score):
    sort_score = score.copy()
    sort_score.sort(reverse = True)
    print(sort_score)
    result = [None] * (len(score))
    rank = 0
    for i in range(0,len(sort_score)):
        index = score.index(sort_score[i])
        if i ==0:
            result[index] = 'Gold Medal'
            rank = rank+1
        elif i ==1:
            result[index] = 'Silver Medal'
            rank = rank+1
        elif i ==2:
            result[index] = 'Bronze Medal'
            rank = rank+1
        else:
            rank = rank+1
            result[index] = rank
    print(result)
    return result

findRelativeRanks([5,4,3,2,1])
findRelativeRanks([10,3,8,9,4])