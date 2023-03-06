import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split(' '))
picture = []
graph = [[0 for _ in range(m)] for _ in range(n)]
ls = []
for i in range(n):
  ls = list(map(int, input().split(' ')))
  for j in range(m):
    graph[i][j] = ls[j]
    if ls[j] == 1:
      picture.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited):
  global cnt
  queue = deque()
  queue.append((x, y))
  visited[x][y] = True
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      x1 = x + dx[i]
      y1 = y + dy[i]
      if 0 <= x1 < n and 0 <= y1 < m and visited[x1][y1] == 0 and graph[x1][
          y1] == 1:
        queue.append([x1, y1])
        visited[x1][y1] = True
        cnt += 1


visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 1
cnt_ls = []
for i in range(len(picture)):
  x = picture[i][0]
  y = picture[i][1]
  if not visited[x][y]:
    bfs(x, y, visited)
    cnt_ls.append(cnt)
    cnt = 1
print(len(cnt_ls))
if len(cnt_ls) <= 0:
  print(0)
else:
  print(max(cnt_ls))
