# # 테이블 정의하기
# D[i] = 가치의 합을 i로 만들 때 필요한 동전 개수의 최솟값
# # 점화식 찾기
# D[i] = min(D[i-c1], D[i-c2], ..., D[i-cn]) + 1
# 문제 : 시간초과 발생!!!!!
############## DP 안됨 ###################
n, k = map(int, input().split())
coin = []
for _ in range(n):
	coin.append(int(input()))
coin.sort(reverse=True)
cnt = 0
for i in coin :
	if i > k :
		continue
	else :
		cnt += k // i
		k -= (k // i) * i

print(cnt)
