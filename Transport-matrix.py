class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        res = []
        arr = []

        for i in range (len(matrix[0])):
            for j in range (len(matrix)):
                arr.append(matrix[j][i])
            res.append(arr)
            arr = []
        return res