# from numpy import *
class Solution:
    def luckyNumbers (self, matrix):
        lucky_num =[]
        # print(len(matrix))
        for i in range(len(matrix)):
            min_val = min(matrix[i])
            # print(matrix[i])
            

            for j in range(len(matrix[0])):
                max_val = max(matrix[k][j] for k in range(len(matrix)))  # Find the maximum element in the current column

                print(min_val,max_val)
                if max_val == matrix[i][j] and min_val == matrix[i][j]:
                    lucky_num.append(max_val)
            print(lucky_num)    

        print(lucky_num)
        

# print(luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
s1 = Solution()
s1.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])