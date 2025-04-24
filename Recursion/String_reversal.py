def string_reversal(val):    
    if val == '':
        return val

    return (string_reversal(val[1:])+" "+val[0])
    


string_val = 'Sneha'
print(string_reversal(string_val))