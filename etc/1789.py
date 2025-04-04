# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

# 입력
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

# 출력
# 첫째 줄에 자연수 N의 최댓값을 출력한다.

# 합의 공식 n*(n+1)/2


def sumFormula(n):
    return n*(n+1)/2


def searchForValue(s):
    left = 1
    right = s
    while left<=right:
        mid = (left+right)//2
        if sumFormula(mid)<=s:
            left = mid + 1
        else:
            right = mid -1
    return right


s = int(input())
print(searchForValue(s))
