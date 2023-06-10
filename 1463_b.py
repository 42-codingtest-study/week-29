# 시간 : 560ms
n = int(input())
dp = [0 for _ in range(0, n + 1)]

for i in range(2, n + 1) :
    dp[i] = dp[i-1] + 1
    if not i % 3 :
        dp[i] = min(dp[i//3] + 1, dp[i])
    if not i % 2 :
        dp[i] = min(dp[i//2] + 1, dp[i])

print(dp[n])
