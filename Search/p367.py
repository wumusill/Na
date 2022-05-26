import sys

n, x = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

def solution(n, x, l):
    length = len(l)
    mid = length // 2
    if length > 1:
        return solution(mid, x, l[:mid]) + solution(n - mid, x, l[mid:])
    elif length == 1:
        if l[0] == x:
            return 1
        else:
            return 0

ans = solution(n, x, l)

if ans == 0:
    print(-1)
else:
    print(ans)

##############################################################################

# 정렬된 수열에서 값이 x인 원소의 개수를 세는 함수
def count_by_value(array, x):
    # 데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n - 1)

    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n - 1)

    # 개수를 반환
    return n - a + 1

# 처음 위치를 찾는 이진 탐색 함수
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid + 1, end)

# 마지막 위치를 찾는 이진 탐색 함수
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 경우 왼쪽 확인
    elif array[mid] >= target:
        return last(array, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
    else:
        return last(array, target, mid + 1, end)


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)