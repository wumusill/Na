# 문자열 뒤집기
s = list(input())
same = 1
other = 0
start = s[0]
temp = s[0]
for i in range(1, len(s)):
    now = s[i]
    if temp == now:
        continue
    else:
        temp = s[i]
        if start != now:
            other += 1
        else:
            same += 1

result = min(same, other)
print(result)