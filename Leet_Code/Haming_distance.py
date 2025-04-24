x =2 
y = 4

diff = 0

bin_x = bin(x).replace("0b","")
bin_y = bin(y).replace("0b","")

print(bin_x)
print(bin_y)
print("-------")
if len(bin_x)>len(bin_y):
    bin_y = '0'*(len(bin_x)-len(bin_y)) + bin_y
else:
    bin_x = '0'*(len(bin_y)-len(bin_x)) + bin_x

print(bin_x)
print(bin_y)
for i in range(0,len(bin_y)):
    if bin_x[i] != bin_y[i]:
        diff = diff +1

print(diff)