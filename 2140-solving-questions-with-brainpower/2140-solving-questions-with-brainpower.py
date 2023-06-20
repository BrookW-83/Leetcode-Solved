class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)

        for i in range(n -1, -1, -1):
            p, bp = questions[i]

            curr = i + bp + 1
            if curr >= n:
                curr = n

            dp[i] = max(dp[i + 1], p + dp[curr])

        return dp[0]

