# 10강_1, 2, 3 더하기
# 출력값이 하나만 나오는데 틀린 부분을 모르겠음

import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n) :
    m = int(input())
    def dp(m) :
        d = [0] * 12
        d[0] = 0
        d[1] = 1
        d[2] = 2
        d[3] = 4

        for i in range(4, m + 1) :
            d[i] = d[i - 1] + d[i - 2] + d[i - 3]
        return d[m]
print(dp(m))