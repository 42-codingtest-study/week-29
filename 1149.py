# # 테이블 정의하기
# 
# # 점화식 찾기

n = int(input())
cost = []
for _ in range (n):
    cost.append(list(map(int, input().split())))
dp = [[0] * 3 for _ in range (n)]
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range (1, n) :
    for j in range (3):
        dp[i][j] = cost[i][j] + min(dp[i-1][(j+1) % 3], dp[i-1][(j+2) % 3])

print(min(map(int, dp[n-1])))