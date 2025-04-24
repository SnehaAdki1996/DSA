def numRescueBoats(people, limit):
    res =0
    people.sort()
    l,r = 0 ,len(people)-1

    while l <= r:
        remaining = limit - people[r]
        r -=1
        res +=1
        if l<=r and remaining >= people[l]:
            l+=1
    
    return res

people= [3,5,1,4]
limit = 5
print(numRescueBoats(people, limit))