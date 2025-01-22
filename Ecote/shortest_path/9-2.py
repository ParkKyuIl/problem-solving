# 우선순위 큐를 사용하는 다익스트라 알고리즘

# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split()) # 노드, 간선의 갯수 입력받기
start = int(input()) # 시작 노드 번호 입력받기
graph = [[] for i in range(n+1)] # 각 노드가 어디에 연결되어있는지, 코스트는 얼마인지, 를 담을 2차원배열
distance = [INF] * (n+1) # 시작점으로부터 각 노드까지의 코스트를 담을 1차원 배열

for _ in range(m): #간선의 갯수에 대해 반복
    a,b,c = map(int,input().split()) #a로부터 b까지 갈때 c의 코스트가 든다를 저장
    graph[a].append((b,c)) # 튜플형태로 저장

def dijkstra(start): 
    q=[] #우선순위큐(최소힙)을 담을 배열 선언
    heapq.heappush(q,(0,start)) #우선순위큐에 배열과 시작노드(코스트는 0)을 삽입
    distance[start] = 0 #시작노드까지 가는데에는 코스트가 0 이므로 0으로 할당
    while q: #우선순위큐가 빌때 까지
        dist, now = heapq.heappop(q) #최소힙의 루트, 즉 가장 작은 코스트를 가진 노드를 팝, 그것의 노드번호와 시작점으로부터의 코스트를 저장
        if distance[now] < dist: #만약 꺼낸 노드의 코스트가 해당 노드에 대해 현재 저장된 코스트보다 크다면 (방문했거나, 더 비효율적인 코스트)
            continue #스킵한다
        for i in graph[now]: # 아니라면 해당 노드와 인접한 노드들을 반복방문한다
            cost = dist + i[1] # 꺼낸 노드까지의 코스트 + 꺼낸 노드의 인접노드까지의 코스트 = 새로운 총합 코스트
            if cost < distance[i[0]]: # 새로운 총합 코스트가 현재 저장된 코스트보다 효율적이라면(작다면) 
                distance[i[0]] = cost # 코스트저장 리스트에 해당 노드를 새로운 코스트로 업데이트 해준다
                heapq.heappush(q,(cost,i[0])) # 새롭게 방문 했기때문에, 우선순위큐에 넣어준다

dijkstra(start) #다익스트라 실행

for i in range(n+1): #1부터 탐색하므로, n+1에 대해 반복한다
    if(distance[i] == INF): #만약 코스트가 무한대라면
        print("INFINITY") # 인피니티 출력
    else:
        print(distance[i]) # 정수값의 코스트가 존재한다면 출력


