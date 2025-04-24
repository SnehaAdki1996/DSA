list = [10,35,20,30,50]
list.sort()
max = 0
nd_max = 0
for i in range(0,len(list)):

    if list[i]>max: ## 30 > 35
        nd_max = max  ## 10
        max = list[i]  ## max=35



print(nd_max)


#2nd max without sort