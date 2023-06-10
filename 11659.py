n, m = list(map(int, input().split()))
num_list = list(map(int, input().split()))
res = 0
pre_sum = [0]

for num in num_list:
    res += num
    pre_sum.append(res)
# print(pre_sum)
for i in range(m):
	a, b = map(int, input().split())
	print(pre_sum[b] - pre_sum[a - 1])
