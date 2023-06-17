schedule = []
dp = []
N = int(input())
for _ in range(N):
    schedule.append(list(map(int, input().split())))
    dp.append(schedule[-1][1])
dp.append(0)

for i in range(N - 1, -1, -1):
    if schedule[i][0] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], schedule[i][1] + dp[i + schedule[i][0]])
print(dp[0])
