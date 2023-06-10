## 1
# 1
## 2
# 11
# 2
## 3
# 111
# 21
# 12
## 4
# 1111
# 211
# 121
# 112
# 22

n = int(input())
dp = [0 for _ in range(n+2)]
dp[1] = 1
dp[2] = 2
if n > 2 :
    for i in range(3, n+1) :
        dp[i] = dp[i-2] + dp[i-1]
        dp[i] %= 10007

print(dp[n])
