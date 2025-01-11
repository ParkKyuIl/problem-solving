T = int(input())
 
for test_case in range(1, T + 1):
    sentence = list(input().strip())
    n = len(sentence)
    flag = "YES"
 
     
    # 첫 번째 절반이 회문인지 확인
    for i in range(n // 2):
        if sentence[i] != sentence[n//2 - i - 1]:
            flag = "NO"
            break  # 더 이상 검사할 필요 없음
 
    # 마지막 절반이 회문인지 확인 (첫 번째 절반이 유효할 때만)
    for i in range(n // 2):
        if sentence[i] != sentence[n - i - 1]:
            flag = "NO"
            break
 
    # 결과 출력
    print(f"#{test_case} {flag}")





#     def solution(S):
#     # 회문일 때 시작
#     N = len(S)
#     if S == S[::-1]:
#         if S[:N//2] == S[:N//2][::-1] and S[N//2+1:] == S[N//2+1:][::-1]:
#             return 'YES'
#     else:
#         return 'NO'
#     return 'NO'

# T = int(input())
# for testcase in range(1, T+1):
#     S = input()
#     answer = solution(S)
#     print(f'#{testcase} {answer}')