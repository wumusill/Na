# 큰 수의 법칙 단순한 풀이
n, m, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

first = l[-1]
second = l[-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

# 좀 더 효율적으로
n, m, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()

first = l[-1]
second = l[-2]

# 특정한 수열이 반복, 수열의 길이 k+1
count = m // (k+1) * k + m % (k+1)

result_2 = first * count + second * (m-count)
print(result_2)
