
'''
Given an m x n matrix, find all common elements present in all rows in O(mn) time and one traversal of matrix.
Example: 

Input:
mat[4][5] = {{1, 2, 1, 4, 8},
             {3, 7, 8, 5, 1},
             {8, 7, 7, 3, 1},
             {8, 1, 2, 7, 9},
            };

Output: 
1 8 or 8 1
8 and 1 are present in all rows
'''
d={}
arr = [[1, 2, 1, 4, 8,9],
       [3, 7, 8, 5, 1,9],
       [8, 7, 7, 3, 1,9],
       [8, 1, 2, 7, 9,9]]
       
for i in range(len(arr[0])):
    if arr[0][i] not in d:
        d [arr[0][i]]=0
res=[] 
#print(res)
temp=len(arr)-1
for row in range(1,len(arr)):
    for col in range(len(arr[0])):
        if arr[row][col] in d and d[arr[row][col]]==row-1:
            d[arr[row][col]]=d[arr[row][col]]+1
            
for i in d:
    if d[i]==temp:
        print(i)
