def reversePrefix(word: str, ch: str) -> str:
    index  = word.find(ch)
    if index == -1 :
        return word
    word = word[:index+1][::-1] + word[index+1:]
    return word

print(reversePrefix('xyxzxe','z'))

# expected -> dcbaefd zxyxxe