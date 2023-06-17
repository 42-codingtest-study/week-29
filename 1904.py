N = int(input())
n1 = 1
n2 = 2
res = 1 if N == 1 else 2

for i in range(3, N + 1):
    res = (n1 + n2) % 15746
    n1, n2 = n2, res
print(res)
