def reverseVowels(string_val: str):
    i = 0
    string_val = [i for i in string_val] 
    vowels = ['a','e','i','o','u']
    end= len(string_val)-1
    while i<end:
        if string_val[i].lower() not in vowels:
            i+=1
        if string_val[end].lower() not in vowels:
            end-=1
        if string_val[i].lower() in vowels and string_val[end].lower() in vowels:
            string_val[i],string_val[end]=string_val[end],string_val[i]
            i+=1
            end-=1
    print("".join(string_val))
        

reverseVowels('aA')