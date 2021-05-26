# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는
# 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

# 입력
# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1, 000보다 작은 자연수이다.

# 출력
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 
# 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

# a b c 받고, 곱한다음, 반복문만들어서 i , str(number)해서 형변환 한거 인자로 넣고, i 반복되면서 캐릭터 값 배열에 append ['1','2','3'..]
#그다음 반복문으로 0~N 까지 i로 도니까 list.count i로 하면 코드 길이 줄이기 가능

# 150
# 266
# 427

import sys
result_int = []
value = [int(sys.stdin.readline()) for _ in range(3)]

result_str = value[0] * value[1] * value[2]

for i in str(result_str):
    result_int.append(i)


for i in range(0,10):
    print(result_int.count(str(i))) 
