# # 테이블 정의하기
# D[i][j] = 현재까지 j개의 계단을 연속해서 밟고 i번째 계단까지 올라섰을 떄
# 			점수합의 최댓값, 반드시 i번째 밟아야 함.
# # 점화식 찾기
# D[k][1] = max(D[k-2][1], D[k-2][2]) + S[k]
# D[k][2] = D[k-1][1] + S[k]
# result = max(D[k][1], D[k][2])
# # 점화식에서는 초기값이 무조건 있어야 함.
# D[1][1] = S[1], D[1][2] = 0
# D[2][1] = S[2], D[2][2] = S[1] + S[2]
############## 설명 끝 ###################
n = int(input())
stairs = [0]
for _ in range (n):
	stairs.append(int(input()))
if n == 1 :
	print(stairs[1])
	exit()
# 초기값 설정하기
dp = [[0] * 3 for _ in range(n+1)]
dp[1][1] = stairs[1]
dp[1][2] = 0
dp[2][1] = stairs[2]
dp[2][2] = stairs[1] + stairs[2]

for i in range(3, n + 1) :
	dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + stairs[i];
	dp[i][2] = dp[i - 1][1] + stairs[i];

print(dp)
print(max(dp[n][1], dp[n][2]))