import sys


def dfs(i, j):
    df[i][j] = 0
    counts[-1] += 1

    if i > 0 and df[i - 1][j] == 1:
        dfs(i - 1, j)
    if i < n - 1 and df[i + 1][j] == 1:
        dfs(i + 1, j)
    if j > 0 and df[i][j - 1] == 1:
        dfs(i, j - 1)
    if j < n-1 and df[i][j + 1] == 1:
        dfs(i, j + 1)


n = int(sys.stdin.readline().strip())
df = []
for _ in range(n):
    df.append(list(map(int, sys.stdin.readline().strip())))

counts = []
for i in range(n):
    for j in range(n):
        if df[i][j] == 1:
            counts.append(0)
            dfs(i, j)

counts.sort()

print(len(counts))
for i in range(len(counts)):
    print(counts[i])