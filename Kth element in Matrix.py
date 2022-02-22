
'''
Given a N x N matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the matrix.

Example 1:
Input:
N = 4
mat[][] =     {{16, 28, 60, 64},
                   {22, 41, 63, 91},
                   {27, 50, 87, 93},
                   {36, 78, 87, 94 }}
K = 3
Output: 27
Explanation: 27 is the 3rd smallest element.
 

Example 2:
Input:
N = 4
mat[][] =     {{10, 20, 30, 40}
                   {15, 25, 35, 45}
                   {24, 29, 37, 48}
                   {32, 33, 39, 50}}
K = 7
Output: 30
Explanation: 30 is the 7th smallest element.


Your Task:
You don't need to read input or print anything. Complete the function kthsmallest() which takes the mat, N and K as input parameters and returns the kth smallest element in the matrix.
 

Expected Time Complexity: O(K*Log(N))
Expected Auxiliary Space: O(N)

Approcah 1:
'''
#User function Template for python3

def kthSmallest(mat, n, k): 
    heapp=[]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            heapp.append(mat[i][j])
            
            if len(heapp)>k:
                heapp.sort()
                heapp.pop()
    return heapp[-1]
  
#approach 2:
def kthSmallest(mat, n, k): 
    res=[]
    for i in range (0,n):
        for j in range(0,n):
            res.append(mat[i][j])
    res.sort()
    return(res[k-1])
            
