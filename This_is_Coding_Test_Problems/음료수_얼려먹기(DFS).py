import sys
import time

graph = []
n,m = map(int,sys.stdin.readline().split())
count = 0

for i in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))


def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False


start = time.time()
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1

print(count)
print("time :", time.time() - start) #실행시간 체크
