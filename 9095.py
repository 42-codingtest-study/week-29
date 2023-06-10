# # 테이블 정의하기
# D[i] = i를 1,2,3의 합으로 나타내는 방법의 수
# # 점화식 찾기
# D[4] = ?
# 1+1+1+1, 1+2+1, 2+1+1, 3+1
# 1+1+2, 2+2
# 1+3
# D[4] = 7
# # 점화식에서는 초기값이 무조건 있어야 함.
############## 설명 끝 ###################
t = int(input())
set_dp = [0,1,2,4]
for _ in range(t) :
	n = int(input())
	if n < 4 :
		print(set_dp[n])
		continue
	dp = [0 for _ in range(n+1)]
	dp[1], dp[2], dp[3] = 1, 2, 4
	for i in range(4, n + 1) :
		dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
	print(dp[n])
