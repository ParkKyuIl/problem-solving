# 설탕 배달 다국어
 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	357656	138088	102366	37.960%
# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (3 ≤ N ≤ 5000)

# 출력
# 상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.


# 첫째 줄에 N kg이 들어오므로 N의 변수를 받은 뒤, 수를 세기 위한 count 변수도 함께 만든다.
# 봉지의 최소 개수를 출력해야하므로, While 반복문을 사용하여 총 무게가 0kg보다 작거나 같을때까지 반복한다.
# if 문을 통해 %을 사용하여 5로 나눠 0이 된다면 count에 5를 나눈 숫자를 더해주고, 나누어 떨어지지 않는다면 총무게에 3을 빼고 count에 1을 더한다.
# else 구문으로는 0으로 나누어 떨어지지 않을 시 -1을 출력하도록 한다.

# DP로 푼다면

def sugar_delivery(N):
    # DP 배열 초기화
    dp = [float('inf')] * (N + 1)
    dp[0] = 0  # 0kg은 봉지가 필요 없음

    # DP 테이블 채우기
    for i in range(3, N + 1):
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + 1)
        if i >= 5:
            dp[i] = min(dp[i], dp[i - 5] + 1)

    # 결과 출력
    return dp[N] if dp[N] != float('inf') else -1

# 예시 실행
N = int(input())
print(sugar_delivery(N))




# 그리디로 푼다면
# import sys

# num = int(sys.stdin.readline().rstrip())
# count = 0

# while num >= 0:
#   if num % 5 == 0:
#     count += int(num // 5)
#     print(count)
#     break
  
#   num -= 3
#   count += 1
  
# else:
#   print(-1)


