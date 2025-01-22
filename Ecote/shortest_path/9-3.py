# 모든 노드로 부터 모든 노드까지의 최단거리를 계산하는 플로이드 워셜 알고리즘

# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2


import sys
input = sys.stdin.readline
INF = int(1e9) #무한대값 설정

n = int(input()) #노드의 수 입력받기
m = int(input()) #간선의 수 입력받기

graph = [[INF] * (n+1) for _ in range(n+1)] #각 노드간의 이동코스트를 저장할 2차원배열

for a in range(1,n+1): # a,b가 같은(즉, 노드자신이 자신까지 이동하는 코스트는 0으로 지정) 케이스는 0
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m): #간선의 갯수에 대해 반복
    a,b,c = map(int,input().split()) # "a부터 b까지 가는 코스트는 c다" 에 대한 변수입력받기
    graph[a][b] = c #할당

for k in range(n+1): #3차원 배열, 저장되어있는 a -> b 의 코스트와 새롭게 계산된 a -> k -> b와 비교하여 DP성으로 계산하여 둘중 작은값 저장
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1): # 모든 노드간의 이동코스트가 담긴 2차원배열을 순회하여 결과 출력
    for b in range(1,n+1):
        if(graph[a][b] == INF):
            print("INFINITY", end = " ")
        else:
            print(graph[a][b],end = " ")
    print()