import sys

sys.setrecursionlimit(10**7)
M, N = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def find_route(cx, cy):
    if cx == M - 1 and cy == N - 1:
        return 1
    if dp[cx][cy] != -1:
        return dp[cx][cy]
    result = 0
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if 0 <= nx < M and 0 <= ny < N and _map[nx][ny] < _map[cx][cy]:
            result += find_route(nx, ny)
    dp[cx][cy] = result
    return dp[cx][cy]


print(find_route(0, 0))
