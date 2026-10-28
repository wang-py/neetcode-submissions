class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix)
        m = b
        r = len(matrix[0])

        for i in range(t, b):
            l = 0
            n = r
            for j in range(l, r):
                print(f'matrix[i][j] is {matrix[i][j]}')
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:
                    l = l + n // 2
                    n = n // 2
                    continue
                elif matrix[i][j] > target:
                    return False
        
        return False
