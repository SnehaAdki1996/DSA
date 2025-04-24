
def verify_pattern(str_val):
    stack = []
    mapping = {")":"(","}":"{","]":"["}
    for ch in str_val:
        if ch in mapping.values():
            stack.append(ch)
        elif ch in mapping.keys():
            if not stack or mapping[ch] != stack.pop():
                breakpoint()
                return False
    return not stack


print(verify_pattern(str_val='([)]'))