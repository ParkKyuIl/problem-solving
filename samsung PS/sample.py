# 문제
# 총 N개의 시험장이 있고, 각각의 시험장마다 응시자들이 있다. i번 시험장에 있는 응시자의 수는 Ai명이다.

# 감독관은 총감독관과 부감독관으로 두 종류가 있다. 총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명이고, 부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명이다.

# 각각의 시험장에 총감독관은 오직 1명만 있어야 하고, 부감독관은 여러 명 있어도 된다.

# 각 시험장마다 응시생들을 모두 감시해야 한다. 이때, 필요한 감독관 수의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 시험장의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 둘째 줄에는 각 시험장에 있는 응시자의 수 Ai (1 ≤ Ai ≤ 1,000,000)가 주어진다.

# 셋째 줄에는 B와 C가 주어진다. (1 ≤ B, C ≤ 1,000,000)

# 출력
# 각 시험장마다 응시생을 모두 감독하기 위해 필요한 감독관의 최소 수를 출력한다.

# 예제 입력 1 
# 1
# 1
# 1 1
# 예제 출력 1 
# 1
# 예제 입력 2 
# 3
# 3 4 5   1 2 3    
# 2 2
# 예제 출력 2 
# 7
# 예제 입력 3 
# 5
# 1000000 1000000 1000000 1000000 1000000
# 5 7
# 예제 출력 3 
# 714290
# 예제 입력 4 
# 5
# 10 9 10 9 10
# 7 20
# 예제 출력 4 
# 10
# 예제 입력 5 
# 5
# 10 9 10 9 10
# 7 2


# 입출력, // 올림 나눗셈, 등등 진짜 브3인데 왤캐 오래걸렸냐
def min_supervisors_needed(N, A, B, C):
    total_supervisors = 0
    
    for i in range(N):

        total_supervisors += 1
        remaining_students = A[i] - B  
        
        if remaining_students > 0:
            if(remaining_students % C == 0):
                total_supervisors += (remaining_students) // C  
            else: 
                total_supervisors += (remaining_students) // C+1
    
    return total_supervisors


N = int(input())  
A = list(map(int, input().split()))  
B, C = map(int, input().split())  

print(min_supervisors_needed(N, A, B, C))
