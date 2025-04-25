def findDuplicates( arr):
    # code here
    seen = set()
    duplicates = set()
    for i in range(0,len(arr)):
        if arr[i] in seen:
            duplicates.add(arr[i])
        else:
            seen.add(arr[i])

    print(duplicates)

findDuplicates([1,2,3,1,5,5])
        