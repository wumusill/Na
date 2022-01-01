n, k = map(int, input().split())
cnt = 0
while n != 1:
    if n % k == 0:
        n /= k
        cnt += 1
    else:
        n -= 1
        cnt += 1
print(cnt)

# 책 속 풀이
n, k = map(int, input().split())
result = 0

while True:
    # N이 K로 나누어떨어지는 수가 될 때까지 1씩 빼야 하는 횟수 한 번에 구하기
    target = (n//k) * k
    result += (n - target)
    n = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)

print(result)