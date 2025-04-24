
# +----+---------+----------+-----+
# | id | first   | last     | age |
# +----+---------+----------+-----+
# | 1  | Mason   | King     | 6   |
# | 2  | Ava     | Wright   | 7   |
# | 3  | Taylor  | Hall     | 16  |
# | 4  | Georgia | Thompson | 18  |
# | 5  | Thomas  | Moore    | 10  |


import pandas as pd

my_dic = {
    'id':[1,2,3],
    'first':['Sneha','Vijay','Sheetal'],
    'last' : ['Adki','Konkati','Ad'],
    'age' : [28,26,24]
}

my_stu = pd.DataFrame(my_dic)

my_stu.rename(columns = {'id':'student_id','first':'first_name','last':'last_name','age':'age_in_years'},inplace= True)

print(my_stu)