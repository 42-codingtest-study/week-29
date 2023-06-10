# # 테이블 정의하기
# D[i] = i
# # 점화식 찾기
# D[12] = ?
# 1. 3으로 나누거나 (D[4] + 1)
# 2. 2로 나누거나 (D[6] + 1)
# 3. 1을 빼거나 (D[11] + 1)
# D[12] = min(1, 2, 3)
# # 점화식에서는 초기값이 무조건 있어야 함.
############## 설명 끝 ###################
# 시간 : 468ms
n = int(input())
dp = [0 for _ in range(0, n + 1)]

for i in range(2, n + 1) :
    if not i % 3 :
        if not i % 2 :
            dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
        else :
            dp[i] = min(dp[i//3], dp[i-1]) + 1
    elif not i % 2 :
        dp[i] = min(dp[i//2], dp[i-1]) + 1
    else :
        dp[i] = dp[i-1] + 1

print(dp[n])
