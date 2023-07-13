class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float: 
        dp = [[0 for i in range(row_len)]for row_len in range(1, query_row + 2)]
        dp[0][0] = poured
        
        for i in range(query_row):
            for j in range(len(dp[i])):
                pour = (dp[i][j] -1) / 2
                
                if pour > 0:
                    dp[i+1][j] += pour
                    dp[i+1][j+1] += pour
                    
        if dp[query_row][query_glass] <= 1:
            return dp[query_row][query_glass]
        else:
            return 1