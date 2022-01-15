# 성적이 낮은 순서로 학생 출력하기

n = int(input())
l = []
for _ in range(n):
    a, b = input().split()
    l.append((a, int(b)))

l.sort(key=lambda x: x[1])

for i in l:
    print(i[0], end=' ')