# 숫자 카드 게임
n, m = map(int, input().split())
min_of_row = []
for i in range(n):
    min_of_row.append(min(list(map(int, input().split()))))
print(max(min_of_row))


# 책 속 풀이, append 보다 이게 더 낫다
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_of_row)
print(result)