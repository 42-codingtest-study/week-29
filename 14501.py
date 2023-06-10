n = int(input())

tp = [[0,0]]
for i in range(n):
	a, b = map(int, input().split())
	tp.append([a,b])

dp = [0] * n+1
for i in range
