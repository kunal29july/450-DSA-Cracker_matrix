'''
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

 

Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
'''

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        matrix=mat
        n=len(matrix)
        k=0
        while(k<4):
            for i in range(n):
                for j in range (i,n):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                matrix[i].reverse()
            if matrix==target:
                return True
            else:
                k=k+1
        return False
