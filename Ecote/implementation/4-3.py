# 행복 왕국의 왕실 정원은 체스판과 같은 8 × 8 좌표 평면이다.
# 왕실 정원의 특정한 한 칸에 나이트가 서있다.
# 나이트는 매우 충성스러운 신하로서 매일 무술을 연마한다.
# 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
# 나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있다
# 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
# 이처럼 8 × 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는프로그램을 작성하라.
# 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a 부터 h로 표현한다
# c2에 있을 때 이동할 수 있는 경우의 수는 6가지이다
# a1에 있을 때 이동할 수 있는 경우의 수는 2가지이다
# 입력 조건
# 첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.
# 입력 문자는 a1 처럼 열과 행으로 이뤄진다.
# 출력 조건
# 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
# 입력 예시
# a1
# 출력 예시
# 2
import sys

h = sys.stdin.readline().rstrip()


x = ord(h[0]) - ord('a') + 1

# row = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

moves = [(1,2), (-1,2) ,(1,-2) ,(-1,-2) ,(2,1) , (2,-1) ,(-2,1) ,(-2,-1)]

y = int(h[1])

count = 0

print(x,y)

for dx,dy in moves:
    nx  = x + dx
    ny = y + dy
    if(1<= nx <= 8 and 1<= ny <= 8):
        print(nx,ny)
        count += 1
    

    
print(count)