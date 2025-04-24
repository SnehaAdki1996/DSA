# Shops opening and closing times are given in an array, and people's entry time is given in an array. '
# 'We need to find out how many shops are open when i'th person enters.

shops = [(1, 5), (2, 8), (4, 6)]
entry_times = [3, 7, 9]



shop_each_entry_per = []
for entry_time in entry_times:
    count = 0
    for shop_start,shop_end in shops:
        if shop_start <= entry_time and entry_time <= shop_end:
            count+=1
    shop_each_entry_per.append(count)


print(shop_each_entry_per)
    
