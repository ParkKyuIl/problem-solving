# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	5343	2440	1987	46.145%
# 문제
# 개미가 일렬로 이동할 때, 가장 앞의 개미를 제외한 나머지 개미는 모두 앞에 개미가 한 마리씩 있다. 

# 서로 반대 방향으로 이동하던 두 개미 그룹이 좁은 길에서 만났을 때, 개미는 어떻게 지나갈까?

# 최근 연구에 의하면 위와 같은 상황이 벌어지면 개미는 서로를 점프해서 넘어간다고 한다.

# 즉, 두 그룹이 만났을 때, 1초에 한번씩 개미는 서로를 뛰어 넘는다. (한 개미가 다른 개미를 뛰어 넘고, 다른 개미는 그냥 전진한다고 생각해도 된다)

# 하지만 모든 개미가 점프를 하는 것은 아니다. 자신의 앞에 반대 방향으로 움직이던 개미가 있는 경우에만 점프를 하게 된다.

# 첫 번째 그룹이 ABC로 움직이고, 두 번째 그룹의 개미가 DEF순으로 움직인다고 하자. 그럼, 좁은 길에서 만났을 때, 개미의 순서는 CBADEF가 된다. 1초가 지났을 때는 자신의 앞에 반대방향으로 움직이는 개미가 있는 개미는 A와 D다. 따라서, 개미의 순서는 CBDAEF가 된다. 2초가 되었을 때, 자신의 앞에 반대 방향으로 움직이는 개미는 B,D,A,E가 있다. 따라서, 개미의 순서는 CDBEAF가 된다.

# T초가 지난 후에 개미의 순서를 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 첫 번째 그룹의 개미의 수 N1과 두 번째 그룹의 개미의 수 N2가 주어진다.

# 다음 두 개 줄에는 첫 번째 그룹과 두 번째 그룹의 개미의 순서가 주어진다. 각 개미는 알파벳 대문자로 표현할 수 있으며, 두 그룹에서 중복되는 알파벳은 없다.

# 마지막 줄에는 T가 주어진다. (0 ≤ T ≤ 50)

# 출력
# T초가 지난 후에 개미의 순서를 출력한다. 첫 번째 개미 그룹은 왼쪽에서 오른쪽으로 움직이고, 두 번째 그룹은 반대 방향으로 움직인다.

# 예제 입력 1 
# 3 3
# ABC
# DEF
# 0
# 예제 출력 1 
# CBADEF
# 예제 입력 2 
# 3 3
# ABC
# DEF
# 2
# 예제 출력 2 
# CDBEAF
# 예제 입력 3 
# 3 4
# JLA
# CRUO
# 3
# 예제 출력 3 
# CARLUJO


n1, n2 = map(int, input().split())
ant1 = list(input())
ant2 = list(input())
path = ant1[::-1] + ant2  # ant1의 역순 + ant2
t = int(input())
for _ in range(t):
    for i in range(len(path)-1):
        # 두 개미 그룹이 만났다면 자리를 바꾼다.
        if path[i] in ant1 and path[i+1] in ant2: # 다른 그룹의 두 개미가 만났다면 (핵심)
            path[i], path[i+1] = path[i+1], path[i]
            # 위치를 바꾼 개미가 선두 개미면 반복을 멈춘다. 
            if path[i+1] == ant1[0]:
                break
print(''.join(path))