# 곱하기 혹인 더하기
num_list = list(map(int, list(input())))
result = num_list[0]
for i in num_list[1:]:
    if result == 0 or result == 1:
        result += i
    else:
        if i == 0 or i == 1:
            result += i
        else:
            result *= i
print(result)

