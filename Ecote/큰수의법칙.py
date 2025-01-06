import sys

N,M,K = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

count = 0
result = 0
arr.sort()

while True:
    for _ in range(K):
        result += arr[-1]
        count += 1
    
    result += arr[-2]
    count += 1
    if count == M:
        break

print(result)
