# 문제
# 지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!

# 미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.

# 지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다)  이동한다. 

# 불은 각 지점에서 네 방향으로 확산된다. 

# 지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다. 

# 지훈이와 불은 벽이 있는 공간은 통과하지 못한다.

# 입력
# 입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.

# 다음 입력으로 R줄동안 각각의 미로 행이 주어진다.

#  각각의 문자들은 다음을 뜻한다.

# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간
# J는 입력에서 하나만 주어진다.

# 출력
# 지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.

# 지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다. 

import sys
from collections import deque


def bfs(graph):
    fire = deque()
    jihoon = deque()

    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'J':
                jihoon.append((i,j))
                jihoon_dist[i][j] = 1
            elif graph[i][j] == 'F':
                fire.append((i,j))
                fire_dist[i][j] = 1
    
    while fire:
        x,y = fire.popleft()
        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c:
                if not fire_dist[nx][ny] and graph[nx][ny] != '#':
                    fire.append((nx,ny))
                    fire_dist[nx][ny] = fire_dist[x][y] + 1
            

    while jihoon:

        x,y = jihoon.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            
            if 0 <= nx < r and 0 <= ny < c:
                if not jihoon_dist[nx][ny] and graph[nx][ny] != '#':
                    if jihoon_dist[x][y]+1 < fire_dist[nx][ny] or not fire_dist[nx][ny] : # 지훈이의 현재좌표에서 한발짜국 갔을때 (+1) 불의 dist보다 작은가? or 불이 아직 번지지 않은곳인가? (0으로 초기화 했으므로..)
                        jihoon_dist[nx][ny] = jihoon_dist[x][y] + 1
                        jihoon.append((nx,ny))
            else:                  
                return jihoon_dist[x][y] 
    
    return "IMPOSSIBLE"


graph = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c = map(int,sys.stdin.readline().split())
fire_dist = [[0]*c for _ in range(r)]
jihoon_dist = [[0]*c for _ in range(r)]

for i in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))

print(bfs(graph))
        
        
        



        


            
    
    





