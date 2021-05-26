# 입력
# 입력의 첫 번째 줄은 테스트 케이스의 수 0 < N < 1001 이다.

# 각각의 테스트 케이스는 하나의 줄에 영어 소문자들로만 이루어진 두 개의 문자열이 한 개의 공백으로 구분되어 주어진다. 
# 각각의 문자열의 길이는 최대 1000 이다.

# 출력
# 각각의 테스트 케이스에 대해, 2번째 문자열이 1번째 문자열에 strfry 함수를 적용하여 얻어질 수 있는지의 여부를 "Impossible"(불가능) 
# 또는 "Possible"(가능)으로 나타내시오. (따옴표는 제외하고 출력한다.)


import sys 
answer = []
arr = []
arr_2 = []
number = int(sys.stdin.readline())

for _ in range(0,number):

    sum1 = 0
    sum2 = 0



    a , b  = sys.stdin.readline().split()

    for i in a:
        arr.append(i)
        
    for i in b:
        arr_2.append(i)

    for i in arr:
        sum1 += ord(i)

    for i in arr_2:
        sum2 += ord(i)
    
    print(arr,arr_2)
    arr = []
    arr_2 = []
  
    if sum1==sum2:
        print('Possible')

    else:
        print('Impossible')
