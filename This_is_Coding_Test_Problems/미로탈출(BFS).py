import sys
from collections import deque
graph = []

dx = [-1,1,0,0]  #상하좌우
dy = [0,0,-1,1]
r,c = map(int,sys.stdin.readline().split())

for i in range(r):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))


def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y  = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
            print(graph)
            
    return graph[r-1][c-1]   # 출구는 (n,m)에 있다는 절대적인 전제가 있기 때문에 이렇게 가능한 것.

print(bfs(0,0))



    
