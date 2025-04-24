import pandas as pd

my_dict = {
    "name" : ['Day1','Day2','Day3'],
    "salary" : [400,420,450]   
}

my_df = pd.DataFrame(my_dict)

# updated_sal: lambda a : a*a

# updated_sal_final = []
# for sal in my_dict['salary']:
#     updated_sal_final.append(sal+sal)


my_df['salary'] = my_df['salary'] * 2

breakpoint()
print(my_df)