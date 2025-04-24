def isPrefixOfWord(sentence: str, searchWord: str):
    sen = sentence.split(" ")
    for i in range(0,len(sen)):
        if sen[i].startswith(searchWord):
            return i+1
    return -1

sentence = "i love eating burger"
searchWord = "ll"
print(isPrefixOfWord(sentence,searchWord))