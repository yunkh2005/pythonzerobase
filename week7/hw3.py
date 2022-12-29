def solution(s1, s2, s3):
    m, n = len(s1), len(s2)

    if m + n != len(s3):
        return False
    
    
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s3[i - 1] == s1[i - 1]

    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s3[j - 1] == s2[j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] and  s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
            
    return dp[m][n]

print(solution("aabcc", "dbbca", "aadbbcbcac"))     # True
print(solution("aabcc", "dbbca", "aadbbbaccc"))     # False
# https://8iggy.tistory.com/248?category=972493