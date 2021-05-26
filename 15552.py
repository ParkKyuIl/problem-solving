# 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1, 000, 000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1, 000 이하이다.

# 출력
# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

import sys

t = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(t):
    a, b = list(map(int, sys.stdin.readline().split()))
    arr.append(a+b)

for i in range(t):
    print(arr[i])
